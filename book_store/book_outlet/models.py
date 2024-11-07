from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify
import itertools


class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, default="", null=False,db_index=True)

    def save(self, *args, **kwargs):
        # Generate initial slug
        self.slug = slugify(self.title)
        # Ensure the slug is unique
        for x in itertools.count(1):
            if not Book.objects.filter(slug=self.slug).exists():
                break
            self.slug = f'{slugify(self.title)}-{x}'

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f'{self.title} ({self.rating})'
