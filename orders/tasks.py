from celery import task
from django.core.mail import send_mail

from core.celery import app
from orders.models import Order


@task
def order_created(order_id):
    """Задача отправки email-уведомлений при успешном оформлении заказа."""
    order = Order.objects.get(id=order_id)
    subject = f"Order nr. {order.id}"
    message = f"Dear {order.first_name},\n\nYou have successfully placed an order.\
                  Your order id is {order.id}."
    return send_mail(subject, message, "ninda.xd@gmail.com", [order.email])
