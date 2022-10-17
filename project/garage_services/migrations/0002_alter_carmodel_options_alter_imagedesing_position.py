# Generated by Django 4.1 on 2022-10-17 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage_services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carmodel',
            options={'verbose_name': 'Модель', 'verbose_name_plural': 'Модели'},
        ),
        migrations.AlterField(
            model_name='imagedesing',
            name='position',
            field=models.CharField(choices=[('FIRST', 'Первый экран'), ('FORM_1', 'Форма заявки 1'), ('WHY_ARE_WE', 'Мочему мы'), ('FORM_QUESTIONS', 'Остались вопросы'), ('LOGO_BG', 'Логотип на бекграунд')], max_length=25, verbose_name='Место размещения'),
        ),
    ]
