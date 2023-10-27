from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from app.models import ApiUser, Warehouse, Product
from app.serializer import UserSerializer, WarehouseSerializer, ProductSerializer


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    http_method_names = ['post', 'get']
    serializer_class = UserSerializer

    authentication_classes = []
    permission_classes = []


class WarehouseModelViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

# Продукты
class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True)
    def warehouse(self, request, pk=None):
        warehouse = get_object_or_404(Warehouse.objects.all(), id=pk)
        return Response(
            ProductSerializer(warehouse, many=True).data
        )
