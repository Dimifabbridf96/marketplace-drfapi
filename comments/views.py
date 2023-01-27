from rest_framework import generics, permissions
from .models import Comment
from .serializer import CommentSerializers, CommentDetailSerializer
from api_product.permissions import IsOwnerOrReadOnly


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
