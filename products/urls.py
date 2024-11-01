from django.urls import path
from .views import ProductListView, ProductDetailView, AddProductView, CategoryListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/add/', AddProductView.as_view(), name='add_product'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
]
