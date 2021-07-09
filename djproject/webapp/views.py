from django.shortcuts import render
from rest_framework import viewsets
from .models import client,product
from .serializers import clientSerializer,productSerializer

class clientViewSet(viewsets.ModelViewSet):
    queryset=client.objects.all()
    serializer_class=clientSerializer

class productViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class=productSerializer