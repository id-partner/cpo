# Generated by Django 4.1 on 2022-10-19 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garage_services', '0003_imagedesing_carmodel_imagedesing_vehicle_and_more'),
        ('company_info', '0003_alter_worker_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.ManyToManyField(to='company_info.phone', verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='review',
            name='service_vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='servicevehicle_reviews', to='garage_services.servicesvehicle', verbose_name='Отдельная услуга'),
        ),
        migrations.AlterField(
            model_name='review',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='source_reviews', to='company_info.sourcereview', verbose_name='Источник отзыва'),
        ),
    ]
