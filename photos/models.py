from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify


class Gallery(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    user = models.ForeignKey('auth.User')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)