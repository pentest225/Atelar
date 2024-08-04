from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('my-account/', views.my_account, name='my_account'),

    path('wishlist/', views.wishlist, name='wishlist'),
]