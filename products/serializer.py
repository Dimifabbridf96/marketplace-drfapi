from rest_framework import serializers
from .models import Products
from likes.models import Like
from reviews.models import Reviews


class ProductsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    reviews_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    category = serializers.ChoiceField(choices=Products.CATEGORIES)
    price = serializers.IntegerField(max_value=1000)

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            liked = Like.objects.filter(
                owner=user, product=obj
            ).first()
            return liked.id if liked else None
        return None

    class Meta:
        model = Products
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'image', 'title',
             'description', 'is_owner', 'profile_id', 'profile_image', 'category', 'price', 'like_id', 'likes_count',
             'comments_count','reviews_count'
        ]