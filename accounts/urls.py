from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('customer/<int:pk_test>/', views.customer, name="customer"),
    path('products/', views.products, name="product"),
    path('create_order/', views.create_order, name="create_order"),
    path('update_order/<str:pk>/', views.update_order, name="update_order"),
    path('delete_order/<str:pk>/', views.delete_order, name="delete_order"),
]
