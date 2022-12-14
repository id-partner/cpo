# Generated by Django 4.1 on 2022-09-28 10:06

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('garage_services', '0001_initial'),
        ('company_info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='service',
            field=mptt.fields.TreeManyToManyField(blank=True, to='garage_services.service', verbose_name='Услуги'),
        ),
        migrations.AddField(
            model_name='review',
            name='carmodel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carmodel_reviews', to='garage_services.carmodel', verbose_name='Модель'),
        ),
        migrations.AddField(
            model_name='review',
            name='service',
            field=mptt.fields.TreeManyToManyField(blank=True, to='garage_services.service', verbose_name='Услуги'),
        ),
        migrations.AddField(
            model_name='review',
            name='service_vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='servicevehicle_reviews', to='garage_services.servicesvehicle', verbose_name='Кузов'),
        ),
        migrations.AddField(
            model_name='review',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='source_reviews', to='company_info.sourcereview', verbose_name='Кузов'),
        ),
        migrations.AddField(
            model_name='review',
            name='vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_reviews', to='garage_services.vehicle', verbose_name='Кузов'),
        ),
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.ManyToManyField(to='company_info.address', verbose_name='Адресс'),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.ManyToManyField(to='company_info.phone', verbose_name='Адресс'),
        ),
    ]
