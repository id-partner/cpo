from email.mime import image
from django.db import models
from mptt.models import TreeManyToManyField
from garage_services.models import Vehicle, CarModel, ServicesVehicle, Service

class Gallery(models.Model):
    image = models.ImageField(upload_to='image/company_info/%Y/%m/%d/', verbose_name='Изображение')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовать?')

    class Meta:
        verbose_name = 'Изображение галереи'
        verbose_name_plural = 'Изображения галереи'


class SourceReview(models.Model):
    logo = models.ImageField(upload_to='image/company_info/%Y/%m/%d/', verbose_name='Изображение')
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Площадка отзывов'
        verbose_name_plural = 'Площадки отзывов'


class Review(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя автора')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации', blank=True, null=True)
    content = models.TextField(verbose_name='Текст отзыва')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовать')
    rating = models.FloatField(verbose_name='Рейтинг', blank=True, null=True)
    photo = models.ImageField(upload_to='images/company_info/%Y/%m/%d/', blank=True, null=True, verbose_name='Фото автора')
    source = models.ForeignKey(SourceReview, on_delete=models.CASCADE, related_name='source_reviews', blank=True, null=True, verbose_name='Кузов')
    service = TreeManyToManyField(Service, blank=True, verbose_name='Услуги')
    carmodel = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='carmodel_reviews',blank=True, null=True, verbose_name='Модель')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicle_reviews',blank=True, null=True, verbose_name='Кузов')
    service_vehicle = models.ForeignKey(
        ServicesVehicle, 
        on_delete=models.CASCADE, 
        related_name='servicevehicle_reviews',
        blank=True, 
        null=True, 
        verbose_name='Кузов'
    )

    def __str__(self):
        return self.content[:20]

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'



class Partner(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    logo = models.ImageField(upload_to='image/company_info/%Y/%m/%d/', verbose_name='Изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'


class Address(models.Model):
    city =  models.CharField(max_length=255, verbose_name='Город')
    district = models.CharField(max_length=255, verbose_name='Район')
    street = models.CharField(max_length=255, verbose_name='Улица')
    building = models.CharField(max_length=255, verbose_name='Здание')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Широта')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Долгота')

    def __str__(self):
        return self.street

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

class Phone(models.Model):
    phone = models.IntegerField(verbose_name='Номер телефона')

    class Meta:
        verbose_name = 'Номер телефона'
        verbose_name_plural = 'Номера телефона'


class Contact(models.Model):
    address = models.ManyToManyField(Address, verbose_name='Адресс')
    phone = models.ManyToManyField(Phone, verbose_name='Адресс') 

    class Meta:
        verbose_name = 'Контакная информация'
        verbose_name_plural = 'Контакная информация'


class Worker(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    photo = models.ImageField(upload_to='images/company_info/%Y/%m/%d/', blank=True, null=True, verbose_name='Фото')
    position = models.CharField(max_length=255, verbose_name='Должность')
    about = models.CharField(max_length=255, verbose_name='Должность')
    service = TreeManyToManyField(Service, blank=True, verbose_name='Услуги')
    address = models.ManyToManyField(Address, verbose_name='Адресс')

    def __str__(self):
            return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'