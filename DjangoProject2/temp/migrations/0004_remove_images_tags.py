# Generated by Django 4.0.4 on 2022-05-12 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0003_contact_tags_images_dimension_images_format_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='tags',
        ),
    ]
