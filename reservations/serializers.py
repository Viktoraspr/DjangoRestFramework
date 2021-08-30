from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Reservation, Room


class UserSerializer(serializers.ModelSerializer):
    rooms = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Room.objects.all())
    reservations = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Reservation.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ['id', 'username', 'reservations', 'rooms', 'owner']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
