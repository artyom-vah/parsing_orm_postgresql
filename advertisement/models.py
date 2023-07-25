from django.db import models


class CityInfo(models.Model):
    """Информация о рекламной конструкции в городе"""
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name="Город")
    surface_type = models.CharField(max_length=100, null=True, blank=True, verbose_name="Тип поверхности")
    osv = models.CharField(max_length=90, null=True, blank=True, verbose_name="Осв")
    side = models.CharField(max_length=111, null=True, blank=True, verbose_name="Сторона")
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name="Адрес")
    internal_code = models.CharField(max_length=100, null=True, blank=True, verbose_name="Вн. код")
    latitude = models.FloatField(null=True, blank=True, verbose_name="Широта")
    longitude = models.FloatField(null=True, blank=True, verbose_name="Долгота")
    photo_scheme = models.CharField(max_length=200, null=True, blank=True, verbose_name="Фото/схема")

    def __str__(self):
        return f'Город: {self.city}, Адрес: {self.address}, Тип поверхности: {self.surface_type}'


class Metrics(models.Model):
    """Метрики рекламной конструкции"""
    billboard = models.ForeignKey(CityInfo, on_delete=models.CASCADE)
    digital_impressions = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Диджтал кол-во показов")
    grp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="GRP")
    ots = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="OTS")
    espar_code = models.CharField(max_length=110, null=True, blank=True, verbose_name="Код Эспар")
    july_2023 = models.CharField(max_length=400, null=True, blank=True, verbose_name="Июль 2023")
    august_2023 = models.CharField(max_length=300, null=True, blank=True, verbose_name="Август 2023")
    september_2023 = models.CharField(max_length=300, null=True, blank=True, verbose_name="Сентябрь 2023")
    october_2023 = models.CharField(max_length=400, null=True, blank=True, verbose_name="Октябрь 2023")
    november_2023 = models.CharField(max_length=300, null=True, blank=True, verbose_name="Ноябрь 2023")
    december_2023 = models.CharField(max_length=150, null=True, blank=True, verbose_name="Декабрь 2023")

    def __str__(self):
        return f'''Рекламная конструкция: {self.billboard.city}, {self.billboard.address}, {self.billboard.side},
                   Диджтал кол-во показов: {self.digital_impressions}, GRP: {self.grp}, OTS: {self.ots}'''


class Details(models.Model):
    """Детали рекламной конструкции"""
    billboard = models.ForeignKey(CityInfo, on_delete=models.CASCADE)
    media_material = models.CharField(max_length=200, null=True, blank=True, verbose_name="Материал носителя")
    product_restrictions = models.CharField(max_length=200, null=True, blank=True, verbose_name="Ограничения по продукту")
    city_district = models.CharField(max_length=200, null=True, blank=True, verbose_name="Городской Округ")
    tech_requirements = models.CharField(max_length=200, null=True, blank=True, verbose_name="Тех. требования")

    def __str__(self):
        return f'''Детали рекламной конструкции:
                   Рекламная конструкция: {self.billboard.city}, {self.billboard.address}, {self.billboard.side}
                   Материал носителя: {self.media_material}
                   Ограничения по продукту: {self.product_restrictions}
                   Городской Округ: {self.city_district}
                   Тех. требования: {self.tech_requirements}'''


class Pricing(models.Model):
    """Цены на рекламную конструкцию"""
    billboard = models.ForeignKey(CityInfo, on_delete=models.CASCADE)
    price_with_vat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Прайс C НДС")
    installation_price_with_vat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Монтаж. Прайс с НДС")
    reinstallation_price_with_vat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Переклейка. Прайс с НДС")

    def __str__(self):
        return f'''Цены на рекламную конструкцию:
                      Рекламная конструкция: {self.billboard.city}, {self.billboard.address}, {self.billboard.side}
                      Прайс C НДС: {self.price_with_vat}
                      Монтаж. Прайс с НДС: {self.installation_price_with_vat}
                      Переклейка. Прайс с НДС: {self.reinstallation_price_with_vat}'''


class Software(models.Model):
    """ПО рекламной конструкции"""
    billboard = models.ForeignKey(CityInfo, on_delete=models.CASCADE)
    software_resolution = models.CharField(max_length=200, null=True, blank=True, verbose_name="Разрешение ПО")

    def __str__(self):
        return f'''ПО рекламной конструкции:
                   Рекламная конструкция: {self.billboard.city}, {self.billboard.address}, {self.billboard.side}
                   Разрешение ПО: {self.software_resolution}'''


class Note(models.Model):
    """Примечание к рекламной конструкции"""
    billboard = models.ForeignKey(CityInfo, on_delete=models.CASCADE)
    note = models.TextField(null=True, blank=True, verbose_name="Примечание")

    def __str__(self):
        return f'''Примечание к рекламной конструкции:
                   Рекламная конструкция: {self.billboard.city}, {self.billboard.address}, {self.billboard.side}
                   Примечание: {self.note}'''
