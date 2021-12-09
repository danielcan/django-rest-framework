from rest_framework.serializers import ModelSerializer
from marcas_api.models import Marcas


class MarcasSerializer(ModelSerializer):
    class Meta:
        model = Marcas
        fields = ['id', 'name', 'logo']