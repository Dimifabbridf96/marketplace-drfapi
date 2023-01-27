from rest_framework import generics, permissions
from api_product.permissions import IsOwnerOrReadOnly
from .serializer import ProductsSerializer
from .models import Products


class ProductsList(generics.ListCreateAPIView):
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Products.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductsDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductsSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Products.objects.all()

