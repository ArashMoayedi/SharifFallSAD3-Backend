from rest_framework import serializers

from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'code', 'price', 'rating')


class ItemRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['rating']
