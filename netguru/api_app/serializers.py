from rest_framework import serializers
from .models import Cars


class CarCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cars
        fields = ('id', 'make', 'model', 'user')


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'


class CarRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ('id', 'rating', 'user')
