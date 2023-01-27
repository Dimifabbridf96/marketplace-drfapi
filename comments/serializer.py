from .models import Comment
from rest_framework import serializers


class CommentSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField()
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField()
    profile_image = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        user.request == obj.owner

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'product', 'comment'
        ]