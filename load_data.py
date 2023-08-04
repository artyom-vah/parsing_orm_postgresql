import os
import sys
import pandas as pd

import time
from functools import wraps

import django
from django.db import transaction

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

django.setup()

from advertisement.models import (CityInfo,
                                  Details,
                                  Metrics,
                                  Note,
                                  Pricing,
                                  Software)


def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Подождите пока функция '{func.__name__}' загружает данные из файла 'Занятость города 2023.xlsx' в БД PostgreSQL ...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функция {func.__name__} выполнилась за {execution_time:.2f} секунд. Данные успешно загружены!")
        return result
    return wrapper


@timing_decorator
def load_data_to_db(excel_file):
    """Загружает данные из файла Ексель в БД PostgreSQL """
    df = pd.read_excel(excel_file)

    # Используем списки для bulk_create
    city_info_list = []
    metrics_list = []
    details_list = []
    pricing_list = []
    software_list = []
    note_list = []

    for index, row in df.iterrows():
        city_billboard_info = CityInfo(
            city=row['Город'],
            surface_type=row['Тип поверхности'],
            osv=row['Осв'],
            side=row['Сторона'],
            address=row['Адрес'],
            internal_code=row['Вн. код'],
            latitude=row['Широта'],
            longitude=row['Долгота'],
            photo_scheme=row.get('фото/схема', ''),
        )
        city_info_list.append(city_billboard_info)

        metrics_list.append(Metrics(
            billboard=city_billboard_info,
            digital_impressions=row['Диджтал кол-во показов'] if not pd.isna(row['Диджтал кол-во показов']) else None,
            grp=row['GRP'] if not pd.isna(row['GRP']) else None,
            ots=row['OTS'] if not pd.isna(row['OTS']) else None,
            espar_code=row['Код Эспар'],
            july_2023=row['Июль 2023'],
            august_2023=row['Август 2023'],
            september_2023=row['Сентябрь 2023'],
            october_2023=row['Октябрь 2023'],
            november_2023=row['Ноябрь 2023'],
            december_2023=row['Декабрь 2023'],
        ))

        details_list.append(Details(
            billboard=city_billboard_info,
            media_material=row['Материал носителя'],
            product_restrictions=row['Ограничения по продукту'],
            city_district=row['Городской Округ'],
            tech_requirements=row['Тех. требования'],
        ))

        pricing_list.append(Pricing(
            billboard=city_billboard_info,
            price_with_vat=row['Прайс C НДС'] if not pd.isna(row['Прайс C НДС']) else None,
            installation_price_with_vat=row['Монтаж. Прайс  с НДС'] if not pd.isna(
                row['Монтаж. Прайс  с НДС']) else None,
            reinstallation_price_with_vat=row['Переклейка. Прайс с НДС'] if not pd.isna(
                row['Переклейка. Прайс с НДС']) else None,
        ))

        software_list.append(Software(
            billboard=city_billboard_info,
            software_resolution=row['Разрешение ПО'],
        ))

        note_list.append(Note(
            billboard=city_billboard_info,
            note=row['Примечание'],
        ))

    # Используем транзакцию для ускорения
    with transaction.atomic():
        CityInfo.objects.bulk_create(city_info_list, batch_size=10000)
        Metrics.objects.bulk_create(metrics_list, batch_size=10000)
        Details.objects.bulk_create(details_list, batch_size=10000)
        Pricing.objects.bulk_create(pricing_list, batch_size=10000)
        Software.objects.bulk_create(software_list, batch_size=10000)
        Note.objects.bulk_create(note_list, batch_size=10000)


if __name__ == "__main__":
    excel_file_path = os.path.join(BASE_DIR, "Занятость города 2023.xlsx")
    load_data_to_db(excel_file_path)
