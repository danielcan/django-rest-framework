from marcas_api.models import Marcas
from django.shortcuts import render
from rest_framework import generics
from marcas_api.serializers import MarcasSerializer

class MarcasList(generics.ListCreateAPIView):
    queryset = Marcas.objects.all()
    serializer_class = MarcasSerializer

class MarcasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Marcas
    serializer_class = MarcasSerializer