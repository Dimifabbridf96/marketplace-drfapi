from rest_framework import serializers
from .models import Products

class ProductsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Products
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'image', 'title',
             'description', 'is_owner', 'profile_id', 'profile_image'
        ]