from django.db import models


class CallbackQueueTable(models.Model):
    q_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    msgid = models.BinaryField(unique=True)
    corrid = models.CharField(max_length=128, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    state = models.SmallIntegerField(blank=True, null=True)
    delay = models.IntegerField(blank=True, null=True)
    expiration = models.IntegerField(blank=True, null=True)
    next_event_time = models.DateTimeField(blank=True, null=True)
    enq_time = models.DateTimeField(blank=True, null=True)
    enq_uid = models.TextField(blank=True, null=True)  # This field type is a guess.
    enq_tid = models.BigIntegerField(blank=True, null=True)
    deq_time = models.DateTimeField(blank=True, null=True)
    deq_uid = models.TextField(blank=True, null=True)  # This field type is a guess.
    deq_tid = models.BigIntegerField(blank=True, null=True)
    retry_count = models.IntegerField(blank=True, null=True)
    exception_qschema = models.CharField(max_length=30, blank=True, null=True)
    exception_queue = models.CharField(max_length=30, blank=True, null=True)
    user_data = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        db_table = 'callback_queue_table'


class DCallingList(models.Model):
    date_time = models.DateTimeField(blank=True, null=True)
    patient_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    operator_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    status = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        db_table = 'd_calling_list'


class GMobileBrigades(models.Model):
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
        db_table = 'g_mobile_brigades'

# 
class GPatient(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
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
    info_function = models.IntegerField(blank=True, null=True)
    info_cond = models.IntegerField(blank=True, null=True)
    first_mb = models.IntegerField(blank=True, null=True)
    p_close_end = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    p_close_end_date = models.DateTimeField(blank=True, null=True)
    p_stationar = models.CharField(max_length=255, blank=True, null=True)
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
        db_table = 'g_patient'


class GPatientLog(models.Model):
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
        db_table = 'g_patient_log'


#ЦЕЛЬ ВХОДЯЩЕГО ОБРАЩЕНИЯ
class SCategory(models.Model):
    name_ru = models.CharField(max_length=255)
    name_kz = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 's_category'

#
class SCondition(models.Model):
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    name_kz = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 's_condition'

#
class SCountry(models.Model):
    iso_code = models.CharField(max_length=255, blank=True, null=True)
    lat_code = models.CharField(max_length=255, blank=True, null=True)
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    name_kz = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 's_country'


class SDisease(models.Model):
    name_ru = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 's_disease'


class SLaborActivity(models.Model):
    name_ru = models.CharField(max_length=255)
    name_kz = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 's_labor_activity'


class SLateReg(models.Model):
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    name_kz = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 's_late_reg'


class SMedicService(models.Model):
    bin = models.CharField(primary_key=True, max_length=30)
    name_ru = models.CharField(max_length=1000, blank=True, null=True)
    addr = models.CharField(max_length=2000, blank=True, null=True)
    date_last_upd = models.DateTimeField(blank=True, null=True)
    abrev_rus = models.CharField(max_length=255, blank=True, null=True)
    type_med = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    status = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    coverage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    custom_sort = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 's_medic_service'


class SOperators(models.Model):
    fio = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    date_in = models.DateTimeField(blank=True, null=True)
    date_out = models.DateTimeField(blank=True, null=True)
    destination = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    status = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    role_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        db_table = 's_operators'


class GObservation(models.Model):
    id = models.BigAutoField(primary_key=True)
    patient = models.ForeignKey(GPatient, models.DO_NOTHING, blank=True, null=True)
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
    operator = models.ForeignKey(SOperators, models.DO_NOTHING, blank=True, null=True)
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
        db_table = 'g_observation'

#СПРАВОЧНИК телефоны
class SPhones(models.Model):
    num = models.CharField(max_length=20)
    owner = models.CharField(max_length=500)
    street = models.CharField(max_length=500, blank=True, null=True)
    numhome = models.CharField(max_length=12, blank=True, null=True)
    numblock = models.CharField(max_length=12, blank=True, null=True)
    numflat = models.CharField(max_length=12, blank=True, null=True)
    incident_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 's_phones'


#СПРАВОЧНИК ТИПА ОБРАЩЕНИЙ
class SRatio(models.Model):
    code = models.DecimalField(max_digits=65535, decimal_places=65535)
    name_ru = models.CharField(max_length=255)
    name_kz = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 's_ratio'


#СПРАВОЧНИК РЕГИОНОВ
class SRegion(models.Model):
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
        db_table = 's_region'


#СПРАВОЧНИК ГРУПП РИСКА
class SRiskGroup(models.Model):
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    name_kz = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 's_risk_group'

#СПРАВОЧНИК СОЦИАЛЬНЫХ СТАТУСОВ
class SSocialStatus(models.Model):
    name_ru = models.CharField(max_length=255)
    name_kz = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 's_social_status'


#СПРАВОЧНИК СОЦИАЛЬНЫХ СТАТУСОВ
class SStatusClose(models.Model):
    name_ru = models.CharField(max_length=255)
    name_kz = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    type_status = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        db_table = 's_status_close'

#СПРАВОЧНИК СТАТУСОВ ЗАВЕРШЕНИЯ
class SStatusEnd(models.Model):
    name_ru = models.CharField(max_length=255)
    name_kz = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    status_type = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    type_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 's_status_end'


#СПРАВОЧНИК УЛИЦ
class SStreet(models.Model):
    name_ru = models.CharField(max_length=500)
    name_kz = models.CharField(max_length=500)
    streettype_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    city_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    status = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        db_table = 's_street'


#СПРАВОЧНИК ПАСПОРТОВ (НАЦИОНАЛЬНЫЙ, СЛУЖЕБНЫЙ, ДИПЛОМАТИЧЕСКИЙ, ВНУТРЕННИЙ, УДОСТОВЕРЕНИЕ ЛИЧНОСТИ, ЛИЦА БЕЗ ГРАЖДАНСТВА)
class STypedoc(models.Model):
    name_ru = models.CharField(max_length=255)

    class Meta:
        db_table = 's_typedoc'


#СПРАВОЧНИК ВАКЦИН
class SVaccines(models.Model):
    name_en = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 's_vaccines'

#СПРАВОЧНИК ДЕРЕВЕНЬ
class SVillage(models.Model):
    village_id = models.CharField(max_length=255, blank=True, null=True)
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    name_kz = models.CharField(max_length=255, blank=True, null=True)
    township_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:  
        db_table = 's_village'

#СПРАВОЧНИК ПМСП
class PMSPS(models.Model):
    bin = models.CharField(max_length=30, blank=True, null=True)
    abrev_rus = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'table01'

# ПАЦИЕНТЫ
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
        db_table = 'test_bi_v_copy'

#ВАКЦИНАЦИЯ
class Vaccination(models.Model):
    iin = models.CharField(primary_key=True, max_length=50)
    fio = models.CharField(max_length=50, blank=True, null=True)
    birthday = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    pmsp_name = models.CharField(max_length=50, blank=True, null=True)
    edu_name = models.CharField(max_length=50, blank=True, null=True)
    is_vaccinated = models.CharField(max_length=50)
    not_vaccinated_reason = models.CharField(max_length=30, blank=True, null=True)
    vaccine_date1 = models.CharField(max_length=50, blank=True, null=True)
    vaccine_date2 = models.CharField(max_length=50, blank=True, null=True)
    vaccine_dose = models.CharField(max_length=50, blank=True, null=True)
    vaccine_type = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    date_of_proper_vaccination = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'vaccination'

#ИНЦИДЕНТ
class GIncident(models.Model):
    date_time = models.DateTimeField()
    type_call = models.DecimalField(max_digits=65535, decimal_places=65535)
    type_sess = models.DecimalField(max_digits=65535, decimal_places=65535)
    user_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    phone = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lang_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    category = models.ForeignKey(SCategory, models.DO_NOTHING)
    ratio = models.ForeignKey(SRatio, models.DO_NOTHING, blank=True, null=True)
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
    typedoc = models.ForeignKey(STypedoc, models.DO_NOTHING, blank=True, null=True)
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
    social_status = models.ForeignKey(SSocialStatus, models.DO_NOTHING, db_column='social_status', blank=True, null=True)
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
    lab_actv = models.ForeignKey(SLaborActivity, models.DO_NOTHING, blank=True, null=True)
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
    h_params = models.TextField(blank=True, null=True)  # This field type is a guess.
    village = models.CharField(max_length=255, blank=True, null=True)
    risk_group = models.ForeignKey(SRiskGroup, models.DO_NOTHING, db_column='risk_group', blank=True, null=True)
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

    class Meta:
        db_table = 'g_incident'

#
class GIncidentLog(models.Model):
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
    h_params = models.TextField(blank=True, null=True)  # This field type is a guess.
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
        db_table = 'g_incident_log'        

           