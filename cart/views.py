from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from coupons.forms import CouponApplyForm
from shop.models import Product

from .cart import Cart
from .forms import CartAddProductForm


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
    return redirect("cart_detail")


def cart_remove(request, product_id):
    """Удаление товара из корзины."""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("cart_detail")


def cart_detail(request):
    """Отображает корзину, основываясь на данных, сохраненных в сессии request.session."""
    context = {}
    cart = Cart(request)
    for item in cart:
        item["update_quantity_form"] = CartAddProductForm(
            initial={"quantity": item["quantity"], "update": True},
        )  # Изменение количества товаров в корзине.

    context["cart"] = cart
    coupon_apply_form = CouponApplyForm()
    context["coupon_apply_form"] = coupon_apply_form
    return render(request, "cart/detail.html", context)
