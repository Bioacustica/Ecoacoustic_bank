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
from django.db import models


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
    id_country = models.IntegerField()
    id_department = models.IntegerField()
    id_municipality = models.IntegerField()
    id_vereda = models.IntegerField()
    id_locality = models.IntegerField()
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
    # This field type is a guess.
    coordinates = models.TextField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    chunks = models.IntegerField(blank=True, null=True)
    size = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "catalogue"

    def __str__(self):
        return self.elevation


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


class Datum(models.Model):
    id_datum = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = "datum"


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


class Format(models.Model):
    id_format = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = "format"


class Funding(models.Model):
    id_funding = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

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


class Habitat(models.Model):
    id_habitat = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = "habitat"


class Hardware(models.Model):
    id_hardware = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = "hardware"


class Label(models.Model):
    id_label = models.AutoField(primary_key=True)
    id_type = models.ForeignKey("Type", models.DO_NOTHING, db_column="id_type")

    def __str__(self):
        return self.id_label

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


class Memory(models.Model):
    id_memory = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = "memory"


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


class Project(models.Model):
    id_project = models.AutoField(primary_key=True)
    id_funding = models.ForeignKey(Funding, models.DO_NOTHING, db_column="id_funding")
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = "project"


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


class RecordObs(models.Model):
    id_record_obs = models.AutoField(primary_key=True)
    id_record = models.ForeignKey(Record, models.DO_NOTHING, db_column="id_record")
    observation = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.observation

    class Meta:
        managed = False
        db_table = "record_obs"


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


class Season(models.Model):
    id_season = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = "season"


class Supply(models.Model):
    id_supply = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = "supply"


class Type(models.Model):
    id_type = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = "type"


class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = "user"
