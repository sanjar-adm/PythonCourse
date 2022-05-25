from django.contrib.auth import get_user_model
from django.db import models
from django.forms import IntegerField


User = get_user_model()

class News(models.Model):
    title = models.CharField(
        max_length=200,
        blank=True,
        unique=True,
        db_index=True
    )

    file = models.FileField(
        upload_to='media/',
        blank=True
    )

    content = models.TextField(
        blank=True
    )
    CATEGORY = (
        ('Политика', 'Политика'),
        ('Спорт', 'Спорт'),
        ('Комедии', 'Комедии'),
        ('Музыка', 'Музыка'),
        ('Youtube', 'Youtube'),
    )

    category = models.CharField(
        max_length=200,
        choices=CATEGORY,
        blank=True,
        db_index=True
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    is_published = models.BooleanField(
        default=True
    )
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Cargo(models.Model):
    width = models.IntegerField(blank=True)
    height = models.IntegerField(blank=True)
    length = models.IntegerField(blank=True)
    volume = models.IntegerField(blank=True)
    weight = models.IntegerField(blank=True)
    price = models.IntegerField(blank=True)

    def save(self, force_insert, force_update=False, using=None, update_fields=None):
        self.volume = self.length * self.width * self.height
        self.price = self.volume*100 + self.weight*100
    
