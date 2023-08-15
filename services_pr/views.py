from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser

from .serializers import ServicesSerializer, \
     SelectSerializer, BookingSerivcesSerializer

from .models import Services, SelectCategory, Booking_s
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [IsAuthenticated]

    # parser_classes = (MultiPartParser,)


class SelectViewSet(viewsets.ModelViewSet):
    queryset = SelectCategory.objects.all()
    serializer_class = SelectSerializer
    # permission_classes = [IsAuthenticated]


class BookingUnderServicesViewSet(viewsets.ModelViewSet):
    queryset = Booking_s.objects.all()
    serializer_class = BookingSerivcesSerializer