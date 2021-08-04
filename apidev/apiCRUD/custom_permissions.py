from rest_framework.permissions import BasePermission
from rest_framework import permissions

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
