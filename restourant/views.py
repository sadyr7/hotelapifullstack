from django.shortcuts import render
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import generics
from rest_framework.viewsets import ModelViewSet
from restourant.models import Category_restourant, Product, Like
from .serializers import ProductSerializers, CategorySerializers, LikeSerializer
from rest_framework.pagination import PageNumberPagination

class CategoryViewSet(ModelViewSet):
    queryset = Category_restourant.objects.all()
    serializer_class = CategorySerializers

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    parser_classes = (MultiPartParser,)

class StandartResultPagination (PageNumberPagination):
    page_size = 3
    page_query_param = 'page'


class LikeCreateView(ModelViewSet):
    queryset = Like.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikeDeleteView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'