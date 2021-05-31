# librerias necesarias
import json
import coreapi

from rest_framework import response
from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.schemas import AutoSchema
from django.core.serializers import serialize
from .serializers import *
from django.db.models import indexes

from .models import Funding


# Vistas hechas con el model view set para hacer el CRUD
"""La Clase ModelViewSet incluye implementaciones para
hacer varias acciones como .list() , .create() , .update() , etc
de forma automatica sin necesidad de crear las funciones, esta
clase es muy util para un paronama general que no requiere personalización

"""


class FundingsView(viewsets.ModelViewSet):
    queryset = Funding.objects.all()
    serializer_class = FundingSerializer


class CaseView(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer


class CatalogueView(viewsets.ModelViewSet):
    queryset = Catalogue.objects.all()
    serializer_class = CatalogueSerializer


class CatalogueObsView(viewsets.ModelViewSet):
    queryset = CatalogueObs.objects.all()
    serializer_class = CatalogueObsSerializer


class DatumView(viewsets.ModelViewSet):
    queryset = Datum.objects.all()
    serializer_class = DatumSerializer


class EvidenceView(viewsets.ModelViewSet):
    queryset = Evidence.objects.all()
    serializer_class = EvidenceSerializer


class FormatView(viewsets.ModelViewSet):
    queryset = Format.objects.all()
    serializer_class = FormatSerializer


class HSerialView(viewsets.ModelViewSet):
    queryset = HSerial.objects.all()
    serializer_class = HSerialSerializer


class HabitatView(viewsets.ModelViewSet):
    queryset = Habitat.objects.all()
    serializer_class = HabitatSerializer


class HardwareView(viewsets.ModelViewSet):
    queryset = Hardware.objects.all()
    serializer_class = HardwareSerializer


class LabelView(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class LabeledView(viewsets.ModelViewSet):
    queryset = Labeled.objects.all()
    serializer_class = LabeledSerializer


class MemoryView(viewsets.ModelViewSet):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer


class PhotoPathView(viewsets.ModelViewSet):
    queryset = PhotoPath.objects.all()
    serializer_class = PhotoPathSerializer


class PrecisionView(viewsets.ModelViewSet):
    queryset = Precision.objects.all()
    serializer_class = PrecisionSerializer


class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class RecordView(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class RecordObsView(viewsets.ModelViewSet):
    queryset = RecordObs.objects.all()
    serializer_class = RecordObsSerializer


class RecordPathView(viewsets.ModelViewSet):
    queryset = RecordPath.objects.all()
    serializer_class = RecordPathSerializer


class SamplingView(viewsets.ModelViewSet):
    queryset = Sampling.objects.all()
    serializer_class = SamplingSerializer


class SeasonView(viewsets.ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer


class SupplyView(viewsets.ModelViewSet):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer


class TypeView(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
