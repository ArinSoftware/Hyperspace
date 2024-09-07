from django.db import models
from django.utils.text import slugify

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=50)
    is_featured = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Service, self).save(*args, **kwargs)

    class Meta:
        ordering = ['title']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'