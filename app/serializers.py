from .models import *
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


# class FoodSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Food
#         fields = ['name', 'category', 'info', 'price', 'discounted_price', 'photo', 'is_food_of_day']


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField()
    category = CategorySerializer(read_only=True)
    class Meta:
        depth = 1
        model =Food
        fields = ['name', 'category', 'info', 'price', 'discounted_price', 'photo', 'is_food_of_day']

    def discounted_price(self, obj):
        if obj.discounted_price is not None:
            return obj.discounted_price
        return None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['discounted_price'] is None:
            data.pop('discounted_price')
        return data
