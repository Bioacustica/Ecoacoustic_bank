"""
    Sirve para crear automaticamente un usuario y contraseña para django admin
"""

from __future__ import barry_as_FLUFL

__author__ = "Victor Torres"
__version__ = "0.1"
__license__ = "GPL"
__status__ = "Development"
__maintainer__ = "Victor Torres"


from django.contrib.auth import get_user_model

User = get_user_model()
User.objects.filter(username="admin").exists() or User.objects.create_superuser(
    "admin@admin.com", "admin", "pass"
)
