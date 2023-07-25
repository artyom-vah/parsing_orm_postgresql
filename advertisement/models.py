from django.db import models


class Billboard(models.Model):
    city = models.CharField(max_length=100, null=True, blank=True)
    surface_type = models.CharField(max_length=100, null=True, blank=True)
    osv = models.CharField(max_length=100, null=True, blank=True)
    side = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    internal_code = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    photo_scheme = models.CharField(max_length=200, null=True, blank=True)
    price_with_vat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    digital_impressions = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    grp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ots = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    espar_code = models.CharField(max_length=100, null=True, blank=True)
    july_2023 = models.CharField(max_length=100, null=True, blank=True)
    august_2023 = models.CharField(max_length=100, null=True, blank=True)
    september_2023 = models.CharField(max_length=100, null=True, blank=True)
    october_2023 = models.CharField(max_length=100, null=True, blank=True)
    november_2023 = models.CharField(max_length=100, null=True, blank=True)
    december_2023 = models.CharField(max_length=100, null=True, blank=True)
    media_material = models.CharField(max_length=200, null=True, blank=True)
    product_restrictions = models.CharField(max_length=200, null=True, blank=True)
    city_district = models.CharField(max_length=100, null=True, blank=True)
    tech_requirements = models.CharField(max_length=200, null=True, blank=True)
    installation_price_with_vat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    reinstallation_price_with_vat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    software_resolution = models.CharField(max_length=100, null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'billboard'
