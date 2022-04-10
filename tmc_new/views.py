from asyncio.windows_events import NULL
from contextlib import nullcontext
from distutils.ccompiler import new_compiler
from math import nan
from multiprocessing.sharedctypes import Value
from posixpath import split
from tabnanny import check
from tkinter.tix import S_REGION
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.views.generic import TemplateView
from .models import *
from django.urls import reverse
from datetime import datetime, date
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import mixins, permissions
from random import randint
from django.template import loader
from rest_framework.decorators import (
    action,
    api_view,
    parser_classes,
    permission_classes,
)
from rest_framework.response import Response
from django.template.loader import render_to_string
from django.contrib.auth import logout as auth_logout, login as auth_login, authenticate


statuses_end = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

""" БЛОК """
""" АВТОРИЗАЦИИ """
class LoginView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):  
        username = request.POST.get('username')  
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print('НАШЕЛ')
            return redirect('main')
        else:
            print('НЕ НАШЕЛ')
            message = 'Неправильно указаны данные!'
            return render(request, 'login.html', {'message': message})            


class LogoutView(APIView):
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        template = loader.get_template('login.html')
        return HttpResponse(template.render())

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')  
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print('НАШЕЛ')
            return redirect('main')
        else:
            print('НЕ НАШЕЛ')
            message = 'Неправильно указаны данные!'
            return render(request, 'login.html', {'message': message})     

""" КОНЕЦ """
""" БЛОКА АВТОРИЗАЦИИ """



class Main(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            g_patients = GPatient.objects.filter(status_end__isnull=True)
            print(g_patients)
            return render(request, 'main.html', {
                'g_patients': g_patients,
            })
        else:
            return redirect('login')


class Card(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # CONTEXT
            s_regions = SRegion.objects.all()
            s_villages = SVillage.objects.all()
            s_countries = SCountry.objects.all()
            s_riskgroups = SRiskGroup.objects.all()
            s_conditions = SCondition.objects.all()
            s_countries = SCountry.objects.all()
            s_statuses_end = SStatusEnd.objects.all()
            s_pmsps = SPmsp.objects.all()
            # END CONTEXT
            return render(request, 'card.html',
            {
                's_regions': s_regions,
                's_villages': s_villages,
                's_countries': s_countries,
                's_riskgroups': s_riskgroups,
                's_conditions': s_conditions,
                's_countries': s_countries,
                's_pmsps': s_pmsps,
                's_statuses_end': s_statuses_end,
            })
        else:
            return redirect('login')     

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # CONTEXT
            s_regions = SRegion.objects.all()
            s_villages = SVillage.objects.all()
            s_countries = SCountry.objects.all()
            s_riskgroups = SRiskGroup.objects.all()
            s_conditions = SCondition.objects.all()
            s_countries = SCountry.objects.all()
            s_statuses_end = SStatusEnd.objects.all()
            s_pmsps = SPmsp.objects.all()
            # END CONTEXT
            # DATA MIGRATIONS

            # END DATA MIGRATIONS
            return render(request, 'card_id.html',
            {
                's_regions': s_regions,
                's_villages': s_villages,
                's_countries': s_countries,
                's_riskgroups': s_riskgroups,
                's_conditions': s_conditions,
                's_countries': s_countries,
                's_pmsps': s_pmsps,
                's_statuses_end': s_statuses_end,


            })
        else:
            return redirect('login')


class CheckListSaveView(APIView):
    def get(self, request):
        return 'pussy'

    def post(self, request, id, *args, **kwargs):
        try:
            return {'result': 'success'}
        except:
            return {'result': 'fail'}




class Card_id(APIView):
    def get(self, request, id, *args, **kwargs):
        if request.user.is_authenticated:
            # CONTEXT
            g_patient = GPatient.objects.get(id=id)
            print(g_patient.hospitalize_tmc)
            g_incident = GIncident.objects.get(id=g_patient.incident_id)
            print(g_incident.date_time)
            s_regions = SRegion.objects.all()
            s_villages = SVillage.objects.all()
            s_countries = SCountry.objects.all()
            s_riskgroups = SRiskGroup.objects.all()
            s_conditions = SCondition.objects.all()
            s_countries = SCountry.objects.all()
            s_statuses_end = SStatusEnd.objects.all()
            s_streets = SStreet.objects.all()
            s_pmsps = SPmsp.objects.all()
            s_late_regs = SLateReg.objects.all()
            s_vaccines = SVaccines.objects.all()
            try:
                last_call = last_call = DCallingList.objects.filter(patient_id=id).first().date_time
            except AttributeError:
                last_call = ''    
            # END CONTEXT
            return render(request, 'card_id.html',
            {
                'g_patient': g_patient,
                'g_incident': g_incident,
                's_regions': s_regions,
                's_streets': s_streets,
                's_villages': s_villages,
                's_countries': s_countries,
                's_riskgroups': s_riskgroups,
                's_conditions': s_conditions,
                's_countries': s_countries,
                's_pmsps': s_pmsps,
                's_statuses_end': s_statuses_end,
                's_late_regs': s_late_regs,
                's_vaccines': s_vaccines,
                'last_call': last_call,
            }) 
        else:
            return redirect('login')

    def post(self, request, id, *args, **kwargs):

        if request.user.is_authenticated:

            # CONTEXT
            s_regions = SRegion.objects.all()
            s_villages = SVillage.objects.all()
            s_countries = SCountry.objects.all()
            s_riskgroups = SRiskGroup.objects.all()
            s_conditions = SCondition.objects.all()
            s_countries = SCountry.objects.all()
            s_statuses_end = SStatusEnd.objects.all()
            s_pmsps = SPmsp.objects.all()
            # END CONTEXT

# ВСЁ ЧТО СВЯЗАНО СО STATUS_END - БЕРЕТСЯ И ЗАПИСЫВАЕТСЯ В G_PATIENT

            # FORM DATA
            fio = request.POST.get('fio') #ФИО
            birthday = request.POST.get('birthday') #ДАТА РОЖДЕНИЯ
            sex = request.POST.get('sex') #ПОЛ
            s_country = request.POST.get('s_country') #ГРАЖДАНСТВО
            num_doc = request.POST.get('num_doc') #НОМЕР ДОКУМЕНТА
            s_region = request.POST.get('s_region') #РАЙОН
            s_village = request.POST.get('s_village') #ДЕРЕВНЯ
            s_street = request.POST.get('s_street') #УЛИЦА
            home = request.POST.get('home') #НОМЕР ДОМА
            block = request.POST.get('block') #НОМЕР БЛОКА
            kv = request.POST.get('kv') #НОМЕР КВАРТИРЫ
            date_vz = request.POST.get('date_vz') #ДАТА ВЗЯТИЯ
            time_vz = request.POST.get('time_vz') #ВРЕМЯ ВЗЯТИЯ
            pmsp = request.POST.get('pmsp') #ПМСП
            phone = request.POST.get('phone') #НОМЕР ТЕЛЕФОНА (МОБИЛЬНЫЙ)
            phone_home = request.POST.get('phone_home') #НОМЕР ТЕЛЕФОНА (ДОМАШНИЙ)
            additional_contacts = request.POST.get('additional_contacts') #ДОПОЛНИТЕЛЬНЫЕ КОНТАКТЫ
            info_for_tmc_agent = request.POST.get('info_for_tmc_agent') #ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ ДЛЯ СОТРУДНИКА ТМЦ
            result_of_end = request.POST.get('result_of_end') #СТАТУС ПРИ СНЯТИИ С НАБЛЮДЕНИЯ
            date_of_end = request.POST.get('date_of_end') #ДАТА СНЯТИЯ С НАБЛЮДЕНИЯ
            s_risk_group = request.POST.get('s_risk_group') #ГРУППА РИСКА
            pmsp_ojirenie = request.POST.get('pmsp_ojirenie') #ОЖИРЕНИЕ ПМСП
            pmsp_serdce = request.POST.get('pmsp_serdce') #СЕРДЦЕ ПМСП
            pmsp_ag = request.POST.get('pmsp_ag') #АРТЕРИАЛЬНАЯ ГИПЕРТЕНЗИЯ ПМСП
            pmsp_bronh = request.POST.get('pmsp_bronh') #БРОНХИАЛЬНАЯ АСТМА ПМСП
            pmsp_pechen = request.POST.get('pmsp_pechen') #БОЛЕЗНЬ ПЕЧЕНИ ПМСП
            pmsp_gemat = request.POST.get('pmsp_gemat') #ГЕМАТОЛОГИЧЕСКОЙ РАССТРОЙСТВО ПМСП
            pmsp_pochek = request.POST.get('pmsp_pochek') #БОЛЕЗНЬ ПОЧЕК ПМСП
            pmsp_onko = request.POST.get('pmsp_onko') #ОНКОЛОГИЯ ПМСП
            pmsp_other_chronic =  request.POST.get('pmsp_other_chronic') #ДРУГИЕ ХРОНИЧЕСКИЕ ЗАБОЛЕВАНИЯ ПМСП
            pmsp_pneumonia = request.POST.get('pmsp_pneumonia') #ПНЕВМОНИЯ ПМСП
            pmsp_diabetes = request.POST.get('pmsp_diabetes') #САХАРНЫЙ ДИАБЕТ ПМСП
            pmsp_other_endo = request.POST.get('pmsp_other_endo') #ДРУГИЕ ЭНДОКРИННЫЕ ЗАБОЛЕВАНИЯ ПМСП
            pmsp_hobl = request.POST.get('pmsp_hobl') #ХОБЛ ПМСП
            pregnancy = request.POST.get('pregnancy') #БЕРЕМЕННОСТЬ ТРИМЕСТР
            detailed_diagnosis_info = request.POST.get('detailed_diagnosis_info') #ПОДРОБНОЕ ОПИСАНИЕ ДИАГНОЗА
            nosologiya = request.POST.get('nosologiya') #НОЗОЛОГИЯ
            diagnosis_monitoring = request.POST.get('diagnosis_monitoring') #ДИАГНОЗ НАБЛЮДЕНИЯ
            diagnosis_date = request.POST.get('diagnosis_date') #ДИАГНОЗ НАБЛЮДЕНИЯ
            patient_condition = request.POST.get('patient_condition') #СОСТОЯНИЕ ПАЦИЕНТА
            start_date = request.POST.get('start_date') #ДАТА ВЗЯТИЯ НА ДОМАШНЕЕ НАБЛЮДЕНИЕ
            sign_observation = request.POST.get('sign_observation') #ПОСЛЕ СТАЦИОНАРА
            pneumonia = request.POST.get('pneumonia') #ПНЕВМОНИЯ
            pcr_reason = request.POST.get('pcr_reason') #ПРИЧИНА СДАЧИ ПЦР
            pcr_result = request.POST.get('pcr_result') #РЕЗУЛЬТАТ ПЦР
            pcr_test_date = request.POST.get('pcr_test_date') #ДАТА СДАЧИ ПЦР ТЕСТА
            pcr_result_date = request.POST.get('pcr_result_date') #ДАТА ПОЛУЧЕНИЯ РЕЗУЛЬТАТА ПЦР
            kt_result = request.POST.get('kt_result') #РЕЗУЛЬТАТ КТ
            kt_date = request.POST.get('kt_date') #ДАТА КТ
            kt_result_diagnosis = request.POST.get('kt_result_diagnosis') #РЕЗУЛЬТАТ ДИАГНОЗА КТ
            rentgen_result = request.POST.get('rentgen_result') #РЕЗУЛЬТАТ
            rentgen_date = request.POST.get('rentgen_date') #ДАТА РЕНТГЕНА
            rentgen_result_diagnosis = request.POST.get('rentgen_result_diagnosis') #ЗАКЛЮЧЕНИЕ РЕНТГЕНА
            mb_date = request.POST.get('mb_date') #ДАТА ВЫЕЗДА МБ
            late_reason = request.POST.get('late_reason') #ПРИЧИНА ПОЗДНЕЙ ПОДАЧИ
            pmsp_info_datetime = request.POST.get('pmsp_info_datetime') #ДАТА ПОЛУЧЕНИЯ ДАННЫХ ОТ ПМСП
            first_call_datetime = request.POST.get('first_call_datetitme') #ДАТА ПЕРВОГО ЗВОНКА
            tmc_function_info = request.POST.get('tmc_function_info') #ИНФОРМИРОВАНИЕ О ФУНКЦИЯХ ТМЦ
            tmc_condition_info = request.POST.get('tmc_condition_info') #ИНФОРМИРОВАНИЕ ОБ УСЛОВИЯХ ТМЦ
            refusal_hospitalize = request.POST.get('refusal_hospitalize') #ОТКАЗ ОТ ГОСПИТАЛИЗАЦИИ 
            end_monitoring_patient = request.POST.get('end_monitoring_patient') #ЗАВЕРШЕНИЕ НАБЛЮДЕНИЯ СО СЛОВ ПАЦИЕНТА
            stationar = request.POST.get('stationar') #СТАЦИОНАР
            status_end_date = request.POST.get('status_end_date') #ДАТА ЗАВЕРШЕНИЯ НАБЛЮДЕНИЯ
            vaccine = request.POST.get('vaccine') #ТИП ВАКЦИНЫ
            vaccine_doses = request.POST.get('vaccine_doses') #КОЛИЧЕСТВО ПОЛУЧЕННЫХ ДОЗ ВАКЦИНЫ
            vaccine_first_date = request.POST.get('vaccine_first_date') #ДАТА ПОЛУЧЕНИЯ ПЕРВОЙ ДОЗЫ
            vaccine_second_date = request.POST.get('vaccine_second_date') #ДАТА ПОЛУЧЕНИЯ ВТОРОЙ ДОЗЫ
            # END FORM DATA

            # SAVING TO MODEL (LOG)
            g_patient = GPatient.objects.get(patientid=id)
            # END SAVING TO MODEL

            return render(request, 'card_id.html',
            {
                's_regions': s_regions,
                's_villages': s_villages,
                's_countries': s_countries,
                's_riskgroups': s_riskgroups,
                's_conditions': s_conditions,
                's_countries': s_countries,
                's_pmsps': s_pmsps,
                's_statuses_end': s_statuses_end,
                
            })
        else:
            return redirect('login')




@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def additional_form(request, id):

    return HttpResponse(render_to_string("modal_checklist.html"), {'id': id})


