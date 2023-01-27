from rest_framework import generics
from .models import Profile
from .serializer import ProfileSerializer
from api_product.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()

