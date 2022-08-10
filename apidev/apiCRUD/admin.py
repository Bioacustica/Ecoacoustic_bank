"""Modulo encargado de mantener el sitio de administrador de django"""

from __future__ import barry_as_FLUFL

__author__ = "Victor Torres"
__version__ = "0.1"
__license__ = "GPL"
__status__ = "Development"
__maintainer__ = "Victor Torres"


from django.contrib import admin
from django.apps import apps


class ListAdminMixin(object):
    """con esta clase podemos
    ver de formas mas intuitiva los objectos
    de la base de datos
    """

    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(ListAdminMixin, self).__init__(model, admin_site)


app_config = apps.get_app_config("django_rest_passwordreset")
models = apps.get_models()
for model in models:
    admin_class = type("AdminClass", (ListAdminMixin, admin.ModelAdmin), {})
    try:
        admin.site.register(model, admin_class)
    except admin.sites.AlreadyRegistered:
        pass
