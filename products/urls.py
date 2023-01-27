from django.urls import path
from .models import Products
from products import views

urlpatterns = [
    path('products/', views.ProductsList.as_view()),
    path('products/<int:pk>', views.ProductsDetails.as_view()),
]