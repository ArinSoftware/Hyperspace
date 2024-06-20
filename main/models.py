from django.db import models
from django.utils.text import slugify

class Service(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    image_url = models.URLField(max_length=200)
    description = models.TextField()
    learn_more_link = models.URLField(max_length=200, blank=True)
    slug = models.SlugField(unique=True, blank=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

