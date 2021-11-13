"""
Modulo De permisos custom, estos están encargados de dar permisos a los diferentes roles de forma gobal
Es decir pueden o no acceder a la vista, no limita las acciones que se puedan hacer dentro de la vista.
"""
from __future__ import barry_as_FLUFL

__author__ = "Victor Torres"
__version__ = "0.1"
__license__ = "GPL"
__status__ = "Development"
__maintainer__ = "Victor Torres"

from rest_framework.permissions import BasePermission

# clases creadas para proteger las vistas haciendo extendiendo la cclase BasePermissions


class IsAdmin(BasePermission):
    """clase extendida de los permisos basicos de django

    :param BasePermission: clase madre de permisos
    :type BasePermission: class
    """

    def has_permission(self, request, view):
        return request.user.roles == "admin"


class IsUsuario(BasePermission):
    """clase extendida de los permisos basicos de django

    :param BasePermission: clase madre de permisos
    :type BasePermission: class
    """

    def has_permission(self, request, view):
        return request.user.roles == "usuario"


class IsRegistro(BasePermission):
    """clase extendida de los permisos basicos de django

    :param BasePermission: clase madre de permisos
    :type BasePermission: class
    """

    def has_permission(self, request, view):

        return request.user.roles == "registro"


class IsEtiquetado(BasePermission):
    """clase extendida de los permisos basicos de django

    :param BasePermission: clase madre de permisos
    :type BasePermission: class
    """

    def has_permission(self, request, view):
        return request.user.roles == "Etiquetado"
