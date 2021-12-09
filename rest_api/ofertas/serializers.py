from rest_framework.serializers import ModelSerializer
from ofertas.models import Ofertas


class OfertasSerializer(ModelSerializer):
    class Meta:
        model = Ofertas
        fields = ['id', 'name', 'store', 'image', 'price']