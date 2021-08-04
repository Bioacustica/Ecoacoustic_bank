from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password

from .models import User


class UserBackend(ModelBackend):
    """Clase encargada de autenticar
    los usuarios que  hagan login

    :param ModelBackend: clase heredada del default backend de Django
    :type ModelBackend: module
    """

    def authenticate(self, email: str = None, password: str = None) -> None:
        """metodo que verifica si los usaurios existen
        en la base de datos

        :param email: email del usuario, defaults to None
        :type email: string, optional
        :param password: constraseña el usuario, defaults to None
        :type password: string, optional
        :return: None
        :rtype: None
        """
        login_valid = settings.ADMIN_LOGIN == email
        pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
        if login_valid and pwd_valid:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = User(email=email)
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return user
        return None
