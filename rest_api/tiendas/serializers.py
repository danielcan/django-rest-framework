from rest_framework.serializers import ModelSerializer
from tiendas.models import Tiendas


class TiendaSerializer(ModelSerializer):
    class Meta:
        model = Tiendas
        fields = ['id', 'brand', 'identifier', 'name', 'address']