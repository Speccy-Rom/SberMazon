from django.contrib import admin

from shop.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "price", "available", "created", "updated"]
    list_filter = ["available", "created", "updated"]
    list_editable = [
        "price",
        "available",
    ]  # добавляет возможность изменять перечисленные поля со страницы списка товаров,
    # не переходя к форме редактирования то- вара
    prepopulated_fields = {"slug": ("name",)}
