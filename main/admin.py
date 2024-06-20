from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'learn_more_link')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

