from rest_framework import generics, permissions, filters
from api_product.permissions import IsOwnerOrReadOnly
from .serializer import ProductsSerializer
from .models import Products
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend


class ProductsList(generics.ListAPIView):
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Products.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('liked', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        #user feed
        'owner__followed__owner__profile',
        #user liked products
        'liked__owner__profile',
        #user products
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
        'category',
        'description'

    ]

    ordering_fields = [
        'comments_count',
        'likes_count',
        'owner__comment__created_at',
        'owner__liked__created_at',
        'price',

    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductsDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductsSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Products.objects.annotate(
        comments_count=Count('owner__comment', distinct=True),
        likes_count=Count('owner__like', distinct=True)
    ).order_by('-created_at')

