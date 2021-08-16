# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the
# desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create
# , modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field
# names.
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from simple_history.models import HistoricalRecords


@receiver(reset_password_token_created)
def password_reset_token_created(
    sender, instance, reset_password_token, *args, **kwargs
):
    """CLase encargada de resetear la contraseña del usuario
    :param sender: Sender provides a simple interface to set up SMTP and send email messages
    :type sender: vista basada en clases que envia la señal
    :param instance: Vista que instancia la señal
    :param reset_password_token: objecto token
    :type reset_password_token: token
    """

    email_plaintext_message = "{}?token={}".format(
        reverse("password_reset:reset-password-request"), reset_password_token.key
    )

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email],
    )


class UserManager(BaseUserManager):
    """Esta clase se encarga de
    manejar el modelo User de la base de datos
    :param BaseUserManager:  heredamos de la clase BaseUserManager
    la cual funciona con el default user de Django
    en este caso estamos extiendiendo  la clase para hacer
    la nuestra
    """

    def create_user(self, email, username, password=None, roles=None):
        if not email:
            raise ValueError("Email is required")
        if not username:
            raise ValueError("Name is required")

        user = self.model(
            email=self.normalize_email(email), username=username, roles=roles
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )

        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, roles="admin"):
        user = self.create_user(
            email=email, username=username, password=password, roles=roles
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    ROLES = (
        ("admin", "admin"),
        ("usuario", "usuario"),
        ("etiquetado", "etiquetado"),
        ("registro", "registro"),
    )
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True, unique=True)
    last_login = models.DateField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    roles = models.CharField(max_length=50, choices=ROLES, null=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    objects = UserManager()

    class Meta:
        managed = False
        db_table = "user"


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = "auth_group"


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey("AuthPermission", models.DO_NOTHING)

    def __str__(self):
        return self.group

    class Meta:
        managed = False
        db_table = "auth_group_permissions"
        unique_together = (("group", "permission"),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey("DjangoContentType", models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = "auth_permission"
        unique_together = (("content_type", "codename"),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "auth_user"


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_groups"
        unique_together = (("user", "group"),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_user_permissions"
        unique_together = (("user", "permission"),)


class Case(models.Model):
    id_case = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = "case"


class Catalogue(models.Model):
    id_catalogue = models.AutoField(primary_key=True)
    id_sampling = models.ForeignKey(
        "Sampling", models.DO_NOTHING, db_column="id_sampling"
    )
    id_country = models.ForeignKey("Country", models.DO_NOTHING, db_column="id_country")
    id_department = models.ForeignKey(
        "Department", models.DO_NOTHING, db_column="id_department"
    )
    id_municipality = models.ForeignKey(
        "Municipality", models.DO_NOTHING, db_column="id_municipality"
    )
    id_vereda = models.ForeignKey("Vereda", models.DO_NOTHING, db_column="id_vereda")
    id_locality = models.ForeignKey(
        "Locality", models.DO_NOTHING, db_column="id_locality"
    )
    id_gain = models.IntegerField()
    id_filters = models.IntegerField()
    id_collector = models.ForeignKey(
        "User", models.DO_NOTHING, db_column="id_collector"
    )
    id_h_serial = models.ForeignKey(
        "HSerial", models.DO_NOTHING, db_column="id_h_serial"
    )
    id_supply = models.ForeignKey("Supply", models.DO_NOTHING, db_column="id_supply")
    id_case = models.ForeignKey(Case, models.DO_NOTHING, db_column="id_case")
    id_memory = models.ForeignKey("Memory", models.DO_NOTHING, db_column="id_memory")
    id_habitat = models.ForeignKey("Habitat", models.DO_NOTHING, db_column="id_habitat")
    id_precision = models.ForeignKey(
        "Precision", models.DO_NOTHING, db_column="id_precision"
    )
    id_datum = models.ForeignKey("Datum", models.DO_NOTHING, db_column="id_datum")
    elevation = models.IntegerField(blank=True, null=True)
    coordinates = models.TextField(blank=True, null=True)  # This field type is a guess.
    height = models.IntegerField(blank=True, null=True)
    chunks = models.SmallIntegerField(blank=True, null=True)
    size = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "catalogue"

    def __str__(self):
        return self.elevation

    @staticmethod
    def has_read_permission(request):
        """función encargada de permitir
        o denegar si un usuario con su rol
        puede hacer cambios en la bd
        """
        if (
            request.user.roles == "registro"
            or request.user.roles == "admin"
            or request.user.roles == "etiquetado"
        ):
            return True
        return False

    def has_object_read_permission(self, request):
        """función encargada de permitir
        o denegar si un usuario con su rol
        puede hacer cambios en la bd
        """
        if (
            request.user.roles == "registro"
            or request.user.roles == "admin"
            or request.user.roles == "etiquetado"
        ):
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    def has_object_write_permission(self, request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_destroy_permission(request):
        if request.user.roles == "admin":
            return True
        return False


    def has_object_destroy_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False


class CatalogueObs(models.Model):
    id_catalogue_obs = models.AutoField(primary_key=True)
    id_catalogue = models.ForeignKey(
        Catalogue, models.DO_NOTHING, db_column="id_catalogue"
    )
    observation = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.id_catalogue

    class Meta:
        managed = False
        db_table = "catalogue_obs"


class Country(models.Model):
    id_country = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "country"

    @staticmethod
    def has_read_permission(request):
        """función encargada de permitir
        o denegar si un usuario con su rol
        puede hacer cambios en la bd
        """
        if (
                request.user.roles == "registro"
                or request.user.roles == "admin"
                or request.user.roles == "etiquetado"
        ):
            return True
        return False

    def has_object_read_permission(self, request):
        """función encargada de permitir
        o denegar si un usuario con su rol
        puede hacer cambios en la bd
        """
        if (
                request.user.roles == "registro"
                or request.user.roles == "admin"
                or request.user.roles == "etiquetado"
        ):
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    def has_object_write_permission(self, request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_destroy_permission(request):
        if request.user.roles == "admin":
            return True
        return False

    def has_object_destroy_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False


class Datum(models.Model):
    id_datum = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = "datum"


class Department(models.Model):
    id_department = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "department"

    @staticmethod
    def has_read_permission(request):
        """función encargada de permitir
        o denegar si un usuario con su rol
        puede hacer cambios en la bd
        """
        if (
                request.user.roles == "registro"
                or request.user.roles == "admin"
                or request.user.roles == "etiquetado"
        ):
            return True
        return False

    def has_object_read_permission(self, request):
        """función encargada de permitir
        o denegar si un usuario con su rol
        puede hacer cambios en la bd
        """
        if (
                request.user.roles == "registro"
                or request.user.roles == "admin"
                or request.user.roles == "etiquetado"
        ):
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    def has_object_write_permission(self, request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_destroy_permission(request):
        if request.user.roles == "admin":
            return True
        return False

    def has_object_destroy_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        "DjangoContentType", models.DO_NOTHING, blank=True, null=True
    )
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "django_admin_log"


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "django_content_type"
        unique_together = (("app_label", "model"),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_migrations"


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_session"


class Evidence(models.Model):
    id_evidence = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = "evidence"

    @staticmethod
    def has_read_permission(request):
        """función encargada de permitir
        o denegar si un usuario con su rol
        puede hacer cambios en la bd
        """
        if (
                request.user.roles == "registro"
                or request.user.roles == "admin"
                or request.user.roles == "etiquetado"
        ):
            return True
        return False

    def has_object_read_permission(self, request):
        """función encargada de permitir
        o denegar si un usuario con su rol
        puede hacer cambios en la bd
        """
        if (
                request.user.roles == "registro"
                or request.user.roles == "admin"
                or request.user.roles == "etiquetado"
        ):
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    def has_object_write_permission(self, request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_destroy_permission(request):
        if request.user.roles == "admin":
            return True
        return False

    def has_object_destroy_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False


class Format(models.Model):
    id_format = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = "format"

    @staticmethod
    def has_read_permission(request):
        if (
            request.user.roles == "registro"
            or request.user.roles == "admin"
            or request.user.roles == "etiquetado"
            or request.user.roles == "usuario"
        ):
            return True
        return False

    def has_object_read_permission(self, request):
        if (
            request.user.roles == "registro"
            or request.user.roles == "admin"
            or request.user.roles == "etiquetado"
            or request.user.roles == "usuario"
        ):
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    def has_object_write_permission(self, request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_destroy_permission(request):
        if request.user.roles == "admin":
            return True
        return False


    def has_object_destroy_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False


class FrequencyDetail(models.Model):
    id_frequency_detail = models.AutoField(primary_key=True)
    id_labeled = models.IntegerField()
    beginning = models.IntegerField(blank=True, null=True)
    ending = models.IntegerField(blank=True, null=True)
    minimal = models.IntegerField(blank=True, null=True)
    maximum = models.IntegerField(blank=True, null=True)
    peak = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.peak

    class Meta:
        managed = False
        db_table = "frequency_detail"

    @staticmethod
    def has_read_permission(request):
        """función encargada de permitir
        o denegar si un usuario con su rol
        puede hacer cambios en la bd
        """
        if (
                request.user.roles == "registro"
                or request.user.roles == "admin"
                or request.user.roles == "etiquetado"
        ):
            return True
        return False

    def has_object_read_permission(self, request):
        """función encargada de permitir
        o denegar si un usuario con su rol
        puede hacer cambios en la bd
        """
        if (
                request.user.roles == "registro"
                or request.user.roles == "admin"
                or request.user.roles == "etiquetado"
        ):
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    def has_object_write_permission(self, request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_destroy_permission(request):
        if request.user.roles == "admin":
            return True
        return False

    def has_object_destroy_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False

      
class Funding(models.Model):
    id_funding = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = "funding"



class HSerial(models.Model):
    id_h_serial = models.AutoField(primary_key=True)
    id_hardware = models.ForeignKey(
        "Hardware", models.DO_NOTHING, db_column="id_hardware"
    )
    h_serial = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.id_h_serial

    class Meta:
        managed = False
        db_table = "h_serial"

    @staticmethod
    def has_read_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    def has_object_read_permission(self, request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    def has_object_write_permission(self, request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_destroy_permission(request):
        if request.user.roles == "admin":
            return True
        return False


    def has_object_destroy_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False


class Habitat(models.Model):
    id_habitat = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = "habitat"

    @staticmethod
    def has_read_permission(request):
        if (
            request.user.roles == "registro"
            or request.user.roles == "admin"
            or request.user.roles == "etiquetado"
            or request.user.roles == "usuario"
        ):
            return True
        return False

    def has_object_read_permission(self, request):
        if (
            request.user.roles == "registro"
            or request.user.roles == "admin"
            or request.user.roles == "etiquetado"
            or request.user.roles == "usuario"
        ):
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    def has_object_write_permission(self, request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_destroy_permission(request):
        if request.user.roles == "admin":
            return True
        return False


    def has_object_destroy_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False


class Hardware(models.Model):
    id_hardware = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = "hardware"

    @staticmethod
    def has_read_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    def has_object_read_permission(self, request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    def has_object_write_permission(self, request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_destroy_permission(request):
        if request.user.roles == "admin":
            return True
        return False


    def has_object_destroy_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False


class Label(models.Model):
    id_label = models.AutoField(primary_key=True)
    id_type = models.ForeignKey("Type", models.DO_NOTHING, db_column="id_type")

    def __str__(self):
        return self.id_label

    @staticmethod
    def has_read_permission(request):
        if (
            request.user.roles == "registro"
            or request.user.roles == "admin"
            or request.user.roles == "etiquetado"
            or request.user.roles == "usuario"
        ):
            return True
        return False

    def has_object_read_permission(self, request):
        if (
            request.user.roles == "registro"
            or request.user.roles == "admin"
            or request.user.roles == "etiquetado"
            or request.user.roles == "usuario"
        ):
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if (
            request.user.roles == "registro"
            or request.user.roles == "admin"
            or request.user.roles == "etiquetado"
        ):
            return True
        return False

    def has_object_write_permission(self, request):
        if (
            request.user.roles == "registro"
            or request.user.roles == "admin"
            or request.user.roles == "etiquetado"
        ):
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if (
            request.user.roles == "registro"
            or request.user.roles == "admin"
            or request.user.roles == "etiquetado"
        ):
            return True
        return False

    @staticmethod
    def has_destroy_permission(request):
        if request.user.roles == "admin":
            return True
        return False


    def has_object_destroy_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False

    class Meta:
        managed = False
        db_table = "label"


class Labeled(models.Model):
    id_labeled = models.AutoField(primary_key=True)
    id_label = models.ForeignKey(Label, models.DO_NOTHING, db_column="id_label")
    id_record = models.ForeignKey("Record", models.DO_NOTHING, db_column="id_record")
    id_evidence = models.ForeignKey(
        Evidence, models.DO_NOTHING, db_column="id_evidence"
    )
    id_labeler = models.ForeignKey("User", models.DO_NOTHING, db_column="id_labeler")
    begin = models.IntegerField(blank=True, null=True)
    label_end = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.begin

    class Meta:
        managed = False
        db_table = "labeled"

    @staticmethod
    def has_read_permission(request):
        if (
            request.user.roles == "registro"
            or request.user.roles == "admin"
            or request.user.roles == "etiquetado"
            or request.user.roles == "usuario"
        ):
            return True
        return False

    def has_object_read_permission(self, request):
        if (
            request.user.roles == "registro"
            or request.user.roles == "admin"
            or request.user.roles == "etiquetado"
            or request.user.roles == "usuario"
        ):
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if (
            request.user.roles == "registro"
            or request.user.roles == "admin"
            or request.user.roles == "etiquetado"
        ):
            return True
        return False

    def has_object_write_permission(self, request):
        if (
            request.user.roles == "registro"
            or request.user.roles == "admin"
            or request.user.roles == "etiquetado"
        ):
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if (
            request.user.roles == "registro"
            or request.user.roles == "admin"
            or request.user.roles == "etiquetado"
        ):
            return True
        return False

    @staticmethod
    def has_destroy_permission(request):
        if request.user.roles == "admin":
            return True
        return False


    def has_object_destroy_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False


class Locality(models.Model):
    id_locality = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = "locality"


    @staticmethod
    def has_read_permission(request):
        """función encargada de permitir
        o denegar si un usuario con su rol
        puede hacer cambios en la bd
        """
        if (
                request.user.roles == "registro"
                or request.user.roles == "admin"
                or request.user.roles == "etiquetado"
        ):
            return True
        return False

    def has_object_read_permission(self, request):
        """función encargada de permitir
        o denegar si un usuario con su rol
        puede hacer cambios en la bd
        """
        if (
                request.user.roles == "registro"
                or request.user.roles == "admin"
                or request.user.roles == "etiquetado"
        ):
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    def has_object_write_permission(self, request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_destroy_permission(request):
        if request.user.roles == "admin":
            return True
        return False

    def has_object_destroy_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False


class Measure(models.Model):
    id_measure = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = "measure"

    @staticmethod
    def has_read_permission(request):
        """función encargada de permitir
        o denegar si un usuario con su rol
        puede hacer cambios en la bd
        """
        if (
                request.user.roles == "registro"
                or request.user.roles == "admin"
                or request.user.roles == "etiquetado"
        ):
            return True
        return False

    def has_object_read_permission(self, request):
        """función encargada de permitir
        o denegar si un usuario con su rol
        puede hacer cambios en la bd
        """
        if (
                request.user.roles == "registro"
                or request.user.roles == "admin"
                or request.user.roles == "etiquetado"
        ):
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    def has_object_write_permission(self, request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_destroy_permission(request):
        if request.user.roles == "admin":
            return True
        return False

    def has_object_destroy_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False


class Memory(models.Model):
    id_memory = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = "memory"

    @staticmethod
    def has_read_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    def has_object_read_permission(self, request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    def has_object_write_permission(self, request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_destroy_permission(request):
        if request.user.roles == "admin":
            return True
        return False

    def has_object_destroy_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False


class Municipality(models.Model):
    id_municipality = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "municipality"

    @staticmethod
    def has_read_permission(request):
        """función encargada de permitir
        o denegar si un usuario con su rol
        puede hacer cambios en la bd
        """
        if (
                request.user.roles == "registro"
                or request.user.roles == "admin"
                or request.user.roles == "etiquetado"
        ):
            return True
        return False

    def has_object_read_permission(self, request):
        """función encargada de permitir
        o denegar si un usuario con su rol
        puede hacer cambios en la bd
        """
        if (
                request.user.roles == "registro"
                or request.user.roles == "admin"
                or request.user.roles == "etiquetado"
        ):
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    def has_object_write_permission(self, request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_destroy_permission(request):
        if request.user.roles == "admin":
            return True
        return False


    def has_object_destroy_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False


class Municipality(models.Model):
    id_municipality = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "municipality"


class PhotoPath(models.Model):
    id_photo_path = models.AutoField(primary_key=True)
    id_catalogue = models.OneToOneField(
        Catalogue, models.DO_NOTHING, db_column="id_catalogue"
    )
    path = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.id_catalogue

    class Meta:
        managed = False
        db_table = "photo_path"


class Precision(models.Model):
    id_precision = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = "precision"

    @staticmethod
    def has_read_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    def has_object_read_permission(self, request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    def has_object_write_permission(self, request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_delete_permission(request):
        if request.user.roles == "admin":
            return True
        return False

    def has_object_delete_permission(request):
        if request.user.roles == "admin":
            return True
        return False


class Project(models.Model):
    id_project = models.AutoField(primary_key=True)
    id_funding = models.ForeignKey(Funding, models.DO_NOTHING, db_column="id_funding")
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = "project"

    @staticmethod
    def has_read_permission(request):
        if (
            request.user.roles == "registro"
            or request.user.roles == "admin"
            or request.user.roles == "etiquetado"
            or request.user.roles == "usuario"
        ):
            return True
        return False

    def has_object_read_permission(self, request):
        if (
            request.user.roles == "registro"
            or request.user.roles == "admin"
            or request.user.roles == "etiquetado"
            or request.user.roles == "usuario"
        ):
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    def has_object_write_permission(self, request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_destroy_permission(request):
        if request.user.roles == "admin":
            return True
        return False


    def has_object_destroy_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False


class PulseType(models.Model):
    id_pulse_type = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "pulse_type"

    @staticmethod
    def has_read_permission(request):
        if (
            request.user.roles == "admin"

        ):
            return True
        return False

    def has_object_read_permission(self, request):
        if (
                request.user.roles == "admin"

        ):
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if request.user.roles == "admin":
            return True
        return False

    def has_object_write_permission(self, request):
        if  request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_destroy_permission(request):
        if request.user.roles == "admin":
            return True
        return False

    def has_object_destroy_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False


class Record(models.Model):
    id_record = models.AutoField(primary_key=True)
    id_catalogue = models.ForeignKey(
        Catalogue, models.DO_NOTHING, db_column="id_catalogue"
    )
    id_format = models.ForeignKey(Format, models.DO_NOTHING, db_column="id_format")
    date = models.DateTimeField(blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    size = models.FloatField(blank=True, null=True)
    sample_rate = models.IntegerField(blank=True, null=True)
    chunk = models.IntegerField(blank=True, null=True)
    channels = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.date

    class Meta:
        managed = False
        db_table = "record"

    @staticmethod
    def has_read_permission(request):
        if (
            request.user.roles == "registro"
            or request.user.roles == "admin"
            or request.user.roles == "etiquetado"
            or request.user.roles == "usuario"
        ):
            return True
        return False

    def has_object_read_permission(self, request):
        if (
            request.user.roles == "registro"
            or request.user.roles == "admin"
            or request.user.roles == "etiquetado"
            or request.user.roles == "usuario"
        ):
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    def has_object_write_permission(self, request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_destroy_permission(request):
        if request.user.roles == "admin":
            return True
        return False


    def has_object_destroy_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False


class RecordObs(models.Model):
    id_record_obs = models.AutoField(primary_key=True)
    id_record = models.ForeignKey(Record, models.DO_NOTHING, db_column="id_record")
    observation = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.observation

    class Meta:
        managed = False
        db_table = "record_obs"

    @staticmethod
    def has_read_permission(request):
        if (
            request.user.roles == "registro"
            or request.user.roles == "admin"
            or request.user.roles == "etiquetado"
            or request.user.roles == "usuario"
        ):
            return True
        return False

    def has_object_read_permission(self, request):
        if (
            request.user.roles == "registro"
            or request.user.roles == "admin"
            or request.user.roles == "etiquetado"
            or request.user.roles == "usuario"
        ):
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    def has_object_write_permission(self, request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_destroy_permission(request):
        if request.user.roles == "admin":
            return True
        return False


    def has_object_destroy_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False


class RecordPath(models.Model):
    id_record_path = models.AutoField(primary_key=True)
    id_record = models.ForeignKey(Record, models.DO_NOTHING, db_column="id_record")
    record_path = models.CharField(max_length=100, blank=True, null=True)
    fingerprint = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.fingerprint

    class Meta:
        managed = False
        db_table = "record_path"

    @staticmethod
    def has_read_permission(request):
        if (
            request.user.roles == "registro"
            or request.user.roles == "admin"
            or request.user.roles == "etiquetado"
            or request.user.roles == "usuario"
        ):
            return True
        return False

    def has_object_read_permission(self, request):
        if (
            request.user.roles == "registro"
            or request.user.roles == "admin"
            or request.user.roles == "etiquetado"
            or request.user.roles == "usuario"
        ):
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    def has_object_write_permission(self, request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_destroy_permission(request):
        if request.user.roles == "admin":
            return True
        return False


    def has_object_destroy_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False


class Sampling(models.Model):
    id_sampling = models.AutoField(primary_key=True)
    id_project = models.ForeignKey(Project, models.DO_NOTHING, db_column="id_project")
    id_cataloger = models.ForeignKey(
        "User", models.DO_NOTHING, db_column="id_cataloger"
    )
    id_season = models.ForeignKey("Season", models.DO_NOTHING, db_column="id_season")
    date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = "sampling"

    @staticmethod
    def has_read_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    def has_object_read_permission(self, request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    def has_object_write_permission(self, request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_destroy_permission(request):
        if request.user.roles == "admin":
            return True
        return False


    def has_object_destroy_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False


class Season(models.Model):
    id_season = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = "season"

    @staticmethod
    def has_read_permission(request):
        if (
            request.user.roles == "registro"
            or request.user.roles == "admin"
            or request.user.roles == "etiquetado"
            or request.user.roles == "usuario"
        ):
            return True
        return False

    def has_object_read_permission(self, request):
        if (
            request.user.roles == "registro"
            or request.user.roles == "admin"
            or request.user.roles == "etiquetado"
            or request.user.roles == "usuario"
        ):
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    def has_object_write_permission(self, request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_destroy_permission(request):
        if request.user.roles == "admin":
            return True
        return False


    def has_object_destroy_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False


class Software(models.Model):
    id_software = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = "software"

    @staticmethod
    def has_read_permission(request):
        if (
                request.user.roles == "admin"

        ):
            return True
        return False

    def has_object_read_permission(self, request):
        if (
                request.user.roles == "admin"

        ):
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if request.user.roles == "admin":
            return True
        return False

    def has_object_write_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_destroy_permission(request):
        if request.user.roles == "admin":
            return True
        return False

    def has_object_destroy_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False

class Supply(models.Model):
    id_supply = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.description

    @staticmethod
    def has_read_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    def has_object_read_permission(self, request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    def has_object_write_permission(self, request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if request.user.roles == "registro" or request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_destroy_permission(request):
        if request.user.roles == "admin":
            return True
        return False


    def has_object_destroy_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False

    class Meta:
        managed = False
        db_table = "supply"


class TimeDetail(models.Model):
    id_time_detail = models.AutoField(primary_key=True)
    id_labeled = models.IntegerField()
    beginning = models.SmallIntegerField(blank=True, null=True)
    ending = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "time_detail"

    @staticmethod
    def has_read_permission(request):
        if (
                request.user.roles == "admin"

        ):
            return True
        return False

    def has_object_read_permission(self, request):
        if (
                request.user.roles == "admin"

        ):
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if request.user.roles == "admin":
            return True
        return False

    def has_object_write_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_destroy_permission(request):
        if request.user.roles == "admin":
            return True
        return False

    def has_object_destroy_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False


class Type(models.Model):
    id_type = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = "type"


class Vereda(models.Model):
    id_vereda = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vereda"


    @staticmethod
    def has_read_permission(request):
        if (
                request.user.roles == "admin"

        ):
            return True
        return False

    def has_object_read_permission(self, request):
        if (
                request.user.roles == "admin"

        ):
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if request.user.roles == "admin":
            return True
        return False

    def has_object_write_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_destroy_permission(request):
        if request.user.roles == "admin":
            return True
        return False

    def has_object_destroy_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False


class Voucher(models.Model):
    id_voucher = models.OneToOneField(
        Catalogue, models.DO_NOTHING, db_column="id_voucher", primary_key=True
    )
    id_catalogue = models.IntegerField()
    voucher = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "voucher"


    @staticmethod
    def has_read_permission(request):
        if (
                request.user.roles == "admin"

        ):
            return True
        return False

    def has_object_read_permission(self, request):
        if (
                request.user.roles == "admin"

        ):
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        if request.user.roles == "admin":
            return True
        return False

    def has_object_write_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_create_permission(request):
        if request.user.roles == "admin":
            return True
        return False

    @staticmethod
    def has_destroy_permission(request):
        if request.user.roles == "admin":
            return True
        return False

    def has_object_destroy_permission(self, request):
        if request.user.roles == "admin":
            return True
        return False
