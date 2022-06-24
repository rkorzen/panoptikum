from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify


class Gallery(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    cover = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)