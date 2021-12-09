from ofertas.models import Ofertas
from django.shortcuts import render
from rest_framework import generics
from ofertas.serializers import OfertasSerializer

class OfertasList(generics.ListCreateAPIView):
    queryset = Ofertas.objects.all()
    serializer_class = OfertasSerializer

class OfertasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ofertas
    serializer_class = OfertasSerializer

