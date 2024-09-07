from django.contrib import admin
from .models import Service

# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display= ('title', 'is_featured', 'slug')
    search_fields= ('title', 'description')
    list_filter=('is_featured',)
