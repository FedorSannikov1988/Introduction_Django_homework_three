from django.shortcuts import render
from shop.models import Client, Order
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def get_all_customer_orders_and_lists_items_in_order(request,
                                                     name_client: str):

    client = \
        Client.objects.filter(name=name_client).first()

    orders = \
        Order.objects.filter(client=client).all()

    context = {
        "name_client": name_client,
        "orders": orders
    }

    return render(request, "get_all_customer_orders_and_lists_items_in_order.html", context)


def for_sort_products_in_ordered(date_and_time_placing_order: datetime,
                                 what_is_it_compared_to: datetime,
                                 list_products: list,
                                 order: Order):

    if date_and_time_placing_order >= what_is_it_compared_to:
        for one_product in order.product.all():
            if one_product not in list_products:
                list_products.append(one_product)


def get_list_products_ordered_by_customer_from_all_his_orders(request,
                                                              name_client: str):

    client = \
        Client.objects.filter(name=name_client).first()

    orders = \
        Order.objects.filter(client=client).all()

    current_datetime = datetime.now()

    seven_days_ago = current_datetime - timedelta(days=7)
    thirty_days_ago = current_datetime - timedelta(days=30)
    #year_days_ago = current_datetime - timedelta(days=365)
    year_days_ago_v2 = current_datetime - relativedelta(years=1)

    seven_days_ago_list_product: list = []
    thirty_days_ago_list_product: list = []
    year_ago_list_product: list = []

    for order in orders:

        date_and_time_placing_order: datetime = \
            order.date_and_time_placing_order.replace(tzinfo=None)

        for_sort_products_in_ordered(list_products=
                                     seven_days_ago_list_product,
                                     date_and_time_placing_order=
                                     date_and_time_placing_order,
                                     what_is_it_compared_to=
                                     seven_days_ago,
                                     order=
                                     order)

        for_sort_products_in_ordered(list_products=
                                     thirty_days_ago_list_product,
                                     date_and_time_placing_order=
                                     date_and_time_placing_order,
                                     what_is_it_compared_to=
                                     thirty_days_ago,
                                     order=
                                     order)

        for_sort_products_in_ordered(list_products=
                                     year_ago_list_product,
                                     date_and_time_placing_order=
                                     date_and_time_placing_order,
                                     what_is_it_compared_to=
                                     year_days_ago_v2,
                                     order=
                                     order)

    context = {
        "name_client": name_client,
        "products": [
            seven_days_ago_list_product,
            thirty_days_ago_list_product,
            year_ago_list_product
        ]
    }

    return render(request,
                  "get_list_products_ordered_by_customer_from_all_his_orders.html",
                  context)
