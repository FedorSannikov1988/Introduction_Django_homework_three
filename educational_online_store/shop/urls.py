from django.urls import path
from .views import get_all_customer_orders_and_lists_items_in_order


urlpatterns = [

    path('get_all_customer_orders_and_lists_items_in_order/<str:name_client>/',
         get_all_customer_orders_and_lists_items_in_order,
         name='get_all_customer_orders_and_lists_items_in_order'),

]
