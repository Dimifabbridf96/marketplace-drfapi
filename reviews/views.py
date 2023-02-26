from rest_framework import generics, permissions
from .models import Reviews
from .serializer import ReviewSerializers, ReviewDetailSerializer
from api_product.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Reviews.objects.all()

    filter_backends = [
        DjangoFilterBackend
    ]

    filterset_fields = [
        #review by products
        'product'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Reviews.objects.all()
