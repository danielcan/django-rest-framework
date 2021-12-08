from rest_framework.serializers import ModelSerializer
from favorito.models import Favorito


class FavoritoSerializer(ModelSerializer):
    class Meta:
        model = Favorito
        fields = ['id', 'usuario', 'tienda']