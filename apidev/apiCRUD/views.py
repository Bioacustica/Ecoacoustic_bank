# librerias necesarias
import json
import coreapi
import logging
from django.http import request

import psycopg2
from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.decorators import authentication_classes
from rest_framework import permissions
from rest_framework import response, decorators, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Funding
from .serializers import MyTokenObtainPairSerializer
from .fnt import choose_role
from .serializers import *

# Vistas hechas con el model view set para hacer el CRUD
"""La Clase ModelViewSet incluye implementaciones para
hacer varias acciones como .list() , .create() , .update() , etc
de forma automatica sin necesidad de crear las funciones, esta
clase es muy util para un paronama general que no requiere personalización

"""
User = get_user_model()
logger = logging.getLogger(__name__)


class MyObtainTokenView(TokenObtainPairView):
    """clase encargada de login con  Users de la DB"""

    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


#  Función  encargada de registrar usuarios
@decorators.api_view(["POST"])
#@decorators.permission_classes([permissions.IsAdminUser])
@permission_classes([IsAuthenticated])
def registration(request):
    """
    Esta clase es la encargada de registrar usuarios nuevos
    unicamente se puede registrar usuarios

    :return: si todo fue exitoso devuelve un creado de forma exitosa
    :rtype: Http status
    """
    
    print(request.data)
    print(len(request.data))
    username = request.data["username"]
    email = request.data["email"]
    password = request.data["password"]
    roles = request.data["roles"]

    credenciales_db = {
        "user": "admin2",
        "password": "pass4",
        "host": "postgres",
        "port": 5432,
        "database": "animalesitm",
    }
    
    conexion = psycopg2.connect(**credenciales_db)
    conexion.autocommit = True
    payload = choose_role(username, password, roles)
    with conexion.cursor() as cursor:
        cursor.execute(payload)
        
        bioacustica = cursor.fetchall()

    serializer = UserCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return response.Response("ok", status=status.HTTP_201_CREATED)
    else:
        return response.Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
class FundingsView(viewsets.ModelViewSet):
    # def my_view(self,request):
    #     username = None
    #     if request.user.is_authenticated():
    #         username = request.user.username
    #     return username
    # logger.debug("The user {} has made modifications in Fundigs ".format(my_view()))
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


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User

    def get_object(self, queryset=None):
        """obtiene el objeto de usuario

        :param queryset: , defaults to None
        :type queryset: queryset, optional
        :return: retorna el objeto usuario
        :rtype: AsbtractBaseUser
        """
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        """con este metodo hacemos directamente la
        actualización de la contraseña

        :param request: recibe los parametros del usuario para 
        hacer la actualuzación
        :type request: json
        :return:  retorna la actualización de la constraseña
        :rtype: response
        """
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
