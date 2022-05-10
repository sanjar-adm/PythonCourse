from distutils.command.upload import upload
from django.db import models

class Employer(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    age = models.IntegerField(verbose_name='Возраст')
    salary = models.IntegerField(verbose_name='ЗП')
    skill = models.CharField(max_length=255, verbose_name='Опыт')
    image = models.ImageField(upload_to='image/%Y/%m/%d', verbose_name='Фото')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField( auto_now=True, verbose_name='Дата обновления')
    public = models.BooleanField(default=True, verbose_name='Опубликованно')