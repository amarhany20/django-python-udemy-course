# Generated by Django 5.0.6 on 2024-06-15 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0002_book_author_book_is_bestselling_alter_book_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
