from .models import Reviews
from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime


class ReviewSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    review = serializers.IntegerField(max_value=5)

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
        
    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Reviews
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'product', 'review', 'profile_id', 'profile_image', 'is_owner'
        ]

class ReviewDetailSerializer(ReviewSerializers):
    product = serializers.ReadOnlyField(source='products.id')