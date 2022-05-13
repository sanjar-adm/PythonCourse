from pyexpat import model
from statistics import mode
from django.db import models
from distutils.command.upload import upload

class Image(models.Model):
    name = models.CharField(max_length=222)
    image = models.FileField(upload_to='media/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    view_image = models.IntegerField()
    tags = models.ForeignKey('Tag', on_delete=models.CASCADE)
    license = models.TextField(blank=True)
    dimension = models.CharField(max_length=255, blank=True)
    format = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.id

class Video(models.Model):
    name = models.CharField(max_length=255)
    video = models.FileField(upload_to='media/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    view_image = models.IntegerField()
    tags = models.ForeignKey('Tag', on_delete=models.CASCADE)
    license = models.TextField(blank=True)
    dimension = models.CharField(max_length=255, blank=True)
    format = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.id

class Tag(models.Model):
    title = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.id

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    CHOICES = (('Python', 'Python'), ('Java', 'Java'))
    choice = models.CharField(max_length=255, choices=CHOICES)
    text = models.TextField(blank=True)    
