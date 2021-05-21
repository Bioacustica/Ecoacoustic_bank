# librarys
from rest_framework import serializers
from .models import Funding


class FundingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funding
        fields = ["id_funding", "description"]
