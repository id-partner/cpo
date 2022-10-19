# Generated by Django 4.1 on 2022-10-19 14:30

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('garage_services', '0003_imagedesing_carmodel_imagedesing_vehicle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicesvehicle',
            name='service',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_vehicles', to='garage_services.service', verbose_name='Услуга'),
        ),
    ]