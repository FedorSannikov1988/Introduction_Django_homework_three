from django.urls import path
from .views import get_all_customer_orders_and_lists_items_in_order, \
                   get_list_products_ordered_by_customer_from_all_his_orders


urlpatterns = [

    path('get_all_customer_orders_and_lists_items_in_order/<str:name_client>/',
         get_all_customer_orders_and_lists_items_in_order,
         name='get_all_customer_orders_and_lists_items_in_order'),

    path('get_list_products_ordered_by_customer_from_all_his_orders/<str:name_client>/',
         get_list_products_ordered_by_customer_from_all_his_orders,
         name='get_list_products_ordered_by_customer_from_all_his_orders'),

]