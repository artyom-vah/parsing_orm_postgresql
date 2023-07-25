import pandas as pd
from .models import Billboard


def load_data_to_db(file_path):
    df = pd.read_excel(file_path)

    for _, row in df.iterrows():
        billboard = Billboard(
            city=row['Город'],
            surface_type=row['Тип поверхности'],
            osv=row['Осв'],
            side=row['Сторона'],
            address=row['Адрес'],
            internal_code=row['Вн. код'],
            latitude=row['Широта'],
            longitude=row['Долгота'],
            photo_scheme=row['фото/схема'],
            price_with_vat=row['Прайс C НДС'] if not pd.isna(row['Прайс C НДС']) else None,
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
            media_material=row['Материал носителя'],
            product_restrictions=row['Ограничения по продукту'],
            city_district=row['Городской Округ'],
            tech_requirements=row['Тех. требования'],
            installation_price_with_vat=row['Монтаж. Прайс  с НДС'] if not pd.isna(
                row['Монтаж. Прайс  с НДС']) else None,
            reinstallation_price_with_vat=row['Переклейка. Прайс с НДС'] if not pd.isna(
                row['Переклейка. Прайс с НДС']) else None,
            software_resolution=row['Разрешение ПО'],
            note=row['Примечание'],
        )
        billboard.save()
