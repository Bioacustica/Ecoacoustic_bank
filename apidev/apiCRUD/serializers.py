# librarys
from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import permissions, serializers
from rest_framework.views import APIView
from .models import *
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.conf import settings


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Clase encargada del login del Usuario
    :param TokenObtainPairSerializer: Clase encargada de obtener
    el access token y el refresh token
    """
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ["email", "password"]

"""Clases encargadas de convertir querysets a forma nativa
    para trabajarla en formato json"""


class FundingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funding
        fields = "__all__"


class CaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Case
        fields = "__all__"


class CatalogueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Catalogue
        fields = "__all__"


class CatalogueObsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CatalogueObs
        fields = "__all__"


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class DatumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Datum
        fields = "__all__"


class MicrophoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Microphone
        fields = "__all__"


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class EvidenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evidence
        fields = "__all__"


class FrequencyDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FrequencyDetail
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



class LocalitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Locality
        fields = "__all__"


class GainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gain
        fields = "__all__"


class FilterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Filter
        fields = "__all__"


class MeasureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Measure
        fields = "__all__"


class MemorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Memory
        fields = "__all__"


class MunicipalitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Municipality
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


class PulseTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PulseType
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


class SoftwareSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Software
        fields = "__all__"


class SupplySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supply
        fields = "__all__"


class TimeDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TimeDetail
        fields = "__all__"


class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"


class VeredaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vereda
        fields = "__all__"


class VoucherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Voucher
        fields = "__all__"


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "roles", "id_user"]


class UserCreateSerializer(serializers.HyperlinkedModelSerializer):
    """[summary]
    :param serializers: [description]
    :type serializers: [type]
    :raises serializers.ValidationError: [description]
    :return: [description]
    :rtype: [type]
    """

    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):

        username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]
        roles = validated_data["roles"]
        is_admin = validated_data["is_admin"]

        if (
            email
            and User.objects.filter(email=email).exclude(username=username).exists()
        ):
            raise serializers.ValidationError(
                {"email": "Email addresses must be unique."}
            )
        user = User(username=username, email=email, roles=roles, is_admin=is_admin)
        user.set_password(password)
        user.save()
        return user


class ChangePasswordSerializer(serializers.Serializer):
    model = User
    """
    Serializer for password change endpoint.
    """
    username = serializers.CharField(required=True)
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)