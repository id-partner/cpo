# Generated by Django 4.1 on 2022-10-30 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garage_services', '0004_alter_servicesvehicle_service'),
        ('blog', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='service_vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='servicevehicle_articles', to='garage_services.servicesvehicle', verbose_name='Точная услуга'),
        ),
    ]
