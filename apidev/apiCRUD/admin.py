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


models = apps.get_models()
for model in models:
    admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
    try:
        admin.site.register(model, admin_class)
    except admin.sites.AlreadyRegistered:
        pass
