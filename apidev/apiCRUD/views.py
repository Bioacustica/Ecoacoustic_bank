# librerias necesarias
import json
import coreapi

from rest_framework import response
from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.schemas import AutoSchema
from django.core.serializers import serialize
from .serializers import FundingSerializer
from django.db.models import indexes

from .models import Funding


class ApiCrudSchema(AutoSchema):
    """
    se creó esta clase con el fin de añadir
    campos adicionales en el swagger pues
    no se permitia ingresa la descripción en
    el post, ni en el put

    """
    # TODO documentar
    def get_manual_fields(self, path: str, method: str) -> str:
        extra_fields = []
        if method.lower() in ["post", "put"]:
            extra_fields = [coreapi.Field("description")]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


# Create your views here.

# Añadir datos al funding
# TODO aplicar pep8,documentar con (docstring,sphinx)
class FundingsPG(APIView):
    """
    clase de la entidad Fundings empleada unicamente para
    crear y obtener registros


    :param APIView: Clase basada en las views de Django que nos permite operar
    con los Response, la caracteristica principal es que soporta solicitudes
    de tipo .get() y .post() usados en las apis
    :type APIView: Rest_framework views

    """
    schema = ApiCrudSchema()

    def post(self, request):
        """
        funcion que sirve para hacer un request.post a la base de datos,
        apuntando a la tabla funding en este caso


        :param request: requerimiento, peticion de la funcion
        con el metodo POST
        :type request: HttpRequest

        :return: Retorna un response con los datos del queryset serlializados
        convertidos a Json de forma adicional retorna un HTTP status 201
        :rtype: Json
        """

        # payload = json.loads(request.body)
        # funding = Funding.objects.create(description=payload["description"])
        serializer = FundingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Obtener datos del funding


    def get(self, request):
        """
        funcion que sirve para hacer un request.Get a la base de datos,
        apuntando a la tabla funding en este caso con un id especifico


        :param request: requerimiento, peticion de la funcion con el metodo GET
        :type request: HttpRequest

        :param id_funding: id unico y autoincremental de la tabla fundings en
        la base de datos.
        :type  id_funding: int


        :return: Retorna un response con los datos del queryset serlializados
        convertidos a Json de forma adicional retorna un HTTP status 200
        :rtype: Json
        """
        fundings = Funding.objects.all()
        serializer = FundingSerializer(fundings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Actualizar funding por id_funding


class FundingsPD(APIView):
    """
    clase de la entidad Fundings empleada unicamente para
    actualizar y borrar registros


    :param APIView: Clase basada en las views de Django que nos permite operar
    con los Response, la caracteristica principal es que soporta solicitudes
    de tipo .get() y .post() usados en las apis
    :type APIView: Rest_framework views

    """

    schema = ApiCrudSchema()

    def put(self, request, id_funding):
        """
        funcion que sirve para hacer un request.put a la base de datos,
        apuntando a la tabla funding en este caso.
        Recibe como parametro un diccionario con el id_funding como clave
        y el valor como parametro a reemplazar


        :param request: requerimiento, peticion de la funcion con el metodo PUT
        :type request: HttpRequest

        :param id_funding: id unico y autoincremental de la tabla fundings en
        la base de datos.
        :type  id_funding: int

        :return: Retorna un response con los datos del queryset serlializados
        convertidos a Json de forma adicional retorna un HTTP status 200
        :rtype: Json
        """
        update_funding = Funding.objects.get(id_funding=id_funding)
        serializer = FundingSerializer(update_funding, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Eliminar registro del funding

    def delete(self, request, id_funding):
        """
        funcion que sirve para hacer un request.put a la base de datos,
        apuntando a la tabla funding en este caso.
        Recibe como parametro un diccionario con el id_funding donde eliminará
        la descripcion correspondiente a ese id


        :param request: requerimiento, peticion de la función
        con el metodo DELETE
        :type request: HttpRequest

        :param id_funding: id unico y autoincremental de la tabla fundings en
        la base de datos.
        :type  id_funding: int

        :return:Retorna un response con los datos del queryset serlializados
        convertidos a Json de forma adicional retorna un HTTP status 204
        :rtype: Json
        """
        funding = Funding.objects.get(id_funding=id_funding)
        funding.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, id_funding):
        """
        funcion que sirve para hacer un request.Get a la base de datos,
        apuntando a la tabla funding en este caso


        :param request: requerimiento, peticion de la funcion con el metodo GET
        :type request: HttpRequest

        :param id_funding: id unico y autoincremental de la tabla fundings en
        la base de datos.
        :type  id_funding: int


        :return: Retorna un response con los datos del queryset serlializados
        convertidos a Json de forma adicional retorna un HTTP status 200
        :rtype: Json
        """
        fundings = Funding.objects.filter(id_funding=id_funding)
        serializer = FundingSerializer(fundings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
