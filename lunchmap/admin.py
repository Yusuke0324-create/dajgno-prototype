from django.contrib import admin

# Register your models here.
from .models import Category, Shop,Blog

admin.site.register(Category)
admin.site.register(Shop)
admin.site.register(Blog)
