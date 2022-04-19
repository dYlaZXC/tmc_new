# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import date, datetime

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


class GIncident(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    fio = models.CharField(max_length=255, blank=True, null=True)
    fio_lat = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    sex = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    country_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    place_of_birth = models.CharField(max_length=255, blank=True, null=True)
    iin = models.CharField(max_length=255, blank=True, null=True)
    citizenship_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    typedoc_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    crossdoc = models.BooleanField(blank=True, null=True)
    num_crossdoc = models.CharField(max_length=255, blank=True, null=True)
    date_crossdoc = models.DateTimeField(blank=True, null=True)
    loc_country = models.CharField(max_length=255, blank=True, null=True)
    loc_city = models.CharField(max_length=255, blank=True, null=True)
    loc_street = models.CharField(max_length=255, blank=True, null=True)
    loc_home = models.CharField(max_length=255, blank=True, null=True)
    loc_block = models.CharField(max_length=255, blank=True, null=True)
    loc_flat = models.CharField(max_length=255, blank=True, null=True)
    pmsp_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    blood_group = models.CharField(max_length=255, blank=True, null=True)
    rfactor = models.CharField(max_length=255, blank=True, null=True)
    date_edit = models.DateTimeField(blank=True, null=True)
    lament = models.CharField(max_length=255, blank=True, null=True)
    anamnesis = models.CharField(max_length=255, blank=True, null=True)
    diagnosis = models.CharField(max_length=255, blank=True, null=True)
    recom = models.CharField(max_length=255, blank=True, null=True)
    coment = models.CharField(max_length=255, blank=True, null=True)
    user_edit = models.CharField(max_length=255, blank=True, null=True)
    status_close = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rating = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    user_close = models.CharField(max_length=255, blank=True, null=True)
    date_close = models.DateTimeField(blank=True, null=True)
    social_status = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    work_place = models.CharField(max_length=255, blank=True, null=True)
    study_place = models.CharField(max_length=255, blank=True, null=True)
    date_last_ws = models.DateTimeField(blank=True, null=True)
    phone_contact = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    phone_contact_m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pcr = models.CharField(max_length=255, blank=True, null=True)
    wellbeing = models.CharField(max_length=255, blank=True, null=True)
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
    other_simp = models.CharField(max_length=255, blank=True, null=True)
    other_diagnos = models.CharField(max_length=255, blank=True, null=True)
    max_temp = models.CharField(max_length=255, blank=True, null=True)
    date_f_simp = models.DateTimeField(blank=True, null=True)
    lab_actv_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c_contact_zabol = models.BooleanField(blank=True, null=True)
    c_contact_covid = models.BooleanField(blank=True, null=True)
    c_med_org = models.CharField(max_length=255, blank=True, null=True)
    c_fio = models.CharField(max_length=255, blank=True, null=True)
    c_typ_contact = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c_date_last = models.DateTimeField(blank=True, null=True)
    c_date_pcr = models.DateTimeField(blank=True, null=True)
    c_pcr_result = models.CharField(max_length=255, blank=True, null=True)
    c_perem = models.BooleanField(blank=True, null=True)
    c_perem_bdate = models.DateTimeField(blank=True, null=True)
    c_perem_edate = models.DateTimeField(blank=True, null=True)
    c_oblast = models.CharField(max_length=255, blank=True, null=True)
    c_region = models.CharField(max_length=255, blank=True, null=True)
    c_city = models.CharField(max_length=255, blank=True, null=True)
    c_street = models.CharField(max_length=255, blank=True, null=True)
    c_home = models.CharField(max_length=255, blank=True, null=True)
    c_flat = models.CharField(max_length=255, blank=True, null=True)
    c_block = models.CharField(max_length=255, blank=True, null=True)
    c_index = models.CharField(max_length=255, blank=True, null=True)
    village = models.CharField(max_length=255, blank=True, null=True)
    risk_group = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hobl = models.BooleanField(blank=True, null=True)
    loc_region = models.CharField(max_length=255, blank=True, null=True)
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
    phone_other = models.CharField(max_length=255, blank=True, null=True)
    h_params = models.CharField(max_length=123, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'g_incident'

    def birthday_format(self):
        if self.birthday is not None:
            year = str(self.birthday.year)
            month = str(self.birthday.month) if self.birthday.month > 9 else '0' + str(self.birthday.month)
            day = str(self.birthday.day) if self.birthday.day > 9 else '0' + str(self.birthday.day)
            return year + '-' + month + '-' + day
    
    def date_start(self):
        if self.date_time is not None:
            year = str(self.date_time.year)
            month = str(self.date_time.month) if self.date_time.month > 9 else '0' + str(self.date_time.month)
            day = str(self.date_time.day) if self.date_time.day > 9 else '0' + str(self.date_time.day)
            return year + '-' + month + '-' + day
        else:
            return self.date_time  

    def time_start(self):
        if self.date_time is not None:
            if self.date_time.hour == 0:
                return str(self.date_time.hour) + '0:' + str(self.date_time.minute)
            return str(self.date_time.hour) + ':' + str(self.date_time.minute)


class GIncidentLog(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    fio = models.CharField(max_length=255, blank=True, null=True)
    fio_lat = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    sex = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    country_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    place_of_birth = models.CharField(max_length=255, blank=True, null=True)
    iin = models.CharField(max_length=255, blank=True, null=True)
    citizenship_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    typedoc_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    crossdoc = models.BooleanField(blank=True, null=True)
    num_crossdoc = models.CharField(max_length=255, blank=True, null=True)
    date_crossdoc = models.DateTimeField(blank=True, null=True)
    loc_country = models.CharField(max_length=255, blank=True, null=True)
    loc_city = models.CharField(max_length=255, blank=True, null=True)
    loc_street = models.CharField(max_length=255, blank=True, null=True)
    loc_home = models.CharField(max_length=255, blank=True, null=True)
    loc_block = models.CharField(max_length=255, blank=True, null=True)
    loc_flat = models.CharField(max_length=255, blank=True, null=True)
    pmsp_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    blood_group = models.CharField(max_length=255, blank=True, null=True)
    rfactor = models.CharField(max_length=255, blank=True, null=True)
    date_edit = models.DateTimeField(blank=True, null=True)
    lament = models.CharField(max_length=255, blank=True, null=True)
    anamnesis = models.CharField(max_length=255, blank=True, null=True)
    diagnosis = models.CharField(max_length=255, blank=True, null=True)
    recom = models.CharField(max_length=255, blank=True, null=True)
    coment = models.CharField(max_length=255, blank=True, null=True)
    user_edit = models.CharField(max_length=255, blank=True, null=True)
    status_close = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rating = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    user_close = models.CharField(max_length=255, blank=True, null=True)
    date_close = models.DateTimeField(blank=True, null=True)
    social_status = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    work_place = models.CharField(max_length=255, blank=True, null=True)
    study_place = models.CharField(max_length=255, blank=True, null=True)
    date_last_ws = models.DateTimeField(blank=True, null=True)
    phone_contact = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    phone_contact_m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pcr = models.CharField(max_length=255, blank=True, null=True)
    wellbeing = models.CharField(max_length=255, blank=True, null=True)
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
    other_simp = models.CharField(max_length=255, blank=True, null=True)
    other_diagnos = models.CharField(max_length=255, blank=True, null=True)
    max_temp = models.CharField(max_length=255, blank=True, null=True)
    date_f_simp = models.DateTimeField(blank=True, null=True)
    lab_actv_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c_contact_zabol = models.BooleanField(blank=True, null=True)
    c_contact_covid = models.BooleanField(blank=True, null=True)
    c_med_org = models.CharField(max_length=255, blank=True, null=True)
    c_fio = models.CharField(max_length=255, blank=True, null=True)
    c_typ_contact = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c_date_last = models.DateTimeField(blank=True, null=True)
    c_date_pcr = models.DateTimeField(blank=True, null=True)
    c_pcr_result = models.CharField(max_length=255, blank=True, null=True)
    c_perem = models.BooleanField(blank=True, null=True)
    c_perem_bdate = models.DateTimeField(blank=True, null=True)
    c_perem_edate = models.DateTimeField(blank=True, null=True)
    c_oblast = models.CharField(max_length=255, blank=True, null=True)
    c_region = models.CharField(max_length=255, blank=True, null=True)
    c_city = models.CharField(max_length=255, blank=True, null=True)
    c_street = models.CharField(max_length=255, blank=True, null=True)
    c_home = models.CharField(max_length=255, blank=True, null=True)
    c_flat = models.CharField(max_length=255, blank=True, null=True)
    c_block = models.CharField(max_length=255, blank=True, null=True)
    c_index = models.CharField(max_length=255, blank=True, null=True)
    h_params = models.CharField(max_length=123, blank=True, null=True)
    village = models.CharField(max_length=255, blank=True, null=True)
    risk_group = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hobl = models.BooleanField(blank=True, null=True)
    loc_region = models.CharField(max_length=255, blank=True, null=True)
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
    phone_other = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'g_incident_log'


class GMobileBrigades(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    pmsp_name = models.CharField(max_length=255)
    region_code = models.CharField(max_length=255)
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


class GPatient(models.Model):
    id = models.BigAutoField(primary_key=True)
    fio = models.CharField(max_length=65535, blank=True, null=True)
    iin = models.CharField(max_length=65535, blank=True, null=True)
    phone = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    dozvon = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    status = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pmsp_name = models.CharField(max_length=65535, blank=True, null=True)
    watch_diagnosis = models.CharField(max_length=65535, blank=True, null=True)
    diagnosis_date = models.DateTimeField(blank=True, null=True)
    sign_observation_hospital = models.BooleanField(blank=True, null=True)
    pmsp_start_date = models.DateTimeField(blank=True, null=True)
    patient_condition_start = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pcr_date_test = models.DateTimeField(blank=True, null=True)
    pcr_date_receipt = models.DateTimeField(blank=True, null=True)
    pcr_reason = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    num_crossdoc = models.CharField(max_length=65535, blank=True, null=True)
    pcr_result = models.BooleanField(blank=True, null=True)
    status_end = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    status_end_date = models.DateTimeField(blank=True, null=True)
    incident_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lung_damage = models.BooleanField(blank=True, null=True)
    kt_date = models.DateTimeField(blank=True, null=True)
    result_kt = models.BooleanField(blank=True, null=True)
    diagnosis_kt = models.CharField(max_length=65535, blank=True, null=True)
    status_end_description = models.CharField(max_length=65535, blank=True, null=True)
    date_mobile_brigade = models.DateTimeField(blank=True, null=True)
    presc_therapy = models.CharField(max_length=65535, blank=True, null=True)
    info_function = models.IntegerField(blank=True, null=True)
    info_cond = models.IntegerField(blank=True, null=True)
    first_mb = models.IntegerField(blank=True, null=True)
    p_close_end = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    p_close_end_date = models.DateTimeField(blank=True, null=True)
    p_stationar = models.CharField(max_length=65535, blank=True, null=True)
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

    def date_start_format(self):
        if self.date_start is not None:
            day = str(self.date_start.day) if self.date_start.day > 9 else '0' + str(self.date_start.day)
            month = str(self.date_start.month) if self.date_start.month > 9 else '0' + str(self.date_start.month)
            year = self.date_start.year
            return str(day) + '.' + str(month) + '.' + str(year)
        else:
            return self.date_start

    def pmsp_start_date_format(self):
        if self.pmsp_start_date is not None:
            day = str(self.pmsp_start_date.day) if self.pmsp_start_date.day > 9 else '0' + str(self.pmsp_start_date.day)
            month = str(self.pmsp_start_date.month) if self.pmsp_start_date.month > 9 else '0' + str(self.pmsp_start_date.month)
            year = self.pmsp_start_date.year
            hour = str(self.pmsp_start_date.hour) if self.pmsp_start_date.hour > 9 else '0' + str(self.pmsp_start_date.hour)
            minute = str(self.pmsp_start_date.minute) if self.pmsp_start_date.minute > 9 else '0' + str(self.pmsp_start_date.minute)
            return str(year) + '-' + str(month) + '-' + str(day) + 'T' + str(hour) + ':' + str(minute)
        else:
            return self.pmsp_start_date

    def pmsp_start_date_date_format(self):
        return str(self.pmsp_start_date)[:10]


    def days_count(self):
        if self.pcr_date_receipt is not None:
            return (date.today() - self.pcr_date_receipt.date()).days 
        else:
            return ''   


    def mb(self):
        if self.date_mobile_brigade is not None:
            return True
        else:
            return False             

    def status_end_date_format(self):
        if self.status_end_date is not None:
            day = str(self.status_end_date.day) if self.status_end_date.day > 9 else '0' + str(self.status_end_date.day)
            month = str(self.status_end_date.month) if self.status_end_date.month > 9 else '0' + str(self.status_end_date.month)
            year = str(self.status_end_date.year)
            minute = str(self.status_end_date.minute) if self.status_end_date.minute > 9 else '0' + str(self.status_end_date.minute)
            hour = str(self.status_end_date.hour) if self.status_end_date.hour > 9 else '0' + str(self.status_end_date.hour)
            second = str(self.status_end_date.second) if self.status_end_date.second > 9 else '0' + str(self.status_end_date.second)
            return str(str(year) + '-' + str(month) + '-' + str(day) + 'T' + hour + ':' + minute)
        else:
            return self.status_end_date


    def diagnosis_date_format(self):
        if self.diagnosis_date is not None:
            day = str(self.diagnosis_date.day) if self.diagnosis_date.day > 9 else '0' + str(self.diagnosis_date.day)
            month = str(self.diagnosis_date.month) if self.diagnosis_date.month > 9 else '0' + str(self.diagnosis_date.month)
            year = str(self.diagnosis_date.year)
            return year + '-' + month + '-' + day
        else:
            return self.diagnosis_date        

    def pcr_date_test_format(self):
        if self.pcr_date_test is not None:
            day = str(self.pcr_date_test.day) if self.pcr_date_test.day > 9 else '0' + str(self.pcr_date_test.day)
            month = str(self.pcr_date_test.month) if self.pcr_date_test.month > 9 else '0' + str(self.pcr_date_test.month)
            year = str(self.pcr_date_test.year)
            return year + '-' + month + '-' + day
        else:
            return self.pcr_date_test          

    def pcr_date_receipt_format(self):
        if self.pcr_date_receipt is not None:
            day = str(self.pcr_date_receipt.day) if self.pcr_date_receipt.day > 9 else '0' + str(self.pcr_date_receipt.day)
            month = str(self.pcr_date_receipt.month) if self.pcr_date_receipt.month > 9 else '0' + str(self.pcr_date_receipt.month)
            year = str(self.pcr_date_receipt.year)
            return year + '-' + month + '-' + day
        else:
            return self.pcr_date_receipt

    def kt_date_format(self):
        if self.kt_date is not None:
            day = str(self.kt_date.day) if self.kt_date.day > 9 else '0' + str(self.kt_date.day)
            month = str(self.kt_date.month) if self.kt_date.month > 9 else '0' + str(self.kt_date.month)
            year = str(self.kt_date.year)
            return year + '-' + month + '-' + day
        else:
            return self.kt_date

    def xray_date_format(self):
        if self.xray_date is not None:
            day = str(self.xray_date.day) if self.xray_date.day > 9 else '0' + str(self.xray_date.day)
            month = str(self.xray_date.month) if self.xray_date.month > 9 else '0' + str(self.xray_date.month)
            year = str(self.xray_date.year)
            return year + '-' + month + '-' + day
        else:
            return self.xray_date

    def date_mobile_brigade_format(self):
        if self.date_mobile_brigade is not None:
            day = str(self.date_mobile_brigade.day) if self.date_mobile_brigade.day > 9 else '0' + str(self.date_mobile_brigade.day)
            month = str(self.date_mobile_brigade.month) if self.date_mobile_brigade.month > 9 else '0' + str(self.date_mobile_brigade.month)
            year = str(self.date_mobile_brigade.year)
            return year + '-' + month + '-' + day
        else:
            return self.date_mobile_brigade

    def p_close_end_date_format(self):
        if self.p_close_end is not None:
            try:
                day = str(self.p_close_end_date.day) if self.p_close_end_date.day > 9 else '0' + str(self.p_close_end_date.day)
                month = str(self.p_close_end_date.month) if self.p_close_end_date.month > 9 else '0' + str(self.p_close_end_date.month)
                year = str(self.p_close_end_date.year)
                return year + '-' + month + '-' + day
            except AttributeError:
                return self.p_close_end_date    
        else:
            return self.p_close_end_date
    
    # def datetime_format(datetime):
    #     day = str(date.day) if date.day > 9 else '0' + str(date.day)
    #     month = str(date.month) if date.month > 9 else '0' + str(date.month)
    #     year = date.year   


class GPatientLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    fio = models.CharField(max_length=255, blank=True, null=True)
    iin = models.CharField(max_length=255, blank=True, null=True)
    phone = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    dozvon = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    status = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pmsp_name = models.CharField(max_length=255, blank=True, null=True)
    watch_diagnosis = models.CharField(max_length=255, blank=True, null=True)
    diagnosis_date = models.DateTimeField(blank=True, null=True)
    sign_observation_hospital = models.BooleanField(blank=True, null=True)
    pmsp_start_date = models.DateTimeField(blank=True, null=True)
    patient_condition_start = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pcr_date_test = models.DateTimeField(blank=True, null=True)
    pcr_date_receipt = models.DateTimeField(blank=True, null=True)
    pcr_reason = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    num_crossdoc = models.CharField(max_length=255, blank=True, null=True)
    pcr_result = models.BooleanField(blank=True, null=True)
    status_end = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    status_end_date = models.DateTimeField(blank=True, null=True)
    incident_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lung_damage = models.BooleanField(blank=True, null=True)
    kt_date = models.DateTimeField(blank=True, null=True)
    result_kt = models.BooleanField(blank=True, null=True)
    diagnosis_kt = models.CharField(max_length=255, blank=True, null=True)
    status_end_description = models.CharField(max_length=255, blank=True, null=True)
    date_mobile_brigade = models.DateTimeField(blank=True, null=True)
    presc_therapy = models.CharField(max_length=255, blank=True, null=True)
    user_id_edit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    date_edit_log = models.DateTimeField(blank=True, null=True)
    info_function = models.IntegerField(blank=True, null=True)
    info_cond = models.IntegerField(blank=True, null=True)
    first_mb = models.IntegerField(blank=True, null=True)
    p_close_end = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    p_close_end_date = models.DateTimeField(blank=True, null=True)
    p_stationar = models.CharField(max_length=255, blank=True, null=True)
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

    class Meta:
        managed = False
        db_table = 'g_patient_log'


class MainDocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    docfile = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'main_document'


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


class SCondition(models.Model):
    id = models.DecimalField(max_digits=65535, decimal_places=65535, primary_key=True)
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    name_kz = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_condition'


class SCountry(models.Model):
    id = models.DecimalField(max_digits=65535, decimal_places=65535, primary_key=True)
    iso_code = models.CharField(max_length=255, blank=True, null=True)
    lat_code = models.CharField(max_length=255, blank=True, null=True)
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    name_kz = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_country'


class SPmsp(models.Model):
    bin = models.CharField(primary_key=True, max_length=255)
    abrev_rus = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_pmsp'


class SRegion(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    name_ru = models.CharField(max_length=500)
    name_kz = models.CharField(max_length=500)
    city_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    status = models.DecimalField(max_digits=65535, decimal_places=65535)
    code_op = models.DecimalField(max_digits=7, decimal_places=0, blank=True, null=True)
    st_city = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    st_view = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    checkbox = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_region'


class SRiskGroup(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    name_kz = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_risk_group'


class SStatusEnd(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    name_ru = models.CharField(max_length=255)
    name_kz = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    status_type = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    type_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_status_end'


class STypedoc(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    name_ru = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 's_typedoc'


class SVillage(models.Model):
    village_id = models.CharField(max_length=255, primary_key=True)
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    name_kz = models.CharField(max_length=255, blank=True, null=True)
    township_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_village'

class SVaccines(models.Model):
    id = models.DecimalField(max_digits=65535, decimal_places=65535, primary_key=True)
    name_en = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 's_vaccines'


class TestBiVCopy(models.Model):
    patient_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    iin = models.CharField(max_length=255, blank=True, null=True)
    fio = models.CharField(max_length=255, blank=True, null=True)
    num_crossdoc = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    phone = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pmsp_start_date = models.DateTimeField(blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    loc_region = models.CharField(max_length=500, blank=True, null=True)
    loc_street = models.CharField(max_length=255, blank=True, null=True)
    loc_home = models.CharField(max_length=255, blank=True, null=True)
    status_end_date = models.DateTimeField(blank=True, null=True)
    status_end = models.CharField(max_length=255, blank=True, null=True)
    patient_age = models.FloatField(blank=True, null=True)
    not_dozvon_type = models.CharField(max_length=255, blank=True, null=True)
    refusal_hospitalize_tmc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sign_observation_hospital = models.BooleanField(blank=True, null=True)
    pmsp_name = models.CharField(max_length=255, blank=True, null=True)
    diagnosis = models.CharField(max_length=255, blank=True, null=True)
    pcr_result = models.BooleanField(blank=True, null=True)
    pcr_date_test = models.DateTimeField(blank=True, null=True)
    pcr_date_receipt = models.DateTimeField(blank=True, null=True)
    result_kt = models.BooleanField(blank=True, null=True)
    kt_date = models.DateTimeField(blank=True, null=True)
    diagnosis_kt = models.CharField(max_length=255, blank=True, null=True)
    condition_start = models.CharField(max_length=255, blank=True, null=True)
    pcr_reason = models.CharField(max_length=255, blank=True, null=True)
    other_diagnosis_pmsp = models.TextField(blank=True, null=True)
    presc_therapy = models.CharField(max_length=255, blank=True, null=True)
    lung_damage = models.BooleanField(blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    risk_group = models.CharField(max_length=255, blank=True, null=True)
    pregnancy = models.CharField(max_length=255, blank=True, null=True)
    diagnosis_date = models.DateTimeField(blank=True, null=True)
    date_mobile_brigade = models.DateTimeField(blank=True, null=True)
    vaccine_date1 = models.DateTimeField(blank=True, null=True)
    vaccine_date2 = models.DateTimeField(blank=True, null=True)
    vaccine_dose = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vaccine_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_bi_v_copy'


class TestBiVCopy1(models.Model):
    patient_id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    iin = models.CharField(max_length=255, blank=True, null=True)
    fio = models.CharField(max_length=255, blank=True, null=True)
    num_crossdoc = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    phone = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pmsp_start_date = models.DateTimeField(blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    loc_region = models.CharField(max_length=500, blank=True, null=True)
    loc_street = models.CharField(max_length=255, blank=True, null=True)
    loc_home = models.CharField(max_length=255, blank=True, null=True)
    status_end_date = models.DateTimeField(blank=True, null=True)
    status_end = models.CharField(max_length=255, blank=True, null=True)
    patient_age = models.FloatField(blank=True, null=True)
    not_dozvon_type = models.CharField(max_length=255, blank=True, null=True)
    refusal_hospitalize_tmc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sign_observation_hospital = models.BooleanField(blank=True, null=True)
    pmsp_name = models.CharField(max_length=255, blank=True, null=True)
    diagnosis = models.CharField(max_length=255, blank=True, null=True)
    pcr_result = models.BooleanField(blank=True, null=True)
    pcr_date_test = models.DateTimeField(blank=True, null=True)
    pcr_date_receipt = models.DateTimeField(blank=True, null=True)
    result_kt = models.BooleanField(blank=True, null=True)
    kt_date = models.DateTimeField(blank=True, null=True)
    diagnosis_kt = models.CharField(max_length=255, blank=True, null=True)
    condition_start = models.CharField(max_length=255, blank=True, null=True)
    pcr_reason = models.CharField(max_length=255, blank=True, null=True)
    other_diagnosis_pmsp = models.TextField(blank=True, null=True)
    presc_therapy = models.CharField(max_length=255, blank=True, null=True)
    lung_damage = models.BooleanField(blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    risk_group = models.CharField(max_length=255, blank=True, null=True)
    pregnancy = models.CharField(max_length=255, blank=True, null=True)
    diagnosis_date = models.DateTimeField(blank=True, null=True)
    date_mobile_brigade = models.DateTimeField(blank=True, null=True)
    vaccine_date1 = models.DateTimeField(blank=True, null=True)
    vaccine_date2 = models.DateTimeField(blank=True, null=True)
    vaccine_dose = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vaccine_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_bi_v_copy_1'


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


class SStreet(models.Model):
    id = models.DecimalField(max_digits=65535, decimal_places=65535, primary_key=True)
    name_ru = models.CharField(max_length=500)
    name_kz = models.CharField(max_length=500)
    streettype_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    city_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    status = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 's_street'


class SLateReg(models.Model):
    id = models.DecimalField(max_digits=65535, decimal_places=65535, primary_key=True)
    name_ru = models.CharField(max_length=500)        
    name_kz = models.CharField(max_length=500)        
    name_en = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 's_late_reg'


class DCallingList(models.Model):
    date_time = models.DateTimeField()        
    patient_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    operator_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    status = models.DecimalField(max_digits=65535, decimal_places=65535)
    # id = models.DecimalField(max_digits=65535, decimal_places=65535, primary_key=True)

    class Meta:
        managed = False
        db_table = 'd_calling_list'


class SOperators(models.Model):
    id = models.DecimalField(max_digits=65535, decimal_places=65535, primary_key=True)       
    fio = models.CharField(max_length=255, blank=True, null=True)
    login = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    date_in = models.DateTimeField()
    date_out = models.DateTimeField()
    destination = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    status = models.DecimalField(max_digits=65535, decimal_places=65535)
    role_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    
    class Meta:
        managed = False
        db_table = 's_operators'


class GObservation(models.Model):
    id = models.BigAutoField(primary_key=True)
    patient_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    comment = models.CharField(max_length=255, blank=True, null=True)
    operator_id = models.IntegerField(blank=True, null=True)
    temperature = models.CharField(max_length=255, blank=True, null=True)
    systolic = models.CharField(max_length=255, blank=True, null=True)
    diastolic = models.CharField(max_length=255, blank=True, null=True)
    saturation = models.CharField(max_length=255, blank=True, null=True)
    glucose_level = models.CharField(max_length=255, blank=True, null=True)
    wellbeing = models.CharField(max_length=255, blank=True, null=True)
    home_nabl = models.BooleanField(blank=True, null=True)
    ucl_bribiv = models.BooleanField(blank=True, null=True)
    vipoln_naznach = models.BooleanField(blank=True, null=True)
    vipoln_obzvona = models.BooleanField(blank=True, null=True)
    dostup_ctm = models.BooleanField(blank=True, null=True)
    sostoyznie = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    narushen_karantin = models.BooleanField(blank=True, null=True)
    video_call = models.BooleanField(blank=True, null=True)
    jaloba_na_pmsp = models.CharField(max_length=255, blank=True, null=True)
    close_end = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    p_povtor_pcr = models.BooleanField(blank=True, null=True)
    p_go_street = models.BooleanField(blank=True, null=True)
    p_kt = models.BooleanField(blank=True, null=True)
    p_n_naznachenie = models.BooleanField(blank=True, null=True)
    p_n_list = models.BooleanField(blank=True, null=True)
    p_n_raspiska = models.BooleanField(blank=True, null=True)
    p_n_mb = models.BooleanField(blank=True, null=True)
    p_n_call = models.BooleanField(blank=True, null=True)
    medical_taken = models.CharField(max_length=255, blank=True, null=True)
    violation_quar = models.CharField(max_length=255, blank=True, null=True)
    violation_descr = models.CharField(max_length=255, blank=True, null=True)
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
    blagodarnost = models.CharField(max_length=255, blank=True, null=True)
    f_primechanie = models.CharField(max_length=255, blank=True, null=True)
    p_dk_end = models.BooleanField(blank=True, null=True)
    p_gospt_ranee = models.BooleanField(blank=True, null=True)
    p_net_svyazi = models.BooleanField(blank=True, null=True)
    p_error_data = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'g_observation'


