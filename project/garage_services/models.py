from secrets import choice
from tokenize import group
from mptt.models import MPTTModel, TreeForeignKey,TreeManyToManyField
from django.contrib.sites.models import Site
from django.db import models


class SEOservices(MPTTModel):
    # Или стоит унаследовать от стандартных и добавлять вторым пунктом?
    title = models.CharField(max_length=80, blank=True, null=True)
    seo_description = models.CharField(max_length=255, blank=True, null=True)
    canonical_url = models.URLField(blank=True, null=True)
    meta_robots = models.CharField(max_length=50, blank=True, null=True)
    h1 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        abstract = True


class Service(SEOservices):
    name = models.CharField(max_length=255, verbose_name='Название Услуги')
    slug = models.SlugField(max_length=255, unique=True)
    in_menu = models.BooleanField(default=True, verbose_name='Добавляем ли в меню?')
    order = models.IntegerField(default=1, verbose_name='Порядок')
    description = models.CharField(max_length=255, blank=True, verbose_name='Описание')
    content = models.TextField(blank=True)
    icon = models.ImageField(upload_to='images/category/%Y/%m/%d/', blank=True, verbose_name='Иконка категории')
    parent = TreeForeignKey(
        'self', on_delete=models.DO_NOTHING, null=True,
        blank=True, related_name='child_category',
        verbose_name='Родительская услуга'
    )
    min_normochas = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Минимально нормочасов')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Group(models.Model):
    site = models.ForeignKey(Site, blank=True, null=True, on_delete=models.CASCADE)
    name_ru = models.CharField(max_length=255, verbose_name='Название на русском')
    name_en = models.CharField(max_length=255, verbose_name='Название на английском')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    logo = models.ImageField(upload_to='image/logo/%Y/%m/%d/', verbose_name='Логотип концерна')
    services = TreeManyToManyField(Service, verbose_name='Улсуги')
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Концерн'
        verbose_name_plural = 'Концерны'


class Brand(models.Model):
    site = models.ForeignKey(Site, blank=True, null=True, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True, 
                                related_name='group_brands', verbose_name='Концерн')
    name_ru = models.CharField(max_length=255, verbose_name='Название на русском')
    name_en = models.CharField(max_length=255, verbose_name='Название на английском')
    logo = models.ImageField(upload_to='image/logo/%Y/%m/%d/', verbose_name='Логотип марки')
    description = models.TextField(blank=True, verbose_name='Описание')
    services = TreeManyToManyField(Service, verbose_name='Улсуги')
    price_normochas = models.DecimalField(max_digits=19, decimal_places=2, blank=True,
                                            null=True, verbose_name='Стоимость нормочаса')
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'


class CarModel(models.Model):
    name_en = models.CharField(max_length=255, verbose_name='Название на английском')
    name_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название на русском')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand_carmodels', verbose_name='Марка')
    description = models.TextField(blank=True, verbose_name='Описание')
    image_model = models.ImageField(upload_to='image/services/%Y/%m/%d/', verbose_name='Логотип концерна')
    services = TreeManyToManyField(Service, verbose_name='Услуги')
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name_ru

class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'


class Vehicle(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    start_year = models.IntegerField(max_length=4, verbose_name='Год начала производства')
    stop_year = models.IntegerField(max_length=4, blank=True, null=True, verbose_name='Год прекращения производства')
    carmodel = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='carmodel_vehicles', verbose_name='Модель')
    image_model = models.ImageField(upload_to='image/services/%Y/%m/%d/', verbose_name='Логотип концерна')
    services = TreeManyToManyField(Service, verbose_name='Услуги')
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кузов'
        verbose_name_plural = 'Кузова'


class ServicesVehicle(SEOservices):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicle_services', verbose_name='Кузов')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_vehicles', verbose_name='Услуга')
    min_normochas = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Минимально нормочасов')
    normochas = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True, verbose_name='Нормочасов')

    class Meta:
        verbose_name = 'Точная услуга'
        verbose_name_plural = 'Точные услуги'


class Engine(models.Model):
    FUEL_CHOICES = [
        ('PETROL', 'Бензиновый'),
        ('DIESEL', 'Дизельный'),
        ('ELECTRIC', 'Электрический'),
        ('HYBRID', 'Гибридный')
    ]
    model =  models.CharField(max_length=255, verbose_name='Модель')
    fuel = models.CharField(max_length=255, choices=FUEL_CHOICES, verbose_name='Тип двигателя')
    horse_power = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Лошадиных сил')
    torque = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Лошадиных сил')
    vehicle = models.ManyToManyField(Vehicle, on_delete=models.CASCADE, related_name='vehicle_engines', blank=True, null=True, verbose_name='Кузов')

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Двигатель'
        verbose_name_plural = 'Двигатели'


class Transmission(models.Model):
    TRANSMISSION_CHOICES = [
        ('MANUAL', 'МКПП'),
        ('AVTOMAT', 'АКПП'),
        ('ROBOT', 'Робот'),
        ('VARIATOR', 'Вариатор'),
    ]
    model =  models.CharField(max_length=255, verbose_name='Модель')
    type = models.CharField(max_length=255, choices=TRANSMISSION_CHOICES, verbose_name='Тип КПП')
    vendor = models.CharField(max_length=255, blank=True, null=True, verbose_name='Производитель')
    vehicle = models.ManyToManyField(Vehicle, on_delete=models.CASCADE, related_name='vehicle_transmissions', blank=True, null=True, verbose_name='Кузов')

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Коробка передач'
        verbose_name_plural = 'Коробки передач'
    

class Drive(models.Model):
    type = models.CharField(max_length=255, verbose_name='Тип привода')
    vehicle = models.ManyToManyField(Vehicle, on_delete=models.CASCADE, related_name='vehicle_transmissions', blank=True, null=True, verbose_name='Кузов')

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Коробка передач'
        verbose_name_plural = 'Коробки передач'


class Lead(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Имя')
    phone = models.IntegerField(max_length=10 , verbose_name='Номер телефона')
    url =  models.URLField(null=True, blank=True, verbose_name='Страница с которой пришла заявка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'



class ImageDesing(models.Model):
    POSITION_CHOICES = [
        ('FIRST', 'Первый экран'),
        ('FORM_1', 'Форма заявки 1'),
        ('WHY_ARE_WE', 'Мочему мы'),
        ('FORM_QUESTIONS', 'Остались вопросы')
    ]
    image = models.ImageField(upload_to='image/desing/%Y/%m/%d/', verbose_name='Фото для дизайна')
    position = models.CharField(max_length=25, choices=POSITION_CHOICES, verbose_name='Место размещения')
    group = models.ManyToManyField(Group, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Концерн')
    brand = models.ManyToManyField(Brand, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Марка')

    class Meta:
        verbose_name = 'Изображение для оформления'
        verbose_name_plural = 'Изображения для оформления'
