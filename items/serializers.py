from rest_framework import serializers

from .models import Item, Rating, PromotionRequest


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'code', 'price', 'rating')


class ItemFullSerializer (serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class ItemRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"


class PromotionRequestSerializer(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())

    class Meta:
        model = PromotionRequest
        fields = "__all__"
