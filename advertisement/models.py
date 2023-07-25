from django.db import models


# class Billboard(models.Model):
#     city = models.CharField(max_length=100, null=True, blank=True, verbose_name="Город")
#     surface_type = models.CharField(max_length=100, null=True, blank=True, verbose_name="Тип поверхности")
#     osv = models.CharField(max_length=100, null=True, blank=True, verbose_name="Осв")
#     side = models.CharField(max_length=100, null=True, blank=True, verbose_name="Сторона")
#     address = models.CharField(max_length=200, null=True, blank=True, verbose_name="Адрес")
#     internal_code = models.CharField(max_length=100, null=True, blank=True, verbose_name="Вн. код")
#     latitude = models.FloatField(null=True, blank=True, verbose_name="Широта")
#     longitude = models.FloatField(null=True, blank=True, verbose_name="Долгота")
#     photo_scheme = models.CharField(max_length=200, null=True, blank=True, verbose_name="Фото/схема")
#     price_with_vat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Прайс C НДС")
#     digital_impressions = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,verbose_name="Диджтал кол-во показов")
#     grp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="GRP")
#     ots = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="OTS")
#     espar_code = models.CharField(max_length=100, null=True, blank=True, verbose_name="Код Эспар")
#     july_2023 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Июль 2023")
#     august_2023 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Август 2023")
#     september_2023 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Сентябрь 2023")
#     october_2023 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Октябрь 2023")
#     november_2023 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Ноябрь 2023")
#     december_2023 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Декабрь 2023")
#     media_material = models.CharField(max_length=200, null=True, blank=True, verbose_name="Материал носителя")
#     product_restrictions = models.CharField(max_length=200, null=True, blank=True, verbose_name="Ограничения по продукту")
#     city_district = models.CharField(max_length=100, null=True, blank=True, verbose_name="Городской Округ")
#     tech_requirements = models.CharField(max_length=200, null=True, blank=True, verbose_name="Тех. требования")
#     installation_price_with_vat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Монтаж. Прайс с НДС")
#     reinstallation_price_with_vat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Переклейка. Прайс с НДС")
#     software_resolution = models.CharField(max_length=100, null=True, blank=True, verbose_name="Разрешение ПО")
#     note = models.TextField(null=True, blank=True, verbose_name="Примечание")
#

class CityInfo(models.Model):
    """Информация о рекламной конструкции в городе"""
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name="Город")
    surface_type = models.CharField(max_length=100, null=True, blank=True, verbose_name="Тип поверхности")
    osv = models.CharField(max_length=100, null=True, blank=True, verbose_name="Осв")
    side = models.CharField(max_length=100, null=True, blank=True, verbose_name="Сторона")
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name="Адрес")
    internal_code = models.CharField(max_length=100, null=True, blank=True, verbose_name="Вн. код")
    latitude = models.FloatField(null=True, blank=True, verbose_name="Широта")
    longitude = models.FloatField(null=True, blank=True, verbose_name="Долгота")
    photo_scheme = models.CharField(max_length=200, null=True, blank=True, verbose_name="Фото/схема")


class Metrics(models.Model):
    """Метрики рекламной конструкции"""
    billboard = models.ForeignKey(CityInfo, on_delete=models.CASCADE)
    digital_impressions = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Диджтал кол-во показов")
    grp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="GRP")
    ots = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="OTS")
    espar_code = models.CharField(max_length=100, null=True, blank=True, verbose_name="Код Эспар")
    july_2023 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Июль 2023")
    august_2023 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Август 2023")
    september_2023 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Сентябрь 2023")
    october_2023 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Октябрь 2023")
    november_2023 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Ноябрь 2023")
    december_2023 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Декабрь 2023")


class Details(models.Model):
    """Детали рекламной конструкции"""
    billboard = models.ForeignKey(CityInfo, on_delete=models.CASCADE)
    media_material = models.CharField(max_length=200, null=True, blank=True, verbose_name="Материал носителя")
    product_restrictions = models.CharField(max_length=200, null=True, blank=True, verbose_name="Ограничения по продукту")
    city_district = models.CharField(max_length=100, null=True, blank=True, verbose_name="Городской Округ")
    tech_requirements = models.CharField(max_length=200, null=True, blank=True, verbose_name="Тех. требования")


class Pricing(models.Model):
    """Цены на рекламную конструкцию"""
    billboard = models.ForeignKey(CityInfo, on_delete=models.CASCADE)
    price_with_vat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Прайс C НДС")
    installation_price_with_vat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Монтаж. Прайс с НДС")
    reinstallation_price_with_vat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Переклейка. Прайс с НДС")


class Software(models.Model):
    """ПО рекламной конструкции"""
    billboard = models.ForeignKey(CityInfo, on_delete=models.CASCADE)
    software_resolution = models.CharField(max_length=100, null=True, blank=True, verbose_name="Разрешение ПО")


class Note(models.Model):
    """Примечание к рекламной конструкции"""
    billboard = models.ForeignKey(CityInfo, on_delete=models.CASCADE)
    note = models.TextField(null=True, blank=True, verbose_name="Примечание")
