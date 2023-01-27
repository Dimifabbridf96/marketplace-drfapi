from rest_framework import generics
from api_product.permissions import IsOwnerOrReadOnly
from .serializer import ProductsSerializer
from .models import Products

class ProductsSerializer(generics.ListAPIView):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
