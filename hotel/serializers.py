from rest_framework import serializers


from account.serializers import GuestReadSerializer
from hotel.models import Hotel, Booking, Comment

from drf_writable_nested.serializers import WritableNestedModelSerializer


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class BookingWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        exclude = ['guest']





class BookingReadSerializer(serializers.ModelSerializer):
    # room = RoomReadSerializer()
    guest = GuestReadSerializer()

    class Meta:
        model = Booking
        fields = '__all__'



class CommentSerializer(serializers.ModelSerializer):
    User = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Comment
        fields = '__all__'

