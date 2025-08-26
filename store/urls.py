from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/expensive/', views.expensive_products, name='expensive_products'),
    path('products/food/', views.food_products, name='food_products'),
    path('products/search/', views.search_products, name='search_products'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/create/', views.create_product, name='create_product'), 
]
