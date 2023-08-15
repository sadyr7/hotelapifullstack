from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import generics, ModelViewSet
from rest_framework import permissions
from hotel.models import Hotel, Booking, Comment
from hotel.serializers import (

    HotelSerializer,
    BookingWriteSerializer,
    BookingReadSerializer,
    CommentSerializer,
)

from rest_framework.permissions import IsAdminUser

# class RoomViewSet(ModelViewSet):
#     queryset = Room.objects.all
#     serializer_class = RoomWriteSerializer

 
class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAdminUser]

    # parser_classes = (MultiPartParser,)


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.order_by('pk')
    write_serializer_class = BookingWriteSerializer
    read_serializer_class = BookingReadSerializer
    def get_serializer_class(self):
        serializer_action_mapping = {
            'create': self.write_serializer_class,
            'update': self.write_serializer_class,
            'partial_update': self.write_serializer_class,

        }

        return serializer_action_mapping.get(
            self.action,
            self.read_serializer_class
        )

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)



class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return permissions.AllowAny(),
        return permissions.IsAuthenticated(),