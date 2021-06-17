# librerias necesarias
import json
import coreapi
import logging


from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import permission_classes
from rest_framework.decorators import authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Funding
from .serializers import MyTokenObtainPairSerializer

# Vistas hechas con el model view set para hacer el CRUD
"""La Clase ModelViewSet incluye implementaciones para
hacer varias acciones como .list() , .create() , .update() , etc
de forma automatica sin necesidad de crear las funciones, esta
clase es muy util para un paronama general que no requiere personalización

"""
logger = logging.getLogger(__name__)


class MyObtainTokenView(TokenObtainPairView):
    """ clase encargada de login con el Default Users de Django
    """
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
class FundingsView(viewsets.ModelViewSet):
    name = User.objects.get_queryset()
    logger.debug('The user {} has made modifications in Fundigs '.format(name))
    queryset = Funding.objects.all()
    serializer_class = FundingSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
class CaseView(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
class CatalogueView(viewsets.ModelViewSet):
    queryset = Catalogue.objects.all()
    serializer_class = CatalogueSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
class CatalogueObsView(viewsets.ModelViewSet):
    queryset = CatalogueObs.objects.all()
    serializer_class = CatalogueObsSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
class DatumView(viewsets.ModelViewSet):
    queryset = Datum.objects.all()
    serializer_class = DatumSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
class EvidenceView(viewsets.ModelViewSet):
    queryset = Evidence.objects.all()
    serializer_class = EvidenceSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
class FormatView(viewsets.ModelViewSet):
    queryset = Format.objects.all()
    serializer_class = FormatSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
class HSerialView(viewsets.ModelViewSet):
    queryset = HSerial.objects.all()
    serializer_class = HSerialSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
class HabitatView(viewsets.ModelViewSet):
    queryset = Habitat.objects.all()
    serializer_class = HabitatSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
class HardwareView(viewsets.ModelViewSet):
    queryset = Hardware.objects.all()
    serializer_class = HardwareSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
class LabelView(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
class LabeledView(viewsets.ModelViewSet):
    queryset = Labeled.objects.all()
    serializer_class = LabeledSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
class MemoryView(viewsets.ModelViewSet):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
class PhotoPathView(viewsets.ModelViewSet):
    queryset = PhotoPath.objects.all()
    serializer_class = PhotoPathSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
class PrecisionView(viewsets.ModelViewSet):
    queryset = Precision.objects.all()
    serializer_class = PrecisionSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
class RecordView(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
class RecordObsView(viewsets.ModelViewSet):
    queryset = RecordObs.objects.all()
    serializer_class = RecordObsSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
class RecordPathView(viewsets.ModelViewSet):
    queryset = RecordPath.objects.all()
    serializer_class = RecordPathSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
class SamplingView(viewsets.ModelViewSet):
    queryset = Sampling.objects.all()
    serializer_class = SamplingSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
class SeasonView(viewsets.ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
class SupplyView(viewsets.ModelViewSet):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
class TypeView(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
