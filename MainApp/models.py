from django.db import models

class Color(models.Model):
    name = models.CharField(max_length=100, verbose_name='Цвет')
    html = models.CharField(max_length=7, verbose_name='HTML код', default="#000000")
    
    def __repr__(self):
        return f"Color({self.name, self.html})"

class Item(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveBigIntegerField()
    description = models.TextField(verbose_name='Описание', max_length=1000, blank=True)
    colors = models.ManyToManyField(to=Color)

    def __repr__(self):
        return f"Item{self.name, self.brand, self.count}"
    
class Work(models.Model):
    organization = models.CharField(verbose_name='Организация', max_length=32)
    region = models.CharField(verbose_name='Регион', max_length=32, blank=True)
    site = models.CharField(verbose_name='Сайт', max_length=64, blank=True)
    position = models.CharField(verbose_name='Должность', max_length=16)
    duties = models.TextField(verbose_name='Обязанности')
    period = models.PositiveIntegerField(verbose_name='Время работы', default=1)

class Country(models.Model):
    country = models.CharField(max_length=100)
    languages = models.CharField(max_length=100)

