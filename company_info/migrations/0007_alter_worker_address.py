# Generated by Django 4.1 on 2022-10-30 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_info', '0006_alter_worker_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='address',
            field=models.ManyToManyField(blank=True, to='company_info.address', verbose_name='Адресс'),
        ),
    ]
