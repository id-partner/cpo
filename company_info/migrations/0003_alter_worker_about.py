# Generated by Django 4.1 on 2022-10-19 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_info', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='about',
            field=models.CharField(max_length=255, verbose_name='О сотруднике'),
        ),
    ]
