from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('customer/<int:pk_test>/', views.customer, name="customer"),
    path('products/', views.products, name="product"),
]
