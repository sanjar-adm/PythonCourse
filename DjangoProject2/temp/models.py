from pyexpat import model
from statistics import mode
from django.db import models
from distutils.command.upload import upload

class Images(models.Model):
    name = models.CharField(max_length=222)
    image = models.ImageField(upload_to='image/%Y/%m/%d', verbose_name='Фото')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    view_image = models.IntegerField(verbose_name='Кол-во просмотров')
