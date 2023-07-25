from django.db import models

# your_app/models.py

from django.db import models

class Billboard(models.Model):
    '''Рекламный щит'''
    city = models.CharField(max_length=100)
    surface_type = models.CharField(max_length=100)
    osv = models.CharField(max_length=100)
    side = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    internal_code = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    photo_scheme = models.CharField(max_length=200)
    price_with_vat = models.DecimalField(max_digits=10, decimal_places=2)
    digital_impressions = models.DecimalField(max_digits=10, decimal_places=2)
    grp = models.DecimalField(max_digits=10, decimal_places=2)
    ots = models.DecimalField(max_digits=10, decimal_places=2)
    espar_code = models.CharField(max_length=100)
    july_2023 = models.CharField(max_length=100)
    august_2023 = models.CharField(max_length=100)
    september_2023 = models.CharField(max_length=100)
    october_2023 = models.CharField(max_length=100)
    november_2023 = models.CharField(max_length=100)
    december_2023 = models.CharField(max_length=100)
    media_material = models.CharField(max_length=200)
    product_restrictions = models.CharField(max_length=200)
    city_district = models.CharField(max_length=100)
    tech_requirements = models.CharField(max_length=200)
    installation_price_with_vat = models.DecimalField(max_digits=10, decimal_places=2)
    reinstallation_price_with_vat = models.DecimalField(max_digits=10, decimal_places=2)
    software_resolution = models.CharField(max_length=100)
    note = models.TextField()

    class Meta:
        db_table = 'billboard'

