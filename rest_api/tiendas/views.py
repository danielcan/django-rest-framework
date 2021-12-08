from tiendas.models import Tiendas
from django.shortcuts import render
from rest_framework import generics
from tiendas.serializers import TiendaSerializer

class TiendaList(generics.ListCreateAPIView):
    queryset = Tiendas.objects.all()
    serializer_class = TiendaSerializer

class TiendaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tiendas
    serializer_class = TiendaSerializer


