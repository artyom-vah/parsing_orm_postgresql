# Generated by Django 4.2.3 on 2023-07-25 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0002_alter_billboard_address_alter_billboard_august_2023_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='Город')),
                ('surface_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Тип поверхности')),
                ('osv', models.CharField(blank=True, max_length=100, null=True, verbose_name='Осв')),
                ('side', models.CharField(blank=True, max_length=100, null=True, verbose_name='Сторона')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Адрес')),
                ('internal_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='Вн. код')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Широта')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Долгота')),
                ('photo_scheme', models.CharField(blank=True, max_length=200, null=True, verbose_name='Фото/схема')),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_material', models.CharField(blank=True, max_length=200, null=True, verbose_name='Материал носителя')),
                ('product_restrictions', models.CharField(blank=True, max_length=200, null=True, verbose_name='Ограничения по продукту')),
                ('city_district', models.CharField(blank=True, max_length=100, null=True, verbose_name='Городской Округ')),
                ('tech_requirements', models.CharField(blank=True, max_length=200, null=True, verbose_name='Тех. требования')),
                ('billboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisement.cityinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Metrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('digital_impressions', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Диджтал кол-во показов')),
                ('grp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='GRP')),
                ('ots', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='OTS')),
                ('espar_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='Код Эспар')),
                ('july_2023', models.CharField(blank=True, max_length=100, null=True, verbose_name='Июль 2023')),
                ('august_2023', models.CharField(blank=True, max_length=100, null=True, verbose_name='Август 2023')),
                ('september_2023', models.CharField(blank=True, max_length=100, null=True, verbose_name='Сентябрь 2023')),
                ('october_2023', models.CharField(blank=True, max_length=100, null=True, verbose_name='Октябрь 2023')),
                ('november_2023', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ноябрь 2023')),
                ('december_2023', models.CharField(blank=True, max_length=100, null=True, verbose_name='Декабрь 2023')),
                ('billboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisement.cityinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Примечание')),
                ('billboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisement.cityinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_with_vat', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Прайс C НДС')),
                ('installation_price_with_vat', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Монтаж. Прайс с НДС')),
                ('reinstallation_price_with_vat', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Переклейка. Прайс с НДС')),
                ('billboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisement.cityinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('software_resolution', models.CharField(blank=True, max_length=100, null=True, verbose_name='Разрешение ПО')),
                ('billboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisement.cityinfo')),
            ],
        ),
        migrations.DeleteModel(
            name='Billboard',
        ),
    ]
