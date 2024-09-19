from django.contrib import admin
from .models import Blog

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display= ('title', 'slug', 'author')
    search_fields= ('title', 'description', 'author')
    list_filter=('author',)
    row_id_fields=['author']

