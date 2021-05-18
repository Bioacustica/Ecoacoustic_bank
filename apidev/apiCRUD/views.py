# librerias necesarias
from .serializers import FundingSerializer
from django.db.models import indexes
import json
from rest_framework import status
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import Funding
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
# Create your views here.

# Añadir datos al funding
# TODO aplicar pep8,documentar con (docstring,sphinx)


# decorador de vista de la api el cual toma alguno de los metodos HTTP
@api_view(['POST'])
def create_funding(request):
    """
    funcion que sirve para hacer un request.post a la base de datos,
    apuntando a la tabla funding en este caso


    :param request: requerimiento, peticion de la funcion con el metodo POST
    :type request: HttpRequest

    :return: Retorna un Json response con los datos del queryset
    convertidos a Json de forma adicional retorna un HTTP status 201
    :rtype: Json
    """
    payload = json.loads(request.body)
    # description = Funding.objects.get(description=payload["description"])
    funding = Funding.objects.create(description=payload["description"])
    serializer = FundingSerializer(funding)
    return JsonResponse({'funding': serializer.data}, safe=False,
                        status=status.HTTP_201_CREATED)
# Obtener datos del funding


@api_view(["GET"])
def get_funding(request):
    """
    funcion que sirve para hacer un request.Get a la base de datos,
    apuntando a la tabla funding en este caso


    :param request: requerimiento, peticion de la funcion con el metodo GET
    :type request: HttpRequest

    :return: Retorna un Json response con los datos del queryset
    convertidos a Json de forma adicional retorna un HTTP status 200
    :rtype: Json
    """
    fundings = Funding.objects.all()
    serializer = FundingSerializer(fundings, many=True)
    return JsonResponse({'Fundings': serializer.data},
                        safe=False, status=status.HTTP_200_OK)
# Actualizar funding por id_funding


@api_view(["PUT"])
def update_funding(request, id_funding):
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

    :return: Retorna un Json response con los datos del queryset
    convertidos a Json de forma adicional retorna un HTTP status 200
    :rtype: Json
    """
    payload = json.loads(request.body)
    item_funding = Funding.objects.filter(id_funding=id_funding)
    # returns 1 or 0 if the query macth  the id
    item_funding.update(**payload)
    update_funding = Funding.objects.get(id_funding=id_funding)
    serializer = FundingSerializer(update_funding)
    return JsonResponse({'funding': serializer.data},
                        safe=False, status=status.HTTP_200_OK)
# Eliminar registro del funding


@api_view(["DELETE"])
def delete_funding(request, id_funding):
    """
    funcion que sirve para hacer un request.put a la base de datos,
    apuntando a la tabla funding en este caso.
    Recibe como parametro un diccionario con el id_funding donde eliminará
    la descripcion correspondiente a ese id


    :param request: requerimiento, peticion de la funcion con el metodo DELETE
    :type request: HttpRequest

    :param id_funding: id unico y autoincremental de la tabla fundings en
    la base de datos.
    :type  id_funding: int

    :return: Retorna un Json response con los datos del queryset
    convertidos a Json de forma adicional retorna un HTTP status 204
    :rtype: Json
    """
    funding = Funding.objects.get(id_funding=id_funding)
    funding.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
