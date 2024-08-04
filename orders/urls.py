from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders, name='orders'),
    path('checkout',views.checkout,name='checkout'),
    path('order-complete',views.order_complete,name='order_complete'),
]