from django.urls import path
from .views import *

urlpatterns = [

    path('', home, name='home'),

    path('admin-login/', admin_login, name='admin_login'),

    path('dashboard/', dashboard, name='dashboard'),

    path('add-product/', add_product, name='add_product'),

    path(
        'product/<int:id>/',
        product_details,
        name='product_details'
    ),
    path(
    'orders/',
    orders,
    name='orders'
),
path(
    'delete-product/<int:id>/',
    delete_product,
    name='delete_product'
),
path(
    'admin-logout/',
    admin_logout,
    name='admin_logout'
),
path(
    'update-order-status/<int:id>/<str:status>/',
    update_order_status,
    name='update_order_status'
),
path(
    'delete-order/<int:id>/',
    delete_order,
    name='delete_order'
),
]
