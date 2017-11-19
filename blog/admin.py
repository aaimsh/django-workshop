"""https://docs.djangoproject.com/en/1.11/ref/contrib/admin/"""
from django.contrib import admin
from .models import Blog
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'first_name', 'last_name')
