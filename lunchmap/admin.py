from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Shop

admin.site.register(Category)
admin.site.register(Shop)