# librarys
from rest_framework import serializers
from .models import Funding


class FundingSerializer(serializers.ModelSerializer):
    """Clase encargada de convertir querysets a forma nativa
    para trabajarla en formato json

    """
    class Meta:
        model = Funding
        fields = ["id_funding", "description"]
