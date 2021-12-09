from favorito.models import Favorito
from django.shortcuts import render
from rest_framework import generics
from favorito.serializers import FavoritoSerializer

class FavoritoList(generics.ListCreateAPIView):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer

class FavoritoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorito
    serializer_class = FavoritoSerializer

