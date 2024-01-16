from django.shortcuts import render
from shop.models import Client, Order


def get_all_customer_orders_and_lists_items_in_order(request, name_client: str):

    client = \
        Client.objects.filter(name=name_client).first()

    orders = \
        Order.objects.filter(client=client).all()

    context = {
        "name_client": name_client,
        "orders": orders
    }

    return render(request, "get_all_customer_orders_and_lists_items_in_order.html", context)

