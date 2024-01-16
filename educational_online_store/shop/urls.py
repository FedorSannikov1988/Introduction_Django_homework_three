from django.urls import path
from .views import get_all_customer_orders_and_lists_items_in_order, \
                   get_list_products_ordered_by_customer_from_all_his_orders, \
                   GetListProductsOrderedByCustomerIdFromAllHisOrders, \
                   GetListProductsOrderedByCustomerIdFromAllHisOrdersV2


urlpatterns = [

    path('get_all_customer_orders_and_lists_items_in_order/<str:name_client>/',
         get_all_customer_orders_and_lists_items_in_order,
         name='get_all_customer_orders_and_lists_items_in_order'),

    path('get_list_products_ordered_by_customer_from_all_his_orders/<str:name_client>/',
         get_list_products_ordered_by_customer_from_all_his_orders,
         name='get_list_products_ordered_by_customer_from_all_his_orders'),

    #только для того что бы поработать с классами вариант №2:
    path('get_list_products_ordered_by_customer_from_all_his_orders_v2/<int:id_client>/',
         GetListProductsOrderedByCustomerIdFromAllHisOrders.as_view(),
         name='get_list_products_ordered_by_customer_from_all_his_orders_v2'),

    #только для того что бы поработать с классами вариант №3:
    path('get_list_products_ordered_by_customer_from_all_his_orders_v3/<int:id_client>/',
         GetListProductsOrderedByCustomerIdFromAllHisOrdersV2.as_view(),
         name='get_list_products_ordered_by_customer_from_all_his_orders_v3'),
]
