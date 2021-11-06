from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'slug']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']

    def get_prepopulated_fields(self, request, obj=None):
        # добавляет возможность изменять перечисленные поля со страницы списка товаров,
        # не переходя к форме редактирования то- вара
        return {'slug': ('name',)}


