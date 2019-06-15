from django.db import models


class ProductCategory(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(verbose_name='имя категории', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание категории', blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)  # привязка к категории
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name='краткое описание', max_length=60, blank=True)
    description = models.TextField(verbose_name='подробное описание', blank=True)
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)

    def __str__(self):
        return "{} ({})".format(self.name, self.category.name)
