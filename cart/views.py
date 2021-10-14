from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from cart.cart import Cart
from cart.forms import CartAddProductForm
from shop.models import Product


@require_POST  # обернули функцию cart_add() декоратором require_POST, чтобы обратиться к ней можно было только
# методом POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd["quantity"],
            update_quantity=cd["update"],
        )
    return redirect("cart:cart_detail")


def cart_remove(request, product_id):
    """Удаление товара из корзины"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("cart:cart_detail")


def cart_detail(request):
    """Отображает корзину, основываясь на данных, сохраненных в сессии request.session."""
    context = {}
    cart = Cart(request)
    context["cart"] = cart
    return render(request, "cart/detail.html", context)
