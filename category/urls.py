from django.urls import path
from category import views

urlpatterns = [
    path('category/', views.CategoryList.as_view()),
    path('category/<int:pk>', views.CategoryDetails.as_view())
]