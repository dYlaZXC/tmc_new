from datetime import date, datetime
from tmc_new.models import (
    SPmsp,
    SCondition,
    GObservation,
    GIncident
)

DOZVON_MODEL_TYPE_CHOICES = [
    (0, ''),
    (1, 'Занят'),
    (2, 'Не отвечает'),
    (3, 'Неверный номер'),
    (4, 'Номер другого человека'),
]

def pmsp_name_format(pmsp_name):
        try:
            name = SPmsp.objects.get(bin=str(pmsp_name))
            return name.abrev_rus
        except:
            return pmsp_name    

def date_start_format(date_start):
        if date_start is not None:
            day = str(date_start.day) if date_start.day > 9 else '0' + str(date_start.day)
            month = str(date_start.month) if date_start.month > 9 else '0' + str(date_start.month)
            year = date_start.year
            return str(day) + '.' + str(month) + '.' + str(year)
        else:
            return date_start

def patient_condition_start_format(patient_condition_start):
        try:
            condition = SCondition.objects.get(id=patient_condition_start).name_ru
            return condition
        except SCondition.DoesNotExist:
            return 'Неизвестно'



def pcr_date_receipt_main_format(pcr_date_receipt):
        if pcr_date_receipt is not None:
            day = str(pcr_date_receipt.day) if pcr_date_receipt.day > 9 else '0' + str(pcr_date_receipt.day)
            month = str(pcr_date_receipt.month) if pcr_date_receipt.month > 9 else '0' + str(pcr_date_receipt.month)
            year = str(pcr_date_receipt.year)
            return day + '.' + month + '.' + year
        else:
            return pcr_date_receipt


def registration_date_time(incident_id):
        try:
            date_time = GIncident.objects.get(id=incident_id).date_time
        except GIncident.DoesNotExist:
            return 'Неизвестно'
        try:
            year = str(date_time.year)
            month = str(date_time.month) if date_time.month > 9 else '0' + str(date_time.month)
            day = str(date_time.day) if date_time.day > 9 else '0' + str(date_time.day)
            hour = str(date_time.hour) if date_time.hour > 9 else '0' + str(date_time.hour)
            minute = str(date_time.minute) if date_time.minute > 9 else '0' + str(date_time.minute)
            return day + '.' + month + '.' + year + ' ' + hour + ':' + minute
        except:
            return date_time   


def last_record_datetime_format(id):
        try:
            observ = GObservation.objects.filter(patient_id=id).order_by('-date').first()
            date = observ.date
            year = str(date.year)
            month = str(date.month) if date.month > 9 else '0' + str(date.month)
            day = str(date.day) if date.day > 9 else '0' + str(date.day)
            hour = str(date.hour) if date.hour > 9 else '0' + str(date.hour)
            minute = str(date.minute) if date.minute > 9 else '0' + str(date.minute)
            return day + '.' + month + '.' + year + ' ' + hour + ':' + minute
        except:
            return 'Не найдено'


def dozvon_type_format(dozvon):
        for key, value in DOZVON_MODEL_TYPE_CHOICES:
            if key == dozvon:
                return value
    
def days_count(pcr_date_receipt):
    if pcr_date_receipt is not None:
        return (date.today() - pcr_date_receipt.date()).days 
    else:
        return ''
