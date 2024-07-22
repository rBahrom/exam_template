from django.contrib import admin
from .models import Shop, Category
from import_export.admin import ImportExportModelAdmin

# admin.site.register(Products)

@admin.register(Shop)
class CategoriesAdmin(ImportExportModelAdmin):
    list_display = ('title', 'category', 'slug', 'image', 'descriptions', 'miqdor', 'count')
    ordering = ('title', )

@admin.register(Category)
class ProductsAdmin(ImportExportModelAdmin):
    list_display = ('category',)
    ordering = ('category', )
