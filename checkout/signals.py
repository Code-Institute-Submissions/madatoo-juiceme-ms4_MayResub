from django.db.models.signals import post_save, post_delete
from django.dispatch import reciver

from .models import OrderLineItem

@reciver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    update order total on lineitem update/create
    """
    instance.order.update_total()

@reciver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, created, **kwargs):
    """
    update order total on lineitem delete
    """
    instance.order.update_total()
    