from .models import Comment
from rest_framework import serializers


class CommentSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'product', 'comment', 'profile_id', 'profile_image', 'is_owner'
        ]

class CommentDetailSerializer(CommentSerializers):
    product = serializers.ReadOnlyField(source='products.id')