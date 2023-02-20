from rest_framework import generics, permissions
from .serializer import CategorySerializer
from .models import Category
from api_product.permissions import IsOwnerOrReadOnly


class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
