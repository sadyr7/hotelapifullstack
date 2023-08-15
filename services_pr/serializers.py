
from rest_framework import serializers

from .models import SelectCategory, Services, Booking_s

# from drf_writable_nested.serializers import WritableNestedModelSerializer



class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class SelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectCategory
        fields = '__all__'



class BookingSerivcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking_s
        fields = '__all__'
