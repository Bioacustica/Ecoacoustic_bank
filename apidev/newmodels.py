# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApicrudFrequencydetail(models.Model):
    id_frequency_detail = models.AutoField(primary_key=True)
    id_labeled = models.IntegerField()
    begining = models.IntegerField(blank=True, null=True)
    ending = models.IntegerField(blank=True, null=True)
    minimal = models.IntegerField(blank=True, null=True)
    maximun = models.IntegerField(blank=True, null=True)
    peak = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apiCRUD_frequencydetail'


class ApicrudHistoricalfunding(models.Model):
    id_funding = models.IntegerField()
    description = models.CharField(max_length=100, blank=True, null=True)
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    history_user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apiCRUD_historicalfunding'


class ApicrudLocality(models.Model):
    id_locality = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apiCRUD_locality'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class Case(models.Model):
    id_case = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'case'


class Catalogue(models.Model):
    id_catalogue = models.AutoField(primary_key=True)
    id_sampling = models.ForeignKey('Sampling', models.DO_NOTHING, db_column='id_sampling')
    id_country = models.ForeignKey('Country', models.DO_NOTHING, db_column='id_country')
    id_department = models.ForeignKey('Department', models.DO_NOTHING, db_column='id_department')
    id_municipality = models.ForeignKey('Municipality', models.DO_NOTHING, db_column='id_municipality')
    id_vereda = models.ForeignKey('Vereda', models.DO_NOTHING, db_column='id_vereda')
    id_locality = models.ForeignKey('Locality', models.DO_NOTHING, db_column='id_locality')
    id_gain = models.IntegerField()
    id_filters = models.IntegerField()
    id_collector = models.ForeignKey('User', models.DO_NOTHING, db_column='id_collector')
    id_h_serial = models.ForeignKey('HSerial', models.DO_NOTHING, db_column='id_h_serial')
    id_supply = models.ForeignKey('Supply', models.DO_NOTHING, db_column='id_supply')
    id_case = models.ForeignKey(Case, models.DO_NOTHING, db_column='id_case')
    id_memory = models.ForeignKey('Memory', models.DO_NOTHING, db_column='id_memory')
    id_habitat = models.ForeignKey('Habitat', models.DO_NOTHING, db_column='id_habitat')
    id_precision = models.ForeignKey('Precision', models.DO_NOTHING, db_column='id_precision')
    id_datum = models.ForeignKey('Datum', models.DO_NOTHING, db_column='id_datum')
    elevation = models.IntegerField(blank=True, null=True)
    coordinates = models.TextField(blank=True, null=True)  # This field type is a guess.
    height = models.IntegerField(blank=True, null=True)
    chunks = models.SmallIntegerField(blank=True, null=True)
    size = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogue'


class CatalogueObs(models.Model):
    id_catalogue_obs = models.AutoField(primary_key=True)
    id_catalogue = models.ForeignKey(Catalogue, models.DO_NOTHING, db_column='id_catalogue')
    observation = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogue_obs'


class Country(models.Model):
    id_country = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class Datum(models.Model):
    id_datum = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datum'


class Department(models.Model):
    id_department = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoRestPasswordresetResetpasswordtoken(models.Model):
    created_at = models.DateTimeField()
    key = models.CharField(unique=True, max_length=64)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.CharField(max_length=256)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_rest_passwordreset_resetpasswordtoken'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Evidence(models.Model):
    id_evidence = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evidence'


class Format(models.Model):
    id_format = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'format'


class FrequencyDetail(models.Model):
    id_frequency_detail = models.AutoField(primary_key=True)
    id_labeled = models.IntegerField()
    beginning = models.IntegerField(blank=True, null=True)
    ending = models.IntegerField(blank=True, null=True)
    minimal = models.IntegerField(blank=True, null=True)
    maximum = models.IntegerField(blank=True, null=True)
    peak = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frequency_detail'


class Funding(models.Model):
    id_funding = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'funding'


class HSerial(models.Model):
    id_h_serial = models.SmallAutoField(primary_key=True)
    id_hardware = models.ForeignKey('Hardware', models.DO_NOTHING, db_column='id_hardware')
    h_serial = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'h_serial'


class Habitat(models.Model):
    id_habitat = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'habitat'


class Hardware(models.Model):
    id_hardware = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hardware'


class Label(models.Model):
    id_label = models.SmallAutoField(primary_key=True)
    id_type = models.ForeignKey('Type', models.DO_NOTHING, db_column='id_type')
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'label'


class Labeled(models.Model):
    id_labeled = models.AutoField(primary_key=True)
    id_label = models.ForeignKey(Label, models.DO_NOTHING, db_column='id_label')
    id_record = models.ForeignKey('Record', models.DO_NOTHING, db_column='id_record')
    id_evidence = models.ForeignKey(Evidence, models.DO_NOTHING, db_column='id_evidence')
    id_labeler = models.ForeignKey('User', models.DO_NOTHING, db_column='id_labeler')
    id_software = models.ForeignKey('Software', models.DO_NOTHING, db_column='id_software')
    id_measure = models.ForeignKey('Measure', models.DO_NOTHING, db_column='id_measure')
    date = models.DateTimeField()
    membership = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    n_calls = models.SmallIntegerField(blank=True, null=True)
    id_pulse_type = models.ForeignKey('PulseType', models.DO_NOTHING, db_column='id_pulse_type', blank=True, null=True)
    id_time_detail = models.ForeignKey('TimeDetail', models.DO_NOTHING, db_column='id_time_detail', blank=True, null=True)
    id_frequency_detail = models.ForeignKey(FrequencyDetail, models.DO_NOTHING, db_column='id_frequency_detail', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'labeled'


class Locality(models.Model):
    id_locality = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locality'


class Measure(models.Model):
    id_measure = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'measure'


class Memory(models.Model):
    id_memory = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'memory'


class Municipality(models.Model):
    id_municipality = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipality'


class PhotoPath(models.Model):
    id_photo_path = models.AutoField(primary_key=True)
    id_catalogue = models.ForeignKey(Catalogue, models.DO_NOTHING, db_column='id_catalogue')
    path = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'photo_path'


class Precision(models.Model):
    id_precision = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'precision'


class Project(models.Model):
    id_project = models.SmallAutoField(primary_key=True)
    id_funding = models.ForeignKey(Funding, models.DO_NOTHING, db_column='id_funding')
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'


class PulseType(models.Model):
    id_pulse_type = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'pulse_type'


class Record(models.Model):
    id_record = models.AutoField(primary_key=True)
    id_catalogue = models.ForeignKey(Catalogue, models.DO_NOTHING, db_column='id_catalogue')
    id_format = models.ForeignKey(Format, models.DO_NOTHING, db_column='id_format')
    date = models.DateTimeField(blank=True, null=True)
    length = models.SmallIntegerField(blank=True, null=True)
    size = models.FloatField(blank=True, null=True)
    sample_rate = models.IntegerField(blank=True, null=True)
    chunk = models.SmallIntegerField(blank=True, null=True)
    channels = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record'


class RecordObs(models.Model):
    id_record_obs = models.AutoField(primary_key=True)
    id_record = models.ForeignKey(Record, models.DO_NOTHING, db_column='id_record')
    observation = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record_obs'


class RecordPath(models.Model):
    id_record_path = models.AutoField(primary_key=True)
    id_record = models.ForeignKey(Record, models.DO_NOTHING, db_column='id_record')
    record_path = models.CharField(max_length=100, blank=True, null=True)
    fingerprint = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record_path'


class RestFrameworkTrackingApirequestlog(models.Model):
    id = models.BigAutoField(primary_key=True)
    requested_at = models.DateTimeField()
    response_ms = models.IntegerField()
    path = models.CharField(max_length=200)
    remote_addr = models.GenericIPAddressField()
    host = models.CharField(max_length=200)
    method = models.CharField(max_length=10)
    query_params = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    status_code = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    view = models.CharField(max_length=200, blank=True, null=True)
    view_method = models.CharField(max_length=200, blank=True, null=True)
    errors = models.TextField(blank=True, null=True)
    username_persistent = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rest_framework_tracking_apirequestlog'


class Sampling(models.Model):
    id_sampling = models.AutoField(primary_key=True)
    id_project = models.ForeignKey(Project, models.DO_NOTHING, db_column='id_project')
    id_cataloger = models.ForeignKey('User', models.DO_NOTHING, db_column='id_cataloger')
    id_season = models.ForeignKey('Season', models.DO_NOTHING, db_column='id_season')
    date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sampling'


class Season(models.Model):
    id_season = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'season'


class Software(models.Model):
    id_software = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'software'


class Supply(models.Model):
    id_supply = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supply'


class TimeDetail(models.Model):
    id_time_detail = models.AutoField(primary_key=True)
    id_labeled = models.IntegerField()
    beginning = models.SmallIntegerField(blank=True, null=True)
    ending = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time_detail'


class Type(models.Model):
    id_type = models.SmallIntegerField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type'


class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    last_login = models.DateField(blank=True, null=True)
    is_admin = models.BooleanField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_staff = models.BooleanField(blank=True, null=True)
    is_superuser = models.BooleanField(blank=True, null=True)
    roles = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class Vereda(models.Model):
    id_vereda = models.SmallAutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vereda'


class Voucher(models.Model):
    id_voucher = models.OneToOneField(Catalogue, models.DO_NOTHING, db_column='id_voucher', primary_key=True)
    id_catalogue = models.IntegerField()
    voucher = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voucher'
