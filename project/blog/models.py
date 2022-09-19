from django.db import models
from mptt.models import TreeManyToManyField
from garage_services.models import Vehicle, CarModel, ServicesVehicle, Service, SEO




class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, unique=True)
    in_menu = models.BooleanField(default=True, verbose_name='Добавляем в меню?')
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название тега')
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Article(SEO):
    tile = models.CharField(max_length=255, verbose_name='Тайтл Записи')
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField(verbose_name='Контент Записи')
    short_description = models.CharField(max_length=255, verbose_name='Короткое описание')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовать?')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    categories = models.ManyToManyField(Category, verbose_name='Категории')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    service = TreeManyToManyField(Service, blank=True, null=True, verbose_name='Услуги')
    carmodel = models.ForeignKey(
        CarModel, 
        on_delete=models.CASCADE, 
        related_name='carmodel_articles',
        blank=True, 
        null=True, 
        verbose_name='Модель'
    )
    vehicle = models.ForeignKey(
        Vehicle, 
        on_delete=models.CASCADE, 
        related_name='vehicle_articles',                         
        blank=True, 
        null=True, 
        verbose_name='Кузов'
    )
    service_vehicle = models.ForeignKey(ServicesVehicle, on_delete=models.CASCADE, related_name='servicevehicle_articles',
                                    blank=True, null=True, verbose_name='Кузов')
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'



class ArticleGallery (models.Model):
    image = models.ImageField(upload_to='image/blog/%Y/%m/%d/', verbose_name='Изображение записи')
    mai_image = models.BooleanField(default=False, verbose_name='Главное фото?')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_images',
                                    blank=True, null=True, verbose_name='Запись')

    class Meta:
        verbose_name = 'Изображение записи'
        verbose_name_plural = 'Изображения записи'


