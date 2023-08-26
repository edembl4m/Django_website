from django.db import models
from django.urls import reverse


def get_product_url(obj, viewname):
    ct_model = obj.__class__._meta.model_name + "s"
    return reverse(viewname, kwargs={'ct_model': ct_model, "slug": obj.slug})


class CategoryManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset()

    def get_categories_for_nav(self):
        # models = get_models_for_nav('mopeds', 'quadbikes')
        qs = list(self.get_queryset())
        data = [
            dict(name=c.name, url=c.get_absolut_url())
            for c in qs
        ]
        return data


class Category(models.Model):

    name = models.CharField('Название категории', max_length=255)
    slug = models.SlugField(unique=True)
    objects = CategoryManager()

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):

    class Meta:
        abstract = True
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=255)
    slug = models.SlugField(unique=True)
    price = models.DecimalField('Цена', max_digits=9, decimal_places=2)
    image = models.ImageField('Изображение')
    description = models.TextField('Описание', null=True)
    # availability = models.CharField('Наличие', max_length=50)
    availability = models.BooleanField('Наличие', default=True)

    def __str__(self):
        return self.name


class CoolingSystem(models.Model):
    title = models.CharField('Название', max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Система охлаждения"
        verbose_name_plural = "Системы охлаждения"


class Transmission(models.Model):
    title = models.CharField('Название', max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Трансмиссия"
        verbose_name_plural = "Трансмиссия"


class LaunchSystem(models.Model):
    title = models.CharField('Название', max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Система запуска"
        verbose_name_plural = "Системы запуска"


class FrontBrakes(models.Model):
    title = models.CharField('Название', max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Передние тормоза"
        verbose_name_plural = "Передние тормоза"


class RearBrakes(models.Model):
    title = models.CharField('Название', max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задние тормоза"
        verbose_name_plural = "Задние тормоза"


# class Mototechnics(Product):

#     engine_capacity = models.CharField('Объем двигателя', max_length=50)    # объем двигателя
#     cooling_system = models.ForeignKey(CoolingSystem, verbose_name='Система охлаждения', on_delete=models.CASCADE, default='')    # система охлаждения
#     # fuel = models.CharField('Топливо', max_length=50) # топливо
#     fuel_consumption = models.CharField('Расход топлива', max_length=50)    # расход топлива
#     # transmission    # трансмиссия
#     # launch_system   # система запуска
#     # front_brakes    # передние тормоза
#     # rear_brakes # задние тормоза
#     front_wheel = models.CharField('Переднее колесо', max_length=100)   # переднее колесо
#     rear_wheel = models.CharField('Заднее колесо', max_length=100)    # заднее колесо

#     def __str__(self):
#         return "{} : {}".format(self.category.name, self.name)

#     class Meta:
#         verbose_name = "Мототехника"


class Mototechnics(models.Model):

    engine_capacity = models.CharField('Объем двигателя', max_length=50)    # объем двигателя
    cooling_system = models.ForeignKey(CoolingSystem, verbose_name='Система охлаждения', on_delete=models.CASCADE, default='')    # система охлаждения
    fuel = models.CharField('Топливо', max_length=50) # топливо
    fuel_consumption = models.CharField('Расход топлива', max_length=50)    # расход топлива
    transmission = models.ForeignKey(Transmission, verbose_name='Трансмиссия ', on_delete=models.CASCADE, default='')   # трансмиссия
    launch_system = models.ForeignKey(LaunchSystem, verbose_name='Система запуска', on_delete=models.CASCADE, default='')  # система запуска
    front_brakes = models.ForeignKey(FrontBrakes, verbose_name='Передние тормоза', on_delete=models.CASCADE, default='')   # передние тормоза
    rear_brakes = models.ForeignKey(RearBrakes, verbose_name='Задние тормоза', on_delete=models.CASCADE, default='')    # задние тормоза
    front_wheel = models.CharField('Переднее колесо', max_length=100)   # переднее колесо
    rear_wheel = models.CharField('Заднее колесо', max_length=100)    # заднее колесо

    # def __str__(self):
    #     return "{} : {}".format(self.category.name, self.name)

    class Meta:
        abstract = True
        verbose_name = "Мототехника"
        verbose_name_plural = "Мототехника"



class Moped(Product, Mototechnics):
    
    def __str__(self):
        return "{} : {}".format(self.category.name, self.name)

    class Meta:
        verbose_name = "Мопед"
        verbose_name_plural = "Мопеды"

    def get_absolut_url(self):
        return get_product_url(self, 'product_detail')


class Scooter(Product, Mototechnics):
    
    def __str__(self):
        return "{} : {}".format(self.category.name, self.name)

    class Meta:
        verbose_name = "Скутер"
        verbose_name_plural = "Скутеры"

    def get_absolut_url(self):
        return get_product_url(self, 'product_detail')


class QuadBike(Product, Mototechnics):
    
    def __str__(self):
        return "{} : {}".format(self.category.name, self.name)

    class Meta:
        verbose_name = "Квадроцикл"
        verbose_name_plural = "Квадроциклы"

    def get_absolut_url(self):
        return get_product_url(self, 'product_detail')


class PitBike(Product, Mototechnics):
    
    def __str__(self):
        return "{} : {}".format(self.category.name, self.name)

    class Meta:
        verbose_name = "Питбайк"
        verbose_name_plural = "Питбайки"

    def get_absolut_url(self):
        return get_product_url(self, 'product_detail')


class CrossTechnique(Product, Mototechnics):
    
    def __str__(self):
        return "{} : {}".format(self.category.name, self.name)

    class Meta:
        verbose_name = "Кроссовая техника"
        verbose_name_plural = "Кроссовая техника"

    def get_absolut_url(self):
        return get_product_url(self, 'product_detail')


class Gallery(models.Model):
    image = models.ImageField('Картинка')
    product = models.ForeignKey(Moped, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"