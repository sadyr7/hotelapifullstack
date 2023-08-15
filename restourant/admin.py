from django.contrib import admin

from restourant.models import Category_restourant, Product, Like

# Register your models here.

admin.site.register(Category_restourant)
admin.site.register(Product)
admin.site.register(Like)