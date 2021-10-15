from django.shortcuts import get_object_or_404, render

from cart.forms import CartAddProductForm
from shop.models import Category, Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {
        "category": category,
        "categories": categories,
        "products": products,
    }
    return render(request, "shop/product/list.html", context)


def product_detail(request, id, slug):
    context = {}
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context["product"] = product
    context["cart_product_form"] = cart_product_form
    return render(request, "shop/product/detail.html", context)
