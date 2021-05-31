# librarys
from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import *


class FundingSerializer(serializers.HyperlinkedModelSerializer):
    """Clase encargada de convertir querysets a forma nativa
    para trabajarla en formato json

    """

    class Meta:
        model = Funding
        fields = "__all__"


class CaseSerializer(serializers.HyperlinkedModelSerializer):
    """[summary]

    Args:
        serializers ([type]): [description]
    """

    class Meta:
        model = Case
        fields = "__all__"


class CatalogueSerializer(serializers.HyperlinkedModelSerializer):
    """[summary]

    Args:
        serializers ([type]): [description]
    """

    class Meta:
        model = Catalogue
        fields = "__all__"


class CatalogueObsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CatalogueObs
        fields = "__all__"


class DatumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Datum
        fields = "__all__"


class EvidenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evidence
        fields = "__all__"


class FormatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Format
        fields = "__all__"


class HSerialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HSerial
        fields = "__all__"


class HabitatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Habitat
        fields = "__all__"


class HardwareSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hardware
        fields = "__all__"


class LabelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Label
        fields = "__all__"


class LabeledSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Labeled
        fields = "__all__"


class MemorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Memory
        fields = "__all__"


class PhotoPathSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PhotoPath
        fields = "__all__"


class PrecisionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Precision
        fields = "__all__"


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = "__all__"


class RecordObsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RecordObs
        fields = "__all__"


class RecordPathSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RecordPath
        fields = "__all__"


class SamplingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sampling
        fields = "__all__"


class SeasonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Season
        fields = "__all__"


class SupplySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supply
        fields = "__all__"


class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
