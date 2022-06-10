# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Appeal(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    komu_peredano = models.CharField(max_length=-1, blank=True, null=True)
    fio_actives = models.CharField(max_length=-1, blank=True, null=True)
    user_fio = models.CharField(max_length=-1, blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    complaint_result = models.TextField(blank=True, null=True)
    shift = models.BooleanField(blank=True, null=True)
    phone = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fio = models.CharField(max_length=-1, blank=True, null=True)
    iin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    sex = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    subtype_call = models.ForeignKey('SSubtypeCall', models.DO_NOTHING, blank=True, null=True)
    type_call = models.ForeignKey('STypeCall', models.DO_NOTHING, blank=True, null=True)
    workplace = models.ForeignKey('SWorkplace', models.DO_NOTHING, blank=True, null=True)
    pmsp_name = models.ForeignKey('SPmsp', models.DO_NOTHING, blank=True, null=True)
    region = models.ForeignKey('SRegion', models.DO_NOTHING, blank=True, null=True)
    complaint_status = models.ForeignKey('SAppealStatus', models.DO_NOTHING, blank=True, null=True)
    giid = models.CharField(max_length=-1, blank=True, null=True)
    is_first = models.BooleanField(blank=True, null=True)
    agent_id = models.CharField(max_length=123, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appeal'


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
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BorcovskyBridge(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    agent_name = models.CharField(max_length=123, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'borcovsky_bridge'


class Company(models.Model):
    bin = models.CharField(unique=True, max_length=30, blank=True, null=True)
    abrev_rus = models.CharField(max_length=30, blank=True, null=True)
    name_ru = models.CharField(max_length=1000, blank=True, null=True)
    addr = models.CharField(max_length=2000, blank=True, null=True)
    date_last_upd = models.DateTimeField(blank=True, null=True)
    type_med = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    status = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    coverage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    custom_sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class DCallPatient(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    incident = models.ForeignKey('GIncident', models.DO_NOTHING)
    patient = models.ForeignKey('GPatient', models.DO_NOTHING)
    status = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_call_patient'


class DCallingList(models.Model):
    date_time = models.DateTimeField(blank=True, null=True)
    patient_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    operator_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    status = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_calling_list'


class DNosology(models.Model):
    incident_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    disease_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    date_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_nosology'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GIncallLog(models.Model):
    globalinteractionid = models.CharField(max_length=-1, blank=True, null=True)
    interactionstepid = models.CharField(max_length=-1, blank=True, null=True)
    customerphone = models.CharField(max_length=-1, blank=True, null=True)
    language = models.CharField(max_length=-1, blank=True, null=True)
    destination = models.CharField(max_length=-1, blank=True, null=True)
    g_incident_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    direction = models.CharField(max_length=-1, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'g_incall_log'


class GIncident(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    date_time = models.DateTimeField()
    type_call = models.DecimalField(max_digits=65535, decimal_places=65535)
    type_sess = models.DecimalField(max_digits=65535, decimal_places=65535)
    user_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    phone = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lang_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    category = models.ForeignKey('SCategory', models.DO_NOTHING)
    ratio = models.ForeignKey('SRatio', models.DO_NOTHING, blank=True, null=True)
    resident = models.BooleanField(blank=True, null=True)
    agree = models.BooleanField(blank=True, null=True)
    fio = models.CharField(max_length=-1, blank=True, null=True)
    fio_lat = models.CharField(max_length=-1, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    sex = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    country_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    place_of_birth = models.CharField(max_length=-1, blank=True, null=True)
    iin = models.CharField(max_length=-1, blank=True, null=True)
    citizenship_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    typedoc = models.ForeignKey('STypedoc', models.DO_NOTHING, blank=True, null=True)
    crossdoc = models.BooleanField(blank=True, null=True)
    num_crossdoc = models.CharField(max_length=-1, blank=True, null=True)
    date_crossdoc = models.DateTimeField(blank=True, null=True)
    loc_country = models.CharField(max_length=-1, blank=True, null=True)
    loc_city = models.CharField(max_length=-1, blank=True, null=True)
    loc_street = models.CharField(max_length=-1, blank=True, null=True)
    loc_home = models.CharField(max_length=-1, blank=True, null=True)
    loc_block = models.CharField(max_length=-1, blank=True, null=True)
    loc_flat = models.CharField(max_length=-1, blank=True, null=True)
    pmsp_name = models.CharField(max_length=-1, blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)
    blood_group = models.CharField(max_length=-1, blank=True, null=True)
    rfactor = models.CharField(max_length=-1, blank=True, null=True)
    date_edit = models.DateTimeField(blank=True, null=True)
    lament = models.CharField(max_length=-1, blank=True, null=True)
    anamnesis = models.CharField(max_length=-1, blank=True, null=True)
    diagnosis = models.CharField(max_length=-1, blank=True, null=True)
    recom = models.CharField(max_length=-1, blank=True, null=True)
    coment = models.CharField(max_length=-1, blank=True, null=True)
    user_edit = models.CharField(max_length=-1, blank=True, null=True)
    status_close = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rating = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    user_close = models.CharField(max_length=-1, blank=True, null=True)
    date_close = models.DateTimeField(blank=True, null=True)
    social_status = models.ForeignKey('SSocialStatus', models.DO_NOTHING, db_column='social_status', blank=True, null=True)
    work_place = models.CharField(max_length=-1, blank=True, null=True)
    study_place = models.CharField(max_length=-1, blank=True, null=True)
    date_last_ws = models.DateTimeField(blank=True, null=True)
    phone_contact = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    phone_contact_m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pcr = models.CharField(max_length=-1, blank=True, null=True)
    wellbeing = models.CharField(max_length=-1, blank=True, null=True)
    ojirenie = models.BooleanField(blank=True, null=True)
    serdce = models.BooleanField(blank=True, null=True)
    astma = models.BooleanField(blank=True, null=True)
    pechen = models.BooleanField(blank=True, null=True)
    pochki = models.BooleanField(blank=True, null=True)
    gema_rast = models.BooleanField(blank=True, null=True)
    pregnancy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bolvgorle = models.BooleanField(blank=True, null=True)
    nasmork = models.BooleanField(blank=True, null=True)
    kashel = models.BooleanField(blank=True, null=True)
    otdishka = models.BooleanField(blank=True, null=True)
    diareya = models.BooleanField(blank=True, null=True)
    other_simp = models.CharField(max_length=-1, blank=True, null=True)
    other_diagnos = models.CharField(max_length=-1, blank=True, null=True)
    max_temp = models.CharField(max_length=-1, blank=True, null=True)
    date_f_simp = models.DateTimeField(blank=True, null=True)
    lab_actv = models.ForeignKey('SLaborActivity', models.DO_NOTHING, blank=True, null=True)
    c_contact_zabol = models.BooleanField(blank=True, null=True)
    c_contact_covid = models.BooleanField(blank=True, null=True)
    c_med_org = models.CharField(max_length=-1, blank=True, null=True)
    c_fio = models.CharField(max_length=-1, blank=True, null=True)
    c_typ_contact = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c_date_last = models.DateTimeField(blank=True, null=True)
    c_date_pcr = models.DateTimeField(blank=True, null=True)
    c_pcr_result = models.CharField(max_length=-1, blank=True, null=True)
    c_perem = models.BooleanField(blank=True, null=True)
    c_perem_bdate = models.DateTimeField(blank=True, null=True)
    c_perem_edate = models.DateTimeField(blank=True, null=True)
    c_oblast = models.CharField(max_length=-1, blank=True, null=True)
    c_region = models.CharField(max_length=-1, blank=True, null=True)
    c_city = models.CharField(max_length=-1, blank=True, null=True)
    c_street = models.CharField(max_length=-1, blank=True, null=True)
    c_home = models.CharField(max_length=-1, blank=True, null=True)
    c_flat = models.CharField(max_length=-1, blank=True, null=True)
    c_block = models.CharField(max_length=-1, blank=True, null=True)
    c_index = models.CharField(max_length=-1, blank=True, null=True)
    h_params = models.CharField(max_length=123, blank=True, null=True)
    village = models.CharField(max_length=-1, blank=True, null=True)
    risk_group = models.ForeignKey('SRiskGroup', models.DO_NOTHING, db_column='risk_group', blank=True, null=True)
    hobl = models.BooleanField(blank=True, null=True)
    loc_region = models.CharField(max_length=-1, blank=True, null=True)
    user_id_edit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hypertension = models.BooleanField(blank=True, null=True)
    cancer = models.BooleanField(blank=True, null=True)
    h_oth_zabolev = models.BooleanField(blank=True, null=True)
    h_pnevmonia = models.BooleanField(blank=True, null=True)
    h_sahar_diabet = models.BooleanField(blank=True, null=True)
    h_oth_endocrin = models.BooleanField(blank=True, null=True)
    h_hobl = models.BooleanField(blank=True, null=True)
    vaccine_dose = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vaccine_date1 = models.DateTimeField(blank=True, null=True)
    vaccine_date2 = models.DateTimeField(blank=True, null=True)
    vaccine_type = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    phone_other = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'g_incident'


class GIncidentLog(models.Model):
    id = models.DecimalField(max_digits=65535, decimal_places=65535)
    date_time = models.DateTimeField()
    type_call = models.DecimalField(max_digits=65535, decimal_places=65535)
    type_sess = models.DecimalField(max_digits=65535, decimal_places=65535)
    user_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    phone = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lang_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    category_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    ratio_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    resident = models.BooleanField(blank=True, null=True)
    agree = models.BooleanField(blank=True, null=True)
    fio = models.CharField(max_length=-1, blank=True, null=True)
    fio_lat = models.CharField(max_length=-1, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    sex = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    country_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    place_of_birth = models.CharField(max_length=-1, blank=True, null=True)
    iin = models.CharField(max_length=-1, blank=True, null=True)
    citizenship_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    typedoc_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    crossdoc = models.BooleanField(blank=True, null=True)
    num_crossdoc = models.CharField(max_length=-1, blank=True, null=True)
    date_crossdoc = models.DateTimeField(blank=True, null=True)
    loc_country = models.CharField(max_length=-1, blank=True, null=True)
    loc_city = models.CharField(max_length=-1, blank=True, null=True)
    loc_street = models.CharField(max_length=-1, blank=True, null=True)
    loc_home = models.CharField(max_length=-1, blank=True, null=True)
    loc_block = models.CharField(max_length=-1, blank=True, null=True)
    loc_flat = models.CharField(max_length=-1, blank=True, null=True)
    pmsp_name = models.CharField(max_length=-1, blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)
    blood_group = models.CharField(max_length=-1, blank=True, null=True)
    rfactor = models.CharField(max_length=-1, blank=True, null=True)
    date_edit = models.DateTimeField(blank=True, null=True)
    lament = models.CharField(max_length=-1, blank=True, null=True)
    anamnesis = models.CharField(max_length=-1, blank=True, null=True)
    diagnosis = models.CharField(max_length=-1, blank=True, null=True)
    recom = models.CharField(max_length=-1, blank=True, null=True)
    coment = models.CharField(max_length=-1, blank=True, null=True)
    user_edit = models.CharField(max_length=-1, blank=True, null=True)
    status_close = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rating = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    user_close = models.CharField(max_length=-1, blank=True, null=True)
    date_close = models.DateTimeField(blank=True, null=True)
    social_status = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    work_place = models.CharField(max_length=-1, blank=True, null=True)
    study_place = models.CharField(max_length=-1, blank=True, null=True)
    date_last_ws = models.DateTimeField(blank=True, null=True)
    phone_contact = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    phone_contact_m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pcr = models.CharField(max_length=-1, blank=True, null=True)
    wellbeing = models.CharField(max_length=-1, blank=True, null=True)
    ojirenie = models.BooleanField(blank=True, null=True)
    serdce = models.BooleanField(blank=True, null=True)
    astma = models.BooleanField(blank=True, null=True)
    pechen = models.BooleanField(blank=True, null=True)
    pochki = models.BooleanField(blank=True, null=True)
    gema_rast = models.BooleanField(blank=True, null=True)
    pregnancy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bolvgorle = models.BooleanField(blank=True, null=True)
    nasmork = models.BooleanField(blank=True, null=True)
    kashel = models.BooleanField(blank=True, null=True)
    otdishka = models.BooleanField(blank=True, null=True)
    diareya = models.BooleanField(blank=True, null=True)
    other_simp = models.CharField(max_length=-1, blank=True, null=True)
    other_diagnos = models.CharField(max_length=-1, blank=True, null=True)
    max_temp = models.CharField(max_length=-1, blank=True, null=True)
    date_f_simp = models.DateTimeField(blank=True, null=True)
    lab_actv_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c_contact_zabol = models.BooleanField(blank=True, null=True)
    c_contact_covid = models.BooleanField(blank=True, null=True)
    c_med_org = models.CharField(max_length=-1, blank=True, null=True)
    c_fio = models.CharField(max_length=-1, blank=True, null=True)
    c_typ_contact = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c_date_last = models.DateTimeField(blank=True, null=True)
    c_date_pcr = models.DateTimeField(blank=True, null=True)
    c_pcr_result = models.CharField(max_length=-1, blank=True, null=True)
    c_perem = models.BooleanField(blank=True, null=True)
    c_perem_bdate = models.DateTimeField(blank=True, null=True)
    c_perem_edate = models.DateTimeField(blank=True, null=True)
    c_oblast = models.CharField(max_length=-1, blank=True, null=True)
    c_region = models.CharField(max_length=-1, blank=True, null=True)
    c_city = models.CharField(max_length=-1, blank=True, null=True)
    c_street = models.CharField(max_length=-1, blank=True, null=True)
    c_home = models.CharField(max_length=-1, blank=True, null=True)
    c_flat = models.CharField(max_length=-1, blank=True, null=True)
    c_block = models.CharField(max_length=-1, blank=True, null=True)
    c_index = models.CharField(max_length=-1, blank=True, null=True)
    h_params = models.CharField(max_length=123, blank=True, null=True)
    village = models.CharField(max_length=-1, blank=True, null=True)
    risk_group = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hobl = models.BooleanField(blank=True, null=True)
    loc_region = models.CharField(max_length=-1, blank=True, null=True)
    user_id_edit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    date_edit_log = models.DateTimeField(blank=True, null=True)
    hypertension = models.BooleanField(blank=True, null=True)
    cancer = models.BooleanField(blank=True, null=True)
    h_oth_zabolev = models.BooleanField(blank=True, null=True)
    h_pnevmonia = models.BooleanField(blank=True, null=True)
    h_sahar_diabet = models.BooleanField(blank=True, null=True)
    h_oth_endocrin = models.BooleanField(blank=True, null=True)
    h_hobl = models.BooleanField(blank=True, null=True)
    vaccine_dose = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vaccine_date1 = models.DateTimeField(blank=True, null=True)
    vaccine_date2 = models.DateTimeField(blank=True, null=True)
    vaccine_type = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    phone_other = models.CharField(max_length=-1, blank=True, null=True)
    id_pk = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'g_incident_log'


class GMobileBrigades(models.Model):
    id = models.DecimalField(max_digits=65535, decimal_places=65535)
    pmsp_name = models.CharField(max_length=-1)
    region_code = models.CharField(max_length=-1)
    date_time = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    act = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    reserve = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    terapevt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pediatr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vop = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    feldsher = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    akysher = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    medsestra = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    psiholog = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    socrabotnik = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    voditel = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'g_mobile_brigades'


class GObservation(models.Model):
    id = models.BigAutoField(primary_key=True)
    patient = models.ForeignKey('GPatient', models.DO_NOTHING, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    sore_throat = models.BooleanField(blank=True, null=True)
    nasal_congestion = models.BooleanField(blank=True, null=True)
    shortness_breath = models.BooleanField(blank=True, null=True)
    vomiting = models.BooleanField(blank=True, null=True)
    nausea = models.BooleanField(blank=True, null=True)
    diarrhea = models.BooleanField(blank=True, null=True)
    dry_cough = models.BooleanField(blank=True, null=True)
    palpitations = models.BooleanField(blank=True, null=True)
    debility = models.BooleanField(blank=True, null=True)
    headache = models.BooleanField(blank=True, null=True)
    congestion_chest = models.BooleanField(blank=True, null=True)
    anosmia = models.BooleanField(blank=True, null=True)
    loss_taste = models.BooleanField(blank=True, null=True)
    cough_phlegm = models.BooleanField(blank=True, null=True)
    sweating = models.BooleanField(blank=True, null=True)
    dyspnea = models.BooleanField(blank=True, null=True)
    muscle_pain = models.BooleanField(blank=True, null=True)
    joint_pain = models.BooleanField(blank=True, null=True)
    discharge_eyes_redness = models.BooleanField(blank=True, null=True)
    rash = models.BooleanField(blank=True, null=True)
    comment = models.CharField(max_length=-1, blank=True, null=True)
    operator = models.ForeignKey('SOperators', models.DO_NOTHING, blank=True, null=True)
    temperature = models.CharField(max_length=-1, blank=True, null=True)
    systolic = models.CharField(max_length=-1, blank=True, null=True)
    diastolic = models.CharField(max_length=-1, blank=True, null=True)
    saturation = models.CharField(max_length=-1, blank=True, null=True)
    glucose_level = models.CharField(max_length=-1, blank=True, null=True)
    wellbeing = models.CharField(max_length=-1, blank=True, null=True)
    home_nabl = models.BooleanField(blank=True, null=True)
    ucl_bribiv = models.BooleanField(blank=True, null=True)
    vipoln_naznach = models.BooleanField(blank=True, null=True)
    vipoln_obzvona = models.BooleanField(blank=True, null=True)
    dostup_ctm = models.BooleanField(blank=True, null=True)
    sostoyznie = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    narushen_karantin = models.BooleanField(blank=True, null=True)
    video_call = models.BooleanField(blank=True, null=True)
    jaloba_na_pmsp = models.CharField(max_length=-1, blank=True, null=True)
    close_end = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    p_povtor_pcr = models.BooleanField(blank=True, null=True)
    p_go_street = models.BooleanField(blank=True, null=True)
    p_kt = models.BooleanField(blank=True, null=True)
    p_n_naznachenie = models.BooleanField(blank=True, null=True)
    p_n_list = models.BooleanField(blank=True, null=True)
    p_n_raspiska = models.BooleanField(blank=True, null=True)
    p_n_mb = models.BooleanField(blank=True, null=True)
    p_n_call = models.BooleanField(blank=True, null=True)
    medical_taken = models.CharField(max_length=-1, blank=True, null=True)
    violation_quar = models.CharField(max_length=-1, blank=True, null=True)
    violation_descr = models.CharField(max_length=-1, blank=True, null=True)
    dublicate = models.BooleanField(blank=True, null=True)
    f_send_mb = models.BooleanField(blank=True, null=True)
    f_corect_ls = models.BooleanField(blank=True, null=True)
    f_info_ses = models.BooleanField(blank=True, null=True)
    f_repeat_call = models.BooleanField(blank=True, null=True)
    f_conf_dc = models.BooleanField(blank=True, null=True)
    f_other_comp_pmsp = models.BooleanField(blank=True, null=True)
    f_social_help = models.BooleanField(blank=True, null=True)
    snijenie_sluha = models.BooleanField(blank=True, null=True)
    boli_v_jivote = models.BooleanField(blank=True, null=True)
    onemenie = models.BooleanField(blank=True, null=True)
    blagodarnost = models.CharField(max_length=-1, blank=True, null=True)
    f_primechanie = models.CharField(max_length=-1, blank=True, null=True)
    p_dk_end = models.BooleanField(blank=True, null=True)
    p_gospt_ranee = models.BooleanField(blank=True, null=True)
    p_net_svyazi = models.BooleanField(blank=True, null=True)
    p_error_data = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'g_observation'


class GPatient(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    fio = models.CharField(max_length=-1, blank=True, null=True)
    iin = models.CharField(max_length=-1, blank=True, null=True)
    phone = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    dozvon = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    status = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pmsp_name = models.CharField(max_length=-1, blank=True, null=True)
    watch_diagnosis = models.CharField(max_length=-1, blank=True, null=True)
    diagnosis_date = models.DateTimeField(blank=True, null=True)
    sign_observation_hospital = models.BooleanField(blank=True, null=True)
    pmsp_start_date = models.DateTimeField(blank=True, null=True)
    patient_condition_start = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pcr_date_test = models.DateTimeField(blank=True, null=True)
    pcr_date_receipt = models.DateTimeField(blank=True, null=True)
    pcr_reason = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    num_crossdoc = models.CharField(max_length=-1, blank=True, null=True)
    pcr_result = models.BooleanField(blank=True, null=True)
    status_end = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    status_end_date = models.DateTimeField(blank=True, null=True)
    incident_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lung_damage = models.BooleanField(blank=True, null=True)
    kt_date = models.DateTimeField(blank=True, null=True)
    result_kt = models.BooleanField(blank=True, null=True)
    diagnosis_kt = models.CharField(max_length=-1, blank=True, null=True)
    status_end_description = models.CharField(max_length=-1, blank=True, null=True)
    date_mobile_brigade = models.DateTimeField(blank=True, null=True)
    presc_therapy = models.CharField(max_length=-1, blank=True, null=True)
    info_function = models.IntegerField(blank=True, null=True)
    info_cond = models.IntegerField(blank=True, null=True)
    first_mb = models.IntegerField(blank=True, null=True)
    p_close_end = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    p_close_end_date = models.DateTimeField(blank=True, null=True)
    p_stationar = models.CharField(max_length=-1, blank=True, null=True)
    dozvon_type = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hospitalize_tmc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    close_date_post = models.DateTimeField(blank=True, null=True)
    complaint_ses = models.CharField(max_length=2000, blank=True, null=True)
    xray_date = models.DateTimeField(blank=True, null=True)
    xray = models.BooleanField(blank=True, null=True)
    xray_result = models.CharField(max_length=2000, blank=True, null=True)
    late_reg_reason = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    contact_pcr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    d_osmotr_cmp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    d_osmotr_pmsp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    d_osmotr_prof = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    d_lab_diag = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    d_inst = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    d_feedback = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    d_comment = models.CharField(max_length=500, blank=True, null=True)
    d_uchet = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'g_patient'


class GPatientLog(models.Model):
    id = models.DecimalField(max_digits=65535, decimal_places=65535)
    fio = models.CharField(max_length=-1, blank=True, null=True)
    iin = models.CharField(max_length=-1, blank=True, null=True)
    phone = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    dozvon = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    status = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pmsp_name = models.CharField(max_length=-1, blank=True, null=True)
    watch_diagnosis = models.CharField(max_length=-1, blank=True, null=True)
    diagnosis_date = models.DateTimeField(blank=True, null=True)
    sign_observation_hospital = models.BooleanField(blank=True, null=True)
    pmsp_start_date = models.DateTimeField(blank=True, null=True)
    patient_condition_start = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pcr_date_test = models.DateTimeField(blank=True, null=True)
    pcr_date_receipt = models.DateTimeField(blank=True, null=True)
    pcr_reason = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    num_crossdoc = models.CharField(max_length=-1, blank=True, null=True)
    pcr_result = models.BooleanField(blank=True, null=True)
    status_end = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    status_end_date = models.DateTimeField(blank=True, null=True)
    incident_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lung_damage = models.BooleanField(blank=True, null=True)
    kt_date = models.DateTimeField(blank=True, null=True)
    result_kt = models.BooleanField(blank=True, null=True)
    diagnosis_kt = models.CharField(max_length=-1, blank=True, null=True)
    status_end_description = models.CharField(max_length=-1, blank=True, null=True)
    date_mobile_brigade = models.DateTimeField(blank=True, null=True)
    presc_therapy = models.CharField(max_length=-1, blank=True, null=True)
    user_id_edit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    date_edit_log = models.DateTimeField(blank=True, null=True)
    info_function = models.IntegerField(blank=True, null=True)
    info_cond = models.IntegerField(blank=True, null=True)
    first_mb = models.IntegerField(blank=True, null=True)
    p_close_end = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    p_close_end_date = models.DateTimeField(blank=True, null=True)
    p_stationar = models.CharField(max_length=-1, blank=True, null=True)
    hospitalize_tmc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    complaint_ses = models.CharField(max_length=2000, blank=True, null=True)
    xray_date = models.DateTimeField(blank=True, null=True)
    xray = models.BooleanField(blank=True, null=True)
    xray_result = models.CharField(max_length=2000, blank=True, null=True)
    contact_pcr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    d_osmotr_cmp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    d_osmotr_pmsp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    d_osmotr_prof = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    d_lab_diag = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    d_inst = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    d_feedback = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    d_comment = models.CharField(max_length=500, blank=True, null=True)
    d_uchet = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_pk = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'g_patient_log'


class IncomingLogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=123, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    username = models.CharField(max_length=123, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incoming_logs'


class MainPmspuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=123)
    pmsp_bin = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_pmspuser'


class MainPmspuserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    pmspuser = models.ForeignKey(MainPmspuser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_pmspuser_groups'
        unique_together = (('pmspuser', 'group'),)


class MainPmspuserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    pmspuser = models.ForeignKey(MainPmspuser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_pmspuser_user_permissions'
        unique_together = (('pmspuser', 'permission'),)


class MdcReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    patient_id = models.AutoField()
    date_dn = models.DateField(blank=True, null=True)
    tip = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdc_report'


class Mo(models.Model):
    mo_name = models.CharField(max_length=30, blank=True, null=True)
    mo_type = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mo'


class Mobilebrigade(models.Model):
    id = models.BigAutoField(primary_key=True)
    actives = models.IntegerField(blank=True, null=True)
    reserved = models.IntegerField(blank=True, null=True)
    dr_terapevt = models.IntegerField(blank=True, null=True)
    dr_pediatr = models.IntegerField(blank=True, null=True)
    vop = models.IntegerField(blank=True, null=True)
    feldsher = models.IntegerField(blank=True, null=True)
    akusher = models.IntegerField(blank=True, null=True)
    med_sestra = models.IntegerField(blank=True, null=True)
    psiholog = models.IntegerField(blank=True, null=True)
    soc_rabotnik = models.IntegerField(blank=True, null=True)
    voditel = models.IntegerField(blank=True, null=True)
    company_bin = models.ForeignKey(Company, models.DO_NOTHING, db_column='company_bin', blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mobilebrigade'


class MonitoringTmc(models.Model):
    monitoring_id = models.BigAutoField(primary_key=True)
    date_monitoring = models.DateField(blank=True, null=True)
    dozvonilis = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    net_otveta = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_connection = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    didnt_call = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bessimptom = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    legkoi = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sredne = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hard = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    not_known = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    with_vilation = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    without_vilation = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monitoring_tmc'


class RaznicaTmc(models.Model):
    id_raznica = models.BigAutoField(primary_key=True)
    date_raznica = models.DateField(blank=True, null=True)
    bezsimptom_pmsp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    legkoi_pmsp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sred_pmsp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hard_pmsp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bezsimptom_tmc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    legkoi_tmc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sred_tmc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hard_tmc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'raznica_tmc'


class SAppealStatus(models.Model):
    name = models.CharField(max_length=123, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_appeal_status'


class SCategory(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    code = models.DecimalField(max_digits=65535, decimal_places=65535)
    name_ru = models.CharField(max_length=-1)
    name_kz = models.CharField(max_length=-1, blank=True, null=True)
    name_en = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_category'


class SCondition(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    name_ru = models.CharField(max_length=-1, blank=True, null=True)
    name_kz = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_condition'


class SCountry(models.Model):
    id = models.DecimalField(max_digits=65535, decimal_places=65535)
    iso_code = models.CharField(max_length=-1, blank=True, null=True)
    lat_code = models.CharField(max_length=-1, blank=True, null=True)
    name_ru = models.CharField(max_length=-1, blank=True, null=True)
    name_kz = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_country'


class SDisease(models.Model):
    id = models.IntegerField(primary_key=True)
    parent_id = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    name_ru = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_disease'


class SLaborActivity(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    name_ru = models.CharField(max_length=-1)
    name_kz = models.CharField(max_length=-1, blank=True, null=True)
    name_en = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_labor_activity'


class SLateReg(models.Model):
    id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    name_ru = models.CharField(max_length=-1, blank=True, null=True)
    name_kz = models.CharField(max_length=-1, blank=True, null=True)
    name_en = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_late_reg'


class SMedicService(models.Model):
    bin = models.CharField(primary_key=True, max_length=30)
    name_ru = models.CharField(max_length=1000, blank=True, null=True)
    addr = models.CharField(max_length=2000, blank=True, null=True)
    date_last_upd = models.DateTimeField(blank=True, null=True)
    abrev_rus = models.CharField(max_length=-1, blank=True, null=True)
    type_med = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    status = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    coverage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    custom_sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_medic_service'


class SOperators(models.Model):
    fio = models.CharField(max_length=-1)
    login = models.CharField(max_length=-1)
    password = models.CharField(max_length=-1)
    date_in = models.DateTimeField(blank=True, null=True)
    date_out = models.DateTimeField(blank=True, null=True)
    destination = models.CharField(max_length=-1, blank=True, null=True)
    role = models.CharField(max_length=-1, blank=True, null=True)
    status = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    role_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_operators'


class SPhones(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    num = models.CharField(max_length=20, blank=True, null=True)
    owner = models.CharField(max_length=500, blank=True, null=True)
    street = models.CharField(max_length=500, blank=True, null=True)
    numhome = models.CharField(max_length=12, blank=True, null=True)
    numblock = models.CharField(max_length=12, blank=True, null=True)
    numflat = models.CharField(max_length=12, blank=True, null=True)
    incident_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_phones'


class SPmsp(models.Model):
    bin = models.CharField(primary_key=True, max_length=-1)
    abrev_rus = models.CharField(max_length=-1, blank=True, null=True)
    name_ru = models.CharField(max_length=1000, blank=True, null=True)
    addr = models.CharField(max_length=2000, blank=True, null=True)
    date_last_upd = models.DateTimeField(blank=True, null=True)
    type_med = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    status = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    coverage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    custom_sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_pmsp'


class SRatio(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    code = models.DecimalField(max_digits=65535, decimal_places=65535)
    name_ru = models.CharField(max_length=-1)
    name_kz = models.CharField(max_length=-1, blank=True, null=True)
    name_en = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_ratio'


class SRegion(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    name_ru = models.CharField(max_length=500, blank=True, null=True)
    name_kz = models.CharField(max_length=500, blank=True, null=True)
    city_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    status = models.DecimalField(max_digits=65535, decimal_places=65535)
    code_op = models.DecimalField(max_digits=7, decimal_places=0, blank=True, null=True)
    st_city = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    st_view = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    checkbox = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    postal_code = models.CharField(unique=True, max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_region'


class SRiskGroup(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    name_ru = models.CharField(max_length=-1, blank=True, null=True)
    name_kz = models.CharField(max_length=-1, blank=True, null=True)
    name_en = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_risk_group'


class SSocialStatus(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    name_ru = models.CharField(max_length=-1)
    name_kz = models.CharField(max_length=-1, blank=True, null=True)
    name_en = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_social_status'


class SStatusClose(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    name_ru = models.CharField(max_length=-1)
    name_kz = models.CharField(max_length=-1, blank=True, null=True)
    name_en = models.CharField(max_length=-1, blank=True, null=True)
    type_status = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_status_close'


class SStatusEnd(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    name_ru = models.CharField(max_length=-1)
    name_kz = models.CharField(max_length=-1, blank=True, null=True)
    name_en = models.CharField(max_length=-1, blank=True, null=True)
    status_type = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    type_name = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_status_end'


class SStreet(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    name_ru = models.CharField(max_length=500, blank=True, null=True)
    name_kz = models.CharField(max_length=500, blank=True, null=True)
    streettype_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    city_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    status = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 's_street'


class SSubtypeCall(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_subtype_call'


class STypeCall(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_type_call'


class STypedoc(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    name_ru = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 's_typedoc'


class SVaccines(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    name_en = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_vaccines'


class SVillage(models.Model):
    village_id = models.CharField(max_length=-1, blank=True, null=True)
    name_ru = models.CharField(max_length=-1, blank=True, null=True)
    name_kz = models.CharField(max_length=-1, blank=True, null=True)
    township_id = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_village'


class SWorkplace(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_workplace'


class ViolationTmc(models.Model):
    violation_id = models.BigAutoField(primary_key=True)
    date_violation = models.DateField(blank=True, null=True)
    pmsp_name = models.CharField(max_length=500, blank=True, null=True)
    fio = models.CharField(max_length=500, blank=True, null=True)
    reason = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=500, blank=True, null=True)
    violation_tip = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'violation_tmc'
