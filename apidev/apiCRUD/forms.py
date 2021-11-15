"""
Modulo encargado de los formularios para las vistas
"""
from __future__ import barry_as_FLUFL

__author__ = "Victor Torres"
__version__ = "0.1"
__license__ = "GPL"
__status__ = "Development"
__maintainer__ = "Victor Torres"

from django import forms


class ContactForm(forms.Form):
    """
    Clase encargada de generar un formulario
    de contacto.
    """
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
