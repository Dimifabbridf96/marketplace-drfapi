from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField(source='product.title')

    class Meta:
        model = Category
        fields = [
            'id', 'name', 'slug', 'description', 'product'
        ]

        def create(self, validated_data):
            return super().create(validated_data)
            