from rest_framework import generics, filters
from .models import Profile
from .serializer import ProfileSerializer
from api_product.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend


class ProfileList(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        products_count=Count('owner__products', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        # user following profiles
        'owner__following__followed__profile',
        # user that follow
        'owner__followed__owner__profile',
    ]

    ordering_fields = [
        'products_count',
        'followers_count',
        'following_count',
        'owner__followed__created_at'
        'owner__following__created_at'
    ]


class ProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        products_count=Count('owner__products', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')

