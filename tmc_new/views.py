from django.utils.translation import gettext_lazy as _
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import url_has_allowed_host_and_scheme
from django.shortcuts import resolve_url
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from contextlib import nullcontext
from distutils.ccompiler import new_compiler
from math import nan
from multiprocessing.sharedctypes import Value
from posixpath import split
import re
from tabnanny import check
from tkinter import N
from tkinter.tix import S_REGION
from django import test
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.views.generic import TemplateView
from .models import *
from django.urls import reverse
from datetime import datetime, date, timedelta
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import mixins, permissions
from random import randint
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from rest_framework.decorators import (
    action,
    api_view,
    parser_classes,
    permission_classes,
)
from rest_framework.response import Response
from django.template.loader import render_to_string
import json
from django.core import serializers
from django.db.models import F
# from django.contrib.auth import logout as auth_logout, login as auth_login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
import math
""" PAGINATOR """
from tmc_new import utils 
from django.core.paginator import Paginator

statuses_end = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

""" БЛОК """
""" АВТОРИЗАЦИИ """

"""
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
.            return redirect('main')
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
"""


class SuccessURLAllowedHostsMixin:
    success_url_allowed_hosts = set()

    def get_success_url_allowed_hosts(self):
        return {self.request.get_host(), *self.success_url_allowed_hosts}


class LoginView(SuccessURLAllowedHostsMixin, FormView):
    """
    Display the login form and handle the login action.
    """
    form_class = AuthenticationForm
    authentication_form = None
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'login.html'
    redirect_authenticated_user = False
    extra_context = None

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            redirect_to = self.get_success_url()
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your LOGIN_REDIRECT_URL doesn't point to a login page."
                )
            return HttpResponseRedirect(redirect_to)
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or resolve_url('main')

    def get_redirect_url(self):
        """Return the user-originating redirect URL if it's safe."""
        redirect_to = self.request.POST.get(
            self.redirect_field_name,
            self.request.GET.get(self.redirect_field_name, '')
        )
        url_is_safe = url_has_allowed_host_and_scheme(
            url=redirect_to,
            allowed_hosts=self.get_success_url_allowed_hosts(),
            require_https=self.request.is_secure(),
        )
        return redirect_to if url_is_safe else ''

    def get_form_class(self):
        return self.authentication_form or self.form_class

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        context.update({
            self.redirect_field_name: self.get_redirect_url(),
            'site': current_site,
            'site_name': current_site.name,
            **(self.extra_context or {})
        })
        return context


class LogoutView(SuccessURLAllowedHostsMixin, TemplateView):
    """
    Log out the user and display the 'You are logged out' message.
    """
    next_page = None
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'registration/logged_out.html'
    extra_context = None

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        auth_logout(request)
        next_page = self.get_next_page()
        if next_page:
            # Redirect to this page until the session has been cleared.
            return HttpResponseRedirect(next_page)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Logout may be done via POST."""
        return self.get(request, *args, **kwargs)

    def get_next_page(self):

        LOGOUT_REDIRECT_URL = 'main'

        if self.next_page is not None:
            next_page = resolve_url(self.next_page)
        elif LOGOUT_REDIRECT_URL:
            next_page = resolve_url(LOGOUT_REDIRECT_URL)
        else:
            next_page = self.next_page

        if (self.redirect_field_name in self.request.POST or
                self.redirect_field_name in self.request.GET):
            next_page = self.request.POST.get(
                self.redirect_field_name,
                self.request.GET.get(self.redirect_field_name)
            )
            url_is_safe = url_has_allowed_host_and_scheme(
                url=next_page,
                allowed_hosts=self.get_success_url_allowed_hosts(),
                require_https=self.request.is_secure(),
            )
            # Security check -- Ensure the user-originating redirection URL is
            # safe.
            if not url_is_safe:
                next_page = self.request.path
        return next_page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        context.update({
            'site': current_site,
            'site_name': current_site.name,
            'title': _('Logged out'),
            **(self.extra_context or {})
        })
        return context


""" КОНЕЦ """
""" БЛОКА АВТОРИЗАЦИИ """



class Main(APIView):

    # DRY №1
    values_qs = ['id',
                'fio',
                'iin',
                'phone',
                'num_crossdoc',
                'date_start',
                'pmsp_name',
                'status',
                'dozvon',
                'dozvon_type',
                'pcr_result',
                'pcr_date_receipt',
                'patient_condition_start',
                'sign_observation_hospital',
                'incident_id'
    ]

    # DRY №2
    qs_add_on = [
                ['pmsp_name_format', 'pmsp_name'], # [НАИМЕНОВАНИЕ ФУНКЦИИ | СВОЙСТВО ОБЪЕКТА, АРГУМЕНТ ДЛЯ ФУНКЦИИ]
                ['date_start_format', 'date_start'],
                ['patient_condition_start_format','patient_condition_start'],
                ['pcr_date_receipt_main_format','pcr_date_receipt'],
                ['registration_date_time','incident_id'],
                ['dozvon_type_format','dozvon'],
                ['days_count','pcr_date_receipt']
    ]
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:

            # g_patients = GPatient.objects.filter(status_end__isnull=True).order_by('id')

            g_patients = GPatient.objects.filter(status_end__isnull=True).values(*(field for field in self.values_qs))

            for g_patient in g_patients:
                for qs_function, qs_value in self.qs_add_on:
                    function_ = getattr(utils, qs_function)
                    g_patient[qs_function] = function_(g_patient[qs_value])

            context = {
                'g_patients': g_patients
            }
            return render(request, 'main.html', context)
        else:
            return redirect('login')

    def post(self, request, *args, **kwargs):
        query = request.POST.get('query')
        
        g_patients = GPatient.objects.filter(
            status_end__isnull=True, fio__icontains=query).values(*(field for field in self.values_qs))
        if not g_patients:
            g_patients = GPatient.objects.filter(
                status_end__isnull=True, iin__icontains=query).values(*(field for field in self.values_qs))
            if not g_patients:
                g_patients = GPatient.objects.filter(
                    status_end__isnull=True, phone__icontains=query).values(*(field for field in self.values_qs))
                if not g_patients:
                        g_patients = GPatient.objects.filter(
                        status_end__isnull=True, id__icontains=query).values(*(field for field in self.values_qs))
        
        
        for g_patient in g_patients:
            for qs_function, qs_value in self.qs_add_on:
                function_ = getattr(utils, qs_function)
                g_patient[qs_function] = function_(g_patient[qs_value])
                
        context = {
            'g_patients': g_patients
        }
        return render(request, 'main.html', context)
        # return render(request, 'main_copy.html', context)

# MAIN GET 
# QS_ADD_ON 

# g_patient['pmsp_name_format'] =               pmsp_name_format(g_patient['pmsp_name'])
# g_patient['date_start_format'] =              g_patient_date_start_format( g_patient['date_start'])
# g_patient['patient_condition_start_format'] = patient_condition_start_format(g_patient['patient_condition_start'])
# g_patient['pcr_date_receipt_main_format'] =   pcr_date_receipt_main_format(g_patient['pcr_date_receipt'])
# g_patient['registration_date_time'] =         registration_date_time(g_patient['incident_id'])
# g_patient['dozvon_type_format'] =             dozvon_type_format(g_patient['dozvon'])
# g_patient['days_count'] =                     days_count(g_patient['pcr_date_receipt'])
                
# g_patient['last_record_datetime_format'] = last_record_datetime_format(g_patient['id'])





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

    def get(self, request, id, *args, **kwargs):
        date = datetime.now() + timedelta(hours=6)
        sore_throat = request.GET.get('sore_throat')
        nasal_congestion = request.GET.get('nasal_congestion')
        shortness_breath = request.GET.get('shortness_breath')
        vomiting = request.GET.get('vomiting')
        nausea = request.GET.get('nausea')
        diarrhea = request.GET.get('diarrhea')
        dry_cough = request.GET.get('dry_cough')
        palpitations = request.GET.get('palpitations')
        debility = request.GET.get('debility')
        headache = request.GET.get('headache')
        congestion_chest = request.GET.get('congestion_chest')
        anosmia = request.GET.get('anosmia')
        loss_taste = request.GET.get('loss_taste')
        cough_phlegm = request.GET.get('cough_phlegm')
        sweating = request.GET.get('sweating')
        dyspnea = request.GET.get('dyspnea')
        muscle_pain = request.GET.get('muscle_pain')
        joint_pain = request.GET.get('joint_pain')
        discharge_eyes_redness = request.GET.get('discharge_eyes_redness')
        rash = request.GET.get('rash')
        operator_id = request.GET.get('operator_id')
        temperature = request.GET.get('temperature')
        saturation = request.GET.get('saturation')
        wellbeing = request.GET.get('wellbeing')
        home_nabl = request.GET.get('home_nabl')
        vipoln_naznach = request.GET.get('vipoln_naznach')
        sostoyznie = request.GET.get('sostoyznie')
        narushen_karantin = request.GET.get('narushen_karantin')
        video_call = request.GET.get('video_call')
        jaloba_na_pmsp = request.GET.get('jaloba_na_pmsp')
        p_povtor_pcr = request.GET.get('p_povtor_pcr')
        p_go_street = request.GET.get('p_go_street')
        p_kt = request.GET.get('p_kt')
        p_n_naznachenie = request.GET.get('p_n_naznachenie')
        p_n_list = request.GET.get('p_n_list')
        p_n_raspiska = request.GET.get('p_n_raspiska')
        p_n_mb = request.GET.get('p_n_mb')
        p_n_call = request.GET.get('p_n_call')
        medical_taken = request.GET.get('medical_taken')
        violation_quar = request.GET.get('violation_quar')
        violation_descr = request.GET.get('violation_descr')
        f_send_mb = request.GET.get('f_send_mb')
        f_corect_ls = request.GET.get('f_corect_ls')
        f_repeat_call = request.GET.get('f_repeat_call')
        f_conf_dc = request.GET.get('f_conf_dc')
        f_other_comp_pmsp = request.GET.get('f_other_comp_pmsp')
        f_social_help = request.GET.get('f_social_help')
        snijenie_sluha = request.GET.get('snijenie_sluha')
        boli_v_jivote = request.GET.get('boli_v_jivote')
        onemenie = request.GET.get('onemenie')
        blagodarnost = request.GET.get('blagodarnost')
        f_primechanie = request.GET.get('f_primechanie')
        p_dk_end = request.GET.get('p_dk_end')
        p_gospt_ranee = request.GET.get('p_gospt_ranee')
        p_net_svyazi = request.GET.get('p_net_svyazi')
        p_error_data = request.GET.get('p_error_data')
        new_g_observation = GObservation(
            patient_id=id,
            date=date,
            sore_throat=sore_throat,
            nasal_congestion=nasal_congestion,
            shortness_breath=shortness_breath,
            vomiting=vomiting,
            nausea=nausea,
            diarrhea=diarrhea,
            dry_cough=dry_cough,
            palpitations=palpitations,
            debility=debility,
            headache=headache,
            congestion_chest=congestion_chest,
            anosmia=anosmia,
            loss_taste=loss_taste,
            cough_phlegm=cough_phlegm,
            sweating=sweating,
            dyspnea=dyspnea,
            muscle_pain=muscle_pain,
            joint_pain=joint_pain,
            discharge_eyes_redness=discharge_eyes_redness,
            rash=rash,
            operator_id=operator_id,
            temperature=temperature,
            saturation=saturation,
            wellbeing=wellbeing,
            home_nabl=home_nabl,
            vipoln_naznach=vipoln_naznach,
            sostoyznie=sostoyznie,
            narushen_karantin=narushen_karantin,
            video_call=video_call,
            jaloba_na_pmsp=jaloba_na_pmsp,
            p_povtor_pcr=p_povtor_pcr,
            p_go_street=p_go_street,
            p_kt=p_kt,
            p_n_naznachenie=p_n_naznachenie,
            p_n_list=p_n_list,
            p_n_raspiska=p_n_raspiska,
            p_n_mb=p_n_mb,
            p_n_call=p_n_call,
            medical_taken=medical_taken,
            violation_quar=violation_quar,
            violation_descr=violation_descr,
            f_send_mb=f_send_mb,
            f_corect_ls=f_corect_ls,
            f_repeat_call=f_repeat_call,
            f_conf_dc=f_conf_dc,
            f_other_comp_pmsp=f_other_comp_pmsp,
            f_social_help=f_social_help,
            f_primechanie=f_primechanie,
            snijenie_sluha=snijenie_sluha,
            boli_v_jivote=boli_v_jivote,
            onemenie=onemenie,
            blagodarnost=blagodarnost,
            p_dk_end=p_dk_end,
            p_gospt_ranee=p_gospt_ranee,
            p_net_svyazi=p_net_svyazi,
            p_error_data=p_error_data,
        )
        print('hello')
        new_g_observation.save()
        g_patient = GPatient.objects.get(id=id)
        g_patient.dozvon = 0
        g_patient.save()
        try:
            return HttpResponse({'success': 'true', 'id': new_g_observation.get('id')})
        except:
            return HttpResponse({'success': 'false'})


class CheckListJournalView(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            g_observations = GObservation.objects.filter(patient_id=id)
            response = serializers.serialize("json", g_observations)
            return JsonResponse(response, safe=False)
        except:
            response = ''
            return JsonResponse(response, safe=False)


# class CheckListCallsView(APIView):
#    def get(self, request, id, *args, **kwargs):
#            d_calling_list = DCallingList.objects.filter(patient_id=id)
#            response = serializers.serialize("json", d_calling_list)
#            print(response)
#            return JsonResponse(response, safe=False)


# class CheckListPatientsView(APIView):
#     def get(self, request, id, *args, **kwargs):
#         g_patients = GPatient.objects.filter(operator_id=id)
#         response = serializers.serialize("json", g_patients)
#         return JsonResponse(response, safe=False)


class Card_id(APIView):
    def get(self, request, id, *args, **kwargs):
        if request.user.is_authenticated:
            # CONTEXT
            g_patient = GPatient.objects.get(id=id)
            g_incident = GIncident.objects.get(id=g_patient.incident_id)
            g_observations = GObservation.objects.filter(patient_id=id)
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
                last_call = last_call = DCallingList.objects.filter(
                    patient_id=id).first().date_time
            except:
                last_call = ''
            # END CONTEXT
            return render(request, 'card_id.html',
                          {
                              'g_patient': g_patient,
                              'g_observations': g_observations,
                              'g_incident': g_incident,
                              's_regions': s_regions,
                              's_streets': s_streets,
                              # 's_villages': s_villages,
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

        fio = request.POST.get('fio')  # ФИО
        iin = request.POST.get('iin')  # ИИН
        is_rezident = request.POST.get('is_rezident')  # Резидент
        if is_rezident == 'on':
            is_rezident = True
        else:
            is_rezident = False

        birthday = request.POST.get('birthday') if request.POST.get(
            'birthday') != '' else None  # ДАТА РОЖДЕНИЯ
        sex = request.POST.get('sex') if request.POST.get(
            'sex') != '' else None  # ПОЛ
        s_country = request.POST.get('s_country') if request.POST.get(
            's_country') != '' else None  # ГРАЖДАНСТВО
        num_doc = request.POST.get('num_doc') if request.POST.get(
            'num_doc') != '' else None  # НОМЕР ДОКУМЕНТА
        s_region = request.POST.get('s_region') if request.POST.get(
            's_region') != '' else None  # РАЙОН
        s_village = request.POST.get('s_village') if request.POST.get(
            's_village') != '' else None  # ДЕРЕВНЯ
        s_street = request.POST.get('s_street') if request.POST.get(
            's_street') != '' else None  # УЛИЦА
        home = request.POST.get('home') if request.POST.get(
            'home') != '' else None  # НОМЕР ДОМА
        block = request.POST.get('block') if request.POST.get(
            'block') != '' else None  # НОМЕР БЛОКА
        kv = request.POST.get('kv') if request.POST.get(
            'kv') != '' else None  # НОМЕР КВАРТИРЫ
        date_vz = request.POST.get('date_vz') if request.POST.get(
            'date_vz') != '' else None  # ДАТА ВЗЯТИЯ
        time_vz = request.POST.get('time_vz') if request.POST.get(
            'time_vz') != '' else None  # ВРЕМЯ ВЗЯТИЯ
        pmsp = request.POST.get('pmsp') if request.POST.get(
            'pmsp') != '' else None  # ПМСП
        phone = request.POST.get('phone') if request.POST.get(
            'phone') != '' else None  # НОМЕР ТЕЛЕФОНА (МОБИЛЬНЫЙ)
        phone_home = request.POST.get('phone_home') if request.POST.get(
            'phone_home') != '' and request.POST.get('phone_home') != 'None' else None  # НОМЕР ТЕЛЕФОНА (ДОМАШНИЙ)
        additional_contacts = request.POST.get('additional_contacts') if request.POST.get(
            'additional_contacts') != '' else None  # ДОПОЛНИТЕЛЬНЫЕ КОНТАКТЫ
        info_for_tmc_agent = request.POST.get('info_for_tmc_agent') if request.POST.get(
            'info_for_tmc_agent') != '' else None  # ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ ДЛЯ СОТРУДНИКА ТМЦ
        result_of_end = request.POST.get('result_of_end') if request.POST.get(
            'result_of_end') != '' else None  # СТАТУС ПРИ СНЯТИИ С НАБЛЮДЕНИЯ
        date_of_end = request.POST.get('date_of_end') if request.POST.get(
            'date_of_end') != '' else None  # ДАТА СНЯТИЯ С НАБЛЮДЕНИЯ
        s_risk_group = request.POST.get('s_risk_group') if request.POST.get(
            's_risk_group') != '' else None  # ГРУППА РИСКА
        pmsp_ojirenie = request.POST.get('pmsp_ojirenie') if request.POST.get(
            'pmsp_ojirenie') != '' else None  # ОЖИРЕНИЕ ПМСП
        pmsp_serdce = request.POST.get('pmsp_serdce') if request.POST.get(
            'pmsp_serdce') != '' else None  # СЕРДЦЕ ПМСП
        pmsp_ag = request.POST.get('pmsp_ag') if request.POST.get(
            'pmsp_ag') != '' else None  # АРТЕРИАЛЬНАЯ ГИПЕРТЕНЗИЯ ПМСП
        pmsp_bronh = request.POST.get('pmsp_bronh') if request.POST.get(
            'pmsp_bronh') != '' else None  # БРОНХИАЛЬНАЯ АСТМА ПМСП
        pmsp_pechen = request.POST.get('pmsp_pechen') if request.POST.get(
            'pmsp_pechen') != '' else None  # БОЛЕЗНЬ ПЕЧЕНИ ПМСП
        pmsp_gemat = request.POST.get('pmsp_gemat') if request.POST.get(
            'pmsp_gemat') != '' else None  # ГЕМАТОЛОГИЧЕСКОЙ РАССТРОЙСТВО ПМСП
        pmsp_pochek = request.POST.get('pmsp_pochek') if request.POST.get(
            'pmsp_pochek') != '' else None  # БОЛЕЗНЬ ПОЧЕК ПМСП
        pmsp_onko = request.POST.get('pmsp_onko') if request.POST.get(
            'pmsp_onko') != '' else None  # ОНКОЛОГИЯ ПМСП
        pmsp_other_chronic = request.POST.get('pmsp_other_chronic') if request.POST.get(
            'pmsp_other_chronic') != '' else None  # ДРУГИЕ ХРОНИЧЕСКИЕ ЗАБОЛЕВАНИЯ ПМСП
        pmsp_pneumonia = request.POST.get('pmsp_pneumonia') if request.POST.get(
            'pmsp_pneumonia') != '' else None  # ПНЕВМОНИЯ ПМСП
        pmsp_diabetes = request.POST.get('pmsp_diabetes') if request.POST.get(
            'pmsp_diabetes') != '' else None  # САХАРНЫЙ ДИАБЕТ ПМСП
        pmsp_other_endo = request.POST.get('pmsp_other_endo') if request.POST.get(
            'pmsp_other_endo') != '' else None  # ДРУГИЕ ЭНДОКРИННЫЕ ЗАБОЛЕВАНИЯ ПМСП
        pmsp_hobl = request.POST.get('pmsp_hobl') if request.POST.get(
            'pmsp_hobl') != '' else None  # ХОБЛ ПМСП
        pregnancy = request.POST.get('pregnancy') if request.POST.get(
            'pregnancy') != '' else None  # БЕРЕМЕННОСТЬ ТРИМЕСТР
        detailed_diagnosis_info = request.POST.get('detailed_diagnosis_info') if request.POST.get(
            'detailed_diagnosis_info') != '' else None  # ПОДРОБНОЕ ОПИСАНИЕ ДИАГНОЗА
        nosologiya = request.POST.get('nosologiya') if request.POST.get(
            'nosologiya') != '' else None  # НОЗОЛОГИЯ
        diagnosis_monitoring = request.POST.get('diagnosis_monitoring') if request.POST.get(
            'diagnosis_monitoring') != '' else None  # ДИАГНОЗ НАБЛЮДЕНИЯ
        diagnosis_date = request.POST.get('diagnosis_date') if request.POST.get(
            'diagnosis_date') != '' else None  # ДИАГНОЗ НАБЛЮДЕНИЯ
        patient_condition = request.POST.get('patient_condition') if request.POST.get(
            'patient_condition') != '' else None  # СОСТОЯНИЕ ПАЦИЕНТА
        pmsp_start_date = request.POST.get('pmsp_start_date') if request.POST.get(
            'pmsp_start_date') != '' else None  # ДАТА ВЗЯТИЯ НА ДОМАШНЕЕ НАБЛЮДЕНИЕ
        sign_observation = request.POST.get('sign_observation') if request.POST.get(
            'sign_observation') != '' else None  # ПОСЛЕ СТАЦИОНАРА
        pneumonia = request.POST.get('pneumonia') if request.POST.get(
            'pneumonia') != '' else None  # ПНЕВМОНИЯ
        pcr_reason = request.POST.get('pcr_reason') if request.POST.get(
            'pcr_reason') != '' else None  # ПРИЧИНА СДАЧИ ПЦР
        pcr_result = request.POST.get('pcr_result') if request.POST.get(
            'pcr_result') != '' else None  # РЕЗУЛЬТАТ ПЦР
        pcr_test_date = request.POST.get('pcr_test_date') if request.POST.get(
            'pcr_test_date') != '' else None  # ДАТА СДАЧИ ПЦР ТЕСТА
        pcr_result_date = request.POST.get('pcr_result_date') if request.POST.get('pcr_result_date') != '' else None  # ДАТА ПОЛУЧЕНИЯ РЕЗУЛЬТАТА ПЦР
        kt_result = request.POST.get('kt_result') if request.POST.get('kt_result') != '' else None  # РЕЗУЛЬТАТ КТ
        kt_date = request.POST.get('kt_date') if request.POST.get('kt_date') != '' else None  # ДАТА КТ
        kt_result_diagnosis = request.POST.get('kt_result_diagnosis') if request.POST.get('kt_result_diagnosis') != '' else None  # РЕЗУЛЬТАТ ДИАГНОЗА КТ
        rentgen_result = request.POST.get('rentgen_result') if request.POST.get('rentgen_result') != '' else None  # РЕЗУЛЬТАТ
        rentgen_date = request.POST.get('rentgen_date') if request.POST.get('rentgen_date') != '' else None  # ДАТА РЕНТГЕНА
        rentgen_result_diagnosis = request.POST.get('rentgen_result_diagnosis') if request.POST.get('rentgen_result_diagnosis') != '' else None  # ЗАКЛЮЧЕНИЕ РЕНТГЕНА
        mb_date = request.POST.get('mb_date') if request.POST.get('mb_date') != '' else None  # ДАТА ВЫЕЗДА МБ
        late_reason = request.POST.get('late_reason') if request.POST.get('late_reason') != '' else None  # ПРИЧИНА ПОЗДНЕЙ ПОДАЧИ
        pmsp_info_datetime = request.POST.get('pmsp_info_datetime') if request.POST.get('pmsp_info_datetime') != '' else None  # ДАТА ПОЛУЧЕНИЯ ДАННЫХ ОТ ПМСП
        first_call_datetime = request.POST.get('first_call_datetitme') if request.POST.get('first_call_datetitme') != '' else None  # ДАТА ПЕРВОГО ЗВОНКА
        tmc_function_info = request.POST.get('tmc_function_info') if request.POST.get('tmc_function_info') != '' else None  # ИНФОРМИРОВАНИЕ О ФУНКЦИЯХ ТМЦ
        tmc_condition_info = request.POST.get('tmc_condition_info') if request.POST.get('tmc_condition_info') != '' else None  # ИНФОРМИРОВАНИЕ ОБ УСЛОВИЯХ ТМЦ
        refusal_hospitalize = request.POST.get('refusal_hospitalize') if request.POST.get('refusal_hospitalize') != '' else None  # ОТКАЗ ОТ ГОСПИТАЛИЗАЦИИ
        end_monitoring_patient = request.POST.get('end_monitoring_patient') if request.POST.get('end_monitoring_patient') != '' else None  # ЗАВЕРШЕНИЕ НАБЛЮДЕНИЯ СО СЛОВ ПАЦИЕНТА
        stationar = request.POST.get('stationar') if request.POST.get('stationar') != '' else None  # СТАЦИОНАР
        status_end_date = request.POST.get('status_end_date') if request.POST.get('status_end_date') != '' else None  # ДАТА ЗАВЕРШЕНИЯ НАБЛЮДЕНИЯ
        vaccine = request.POST.get('vaccine') if request.POST.get('vaccine') != '' else None  # ТИП ВАКЦИНЫ
        vaccine_doses = request.POST.get('vaccine_doses') if request.POST.get('vaccine_doses') != '' else None  # КОЛИЧЕСТВО ПОЛУЧЕННЫХ ДОЗ ВАКЦИНЫ
        vaccine_first_date = request.POST.get('vaccine_first_date') if request.POST.get('vaccine_first_date') != '' else None  # ДАТА ПОЛУЧЕНИЯ ПЕРВОЙ ДОЗЫ
        vaccine_second_date = request.POST.get('vaccine_second_date') if request.POST.get('vaccine_second_date') != '' else None  # ДАТА ПОЛУЧЕНИЯ ВТОРОЙ ДОЗЫ
        presc_therapy = request.POST.get('presc_therapy') if request.POST.get('presc_therapy') != '' else None  # Назначения
        complaint_ses = request.POST.get('complaint') if request.POST.get('complaint') != '' else None  # ЖАЛОБЫ СЭС
        complaint_days = request.POST.get('complaint_days') if request.POST.get('complaint_days') != '' else None  # ЖАЛОБЫ КОЛИЧЕСТВО ДНЕЙ
        other_simp = request.POST.get('nosologiya') if request.POST.get('nosologiya') != '' else None  # Нозология
        violation_descr = request.POST.get('violation_descr') if request.POST.get('violation_descr') != '' else None  # Жалобы на ПМСП
        dozvon = request.POST.get('dozvon')

        print('vaccine: ', vaccine)
        print('vaccine_doses: ', vaccine_doses)
        print('vaccine_first_date: ', vaccine_first_date)
        print('vaccine_second_date: ', vaccine_second_date)

        time_vz = time_vz if time_vz != None else '00:00'
        # END FORM DATA
        d_t = str(date_vz) + ' ' + str(time_vz)
        try:
            date_time = datetime.strptime(d_t, "%Y-%m-%d %H:%M")
        except:
            date_time = str(date_vz) + ' ' + str(time_vz)

        # SAVING TO MODEL (LOG)
        date_edit = datetime.now() + timedelta(hours=6)
        print(date_edit)
        g_patient = GPatient.objects.get(id=id)

        g_patient_log = GPatientLog.objects.create(
            id=g_patient.id,
            iin=g_patient.iin,
            fio=g_patient.fio,
            dozvon=g_patient.dozvon,
            status=g_patient.status,
            date_edit_log=date_edit,
            user_id_edit=request.user.id,
            num_crossdoc=g_patient.num_crossdoc,
            pmsp_name=g_patient.pmsp_name,
            phone=phone,
            status_end=g_patient.status_end,  # result_of_end,
            status_end_date=g_patient.status_end_date,  # date_of_end,
            incident_id=g_patient.incident_id,
            pcr_reason=g_patient.pcr_reason,
            pcr_result=g_patient.pcr_result,
            presc_therapy=presc_therapy,
            result_kt=g_patient.result_kt,
            pcr_date_test=g_patient.pcr_date_test,
            pcr_date_receipt=g_patient.pcr_date_receipt,
            kt_date=g_patient.kt_date,
            diagnosis_kt=g_patient.diagnosis_kt,
            xray=g_patient.xray,
            xray_date=g_patient.xray_date,
            xray_result=g_patient.xray_result,
            date_mobile_brigade=mb_date,
            d_comment=g_patient.d_comment,
            # late_reg_reason =late_reason , v logah netu takogo columna
            date_start=g_patient.date_start,
            date_end=g_patient.date_end,
            pmsp_start_date=g_patient.pmsp_start_date,
            info_function=True if tmc_function_info == 'on' else False,
            info_cond=True if tmc_condition_info == 'on' else False,
            hospitalize_tmc=True if refusal_hospitalize == 'on' else False,
            p_close_end_date=status_end_date,    # p_close_end_date <-- na samom dele eto
            watch_diagnosis=g_patient.watch_diagnosis,
            patient_condition_start=g_patient.patient_condition_start,
            sign_observation_hospital=g_patient.sign_observation_hospital,
            diagnosis_date=g_patient.diagnosis_date,
            complaint_ses=complaint_ses,
            d_feedback=complaint_days,
        )
        g_patient_log.save()

        g_incident = GIncident.objects.get(id=g_patient.incident_id)
        g_incident_log = GIncidentLog.objects.create(
            id=g_incident.id,
            resident=is_rezident,
            iin=g_incident.iin,
            fio=g_incident.fio,
            birthday=g_incident.birthday,
            sex=g_incident.sex,
            citizenship_id=g_incident.citizenship_id,
            num_crossdoc=g_incident.num_crossdoc,
            loc_region=g_incident.loc_region,
            village=g_incident.village,
            loc_street=g_incident.loc_street,
            loc_home=g_incident.loc_home,
            loc_block=g_incident.loc_block,
            loc_flat=g_incident.loc_flat,
            date_time=g_incident.date_time,
            pmsp_name=g_incident.pmsp_name,
            phone=phone,
            phone_contact_m=phone,
            phone_contact=phone_home,
            phone_other=additional_contacts,
            coment=info_for_tmc_agent,
            risk_group=g_incident.risk_group,
            ojirenie=g_incident.ojirenie,
            serdce=g_incident.serdce,
            hypertension=g_incident.hypertension,
            astma=g_incident.astma,
            pechen=g_incident.pechen,
            gema_rast=g_incident.gema_rast,
            pochki=g_incident.pochki,
            cancer=g_incident.cancer,
            h_oth_zabolev=g_incident.h_oth_zabolev,
            h_pnevmonia=g_incident.h_pnevmonia,
            h_sahar_diabet=g_incident.h_sahar_diabet,
            h_oth_endocrin=g_incident.h_oth_endocrin,
            h_hobl=g_incident.h_hobl,
            pregnancy=g_incident.pregnancy,
            type_call=2,
            type_sess=1,
            category_id=4,
            vaccine_type=vaccine,
            vaccine_date1=vaccine_first_date,
            vaccine_dose=vaccine_doses,
            vaccine_date2=vaccine_second_date,
            other_diagnos=detailed_diagnosis_info,
            date_edit=date_edit,
            user_edit=request.user.id,
            other_simp=other_simp,
            # date_time = pmsp_start_date,
        )
        g_incident_log.save()

        # g_patient.iin = iin
        # g_patient.num_crossdoc = num_doc
        # g_patient.pmsp_name = pmsp
        # g_patient.phone = phone
        g_patient.status_end = result_of_end
        g_patient.status_end_date = status_end_date  # ????????????
        # g_patient.pcr_reason = pcr_reason
        # g_patient.pcr_result = pcr_result
        # g_patient.result_kt = kt_result
        # g_patient.pcr_date_test = pcr_test_date
        # g_patient.pcr_date_receipt = pcr_result_date
        # g_patient.kt_date = kt_date
        # g_patient.diagnosis_kt = kt_result_diagnosis
        # g_patient.xray = rentgen_result
        # g_patient.xray_date = rentgen_date
        # g_patient.xray_result = rentgen_result_diagnosis
        g_patient.date_mobile_brigade = mb_date
        # g_patient.late_reg_reason =late_reason
        # g_patient.date_start = pmsp_info_datetime
        # g_patient.pmsp_start_date = pmsp_info_datetime
        g_patient.info_function = True if tmc_function_info == 'on' else False
        g_patient.info_cond = True if tmc_condition_info == 'on' else False
        g_patient.hospitalize_tmc = True if refusal_hospitalize == 'on' else False
        g_patient.status_end_date = date_of_end
        # g_patient.watch_diagnosis = g_patient.watch_diagnosis
        g_patient.presc_therapy = presc_therapy
        g_patient.complaint_ses = complaint_ses
        g_patient.d_feedback = complaint_days
        g_patient.d_comment = violation_descr

        g_patient.dozvon = dozvon
        # g_patient.patient_condition_start = patient_condition
        # g_patient.sign_observation_hospital =sign_observation
        # g_patient.diagnosis_date = diagnosis_date
        g_patient.save()

        # g_incident.rezident = is_rezident
        # g_incident.iin= iin
        # g_incident.birthday = birthday
        # g_incident.sex =sex
        # g_incident.citizenship_id = s_country
        # g_incident.num_crossdoc = num_doc
        # g_incident.loc_region = s_region
        # g_incident.village = s_village
        # g_incident.loc_street = s_street
        # g_incident.loc_home = home
        # g_incident.loc_block = block
        # g_incident.loc_flat = kv
        # g_incident.date_time = date_time
        # g_incident.pmsp_name = pmsp
        g_incident.phone = phone
        g_incident.phone_contact_m = phone
        g_incident.phone_contact = phone_home
        g_incident.phone_other = additional_contacts
        g_incident.coment = info_for_tmc_agent
        g_incident.other_simp = other_simp
        # g_incident.risk_group = s_risk_group

        # g_incident.ojirenie = True if pmsp_ojirenie == 'on' else False
        # g_incident.serdce = True if pmsp_serdce == 'on' else False
        # g_incident.hypertension = True if pmsp_ag == 'on' else False
        # g_incident.astma = True if pmsp_bronh == 'on' else False
        # g_incident.pechen = True if pmsp_pechen == 'on' else False
        # g_incident.gema_rast = True if pmsp_gemat == 'on' else False
        # g_incident.pochki = True if pmsp_pochek == 'on' else False
        # g_incident.cancer = True if pmsp_onko == 'on' else False
        # g_incident.h_oth_zabolev = True if pmsp_other_chronic == 'on' else False
        # g_incident.h_pnevmonia = True if pmsp_pneumonia == 'on' else False
        # g_incident.h_sahar_diabet = True if pmsp_diabetes == 'on' else False
        # g_incident.h_other_endocrin = True if pmsp_other_endo == 'on' else False
        # g_incident.h_hobl = True if pmsp_hobl == 'on' else False

        # g_incident.pregnancy = pregnancy
        g_incident.type_call = 2
        g_incident.type_sess = 1
        g_incident.category_id = 4
        g_incident.vaccine_type = vaccine
        g_incident.vaccine_date1 = vaccine_first_date
        g_incident.vaccine_dose = vaccine_doses
        g_incident.vaccine_date2 = vaccine_second_date
        g_incident.other_diagnos = detailed_diagnosis_info
        # g_incident.date_time = start_date
        g_incident.save()

        # END SAVING TO MODEL

        return redirect(request.META.get('HTTP_REFERER'))

        # return render(request, 'card_id.html',
        # {
        #     's_regions': s_regions,
        #     's_villages': s_villages,
        #     's_countries': s_countries,
        #     's_riskgroups': s_riskgroups,
        #     's_conditions': s_conditions,
        #     's_countries': s_countries,
        #     's_pmsps': s_pmsps,
        #     's_statuses_end': s_statuses_end,

        # })


def CountCalls(request, patient_id):
    try:
        g_patient = GPatient.objects.get(id=patient_id)
        g_patient.dozvon_type += 1
        g_patient.save()
        return JsonResponse({'result': 'success'})
    except TypeError:
        g_patient.dozvon_type = 1
        g_patient.save()
        return JsonResponse({'result': 'fail'})


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def additional_form(request, patient_id, checklist_id):
    g_observation = GObservation.objects.get(id=checklist_id)
    return HttpResponse(render_to_string("modal_checklist.html"), {'id': id})


def set_users(request):
    username_post = request.GET.get('username')
    password_post = request.GET.get('password')
    try:
        user = User()
        user.username = username_post
        user.set_password(password_post)
        user.save()
        return JsonResponse({'result': 'success'})
    except:
        return JsonResponse({'result': 'fail'})


def parse_users(request):
    s_operators = SOperators.objects.all()
    response = serializers.serialize('json', s_operators)
    return JsonResponse(response, safe=False)


def get_count(request):
    date_now = date.today()
    now = datetime.now()
    current_day = datetime(year=now.year, month=now.month,
                           day=now.day, hour=0, minute=0)
    gotten_g_patients = GPatient.objects.filter(status_end__isnull=True)
    gotten_list = []
    snyatten_list = []
    current_list = []
    for gotten_g_patient in gotten_g_patients:
        gotten_list.append(gotten_g_patient.incident_id)
    n_gotten_g_incidents = GIncident.objects.filter(id__in=gotten_list, date_time__gte=current_day + timedelta(
        hours=1), date_time__lte=current_day + timedelta(days=1, hours=1)).count()
    # gotten_g_patients = GPatient.objects.filter(
    #                                              status_end__isnull=True,
    #                                              pmsp_start_date__gte=current_day + timedelta(hours=1), pmsp_start_date__lte=current_day + timedelta(days=1, hours=1)).count()

    current_g_patients = GPatient.objects.filter(
        status_end__isnull=True).count()
    # for current_g_patient in current_g_patients:
    #    current_list.append(current_g_patient.incident_id)
    #n_current_g_incidents = GIncident.objects.filter(id__in=current_list, date_time__lt=current_day + timedelta(hours=1)).count()
    # current_g_patients = GPatient.objects.filter(status_end__isnull=True, pmsp_start_date__lt=date_now).count()
    snyatten_g_patients = GPatient.objects.exclude(status_end__isnull=True).filter(
        close_date_post__gte=current_day + timedelta(hours=1), close_date_post__lte=current_day + timedelta(days=1, hours=1)).count()
    # snyatten_g_patients = GPatient.objects.exclude(status_end__isnull=True)
    # for snyatten_g_patient in snyatten_g_patients:
    #     snyatten_list.append(snyatten_g_patient.incident_id)
    # n_snyatten_g_incidents = GIncident.objects.filter(id__in=snyatten_list).filter()
    return JsonResponse({'current_g_patients': current_g_patients,
                         'gotten_g_patients': n_gotten_g_incidents,
                         'snyatten_g_patients': snyatten_g_patients, }, safe=False)


def custom_serializer(a):
    """
    Handy creation of the Queryset fields
    And we exclude the fields that starts by '_' 
    which are Django internal references
    This will lead to the representation of the annotated fields
    that are generated by the QuerySert annotation
    which are ignored by serializers.serialize() function
    """
    return [{
        'model': a.model.__name__,
        'pk': k.pk,
        'fields': {
            i: j for i, j in k.__dict__.items() if not i.startswith('_')
        }
    } for k in a]


null = [None, '']


def save_log(request, name, bonus=''):

    # get_meta = lambda x, xx, y=exec("def f(meta,s):\n try:\n  return meta[s]\n except:  return None"): (x, xx)

    def get_meta(arr, key):
        try:
            return arr[key]
        except:
            return None

    request_data = {
        'QUERY_STRING': get_meta(request.META, "QUERY_STRING"),
        'RAW_URI': get_meta(request.META, "RAW_URI"),
        'HTTP_HOST': get_meta(request.META, "HTTP_HOST"),
        'HTTP_X_FORWARDED_FOR': get_meta(request.META, "HTTP_X_FORWARDED_FOR"),
        'HTTP_USER_AGENT': get_meta(request.META, "HTTP_USER_AGENT"),
        'HTTP_REFERER': get_meta(request.META, 'HTTP_REFERER')
    }

    user = request.data.get('user_fio')
    if request.user.is_authenticated:
        user = str(request.user)

    IncomingLogs.objects.create(
        name=name,
        description=str(bonus) + ' | ' + str(request_data),
        date_time=datetime.now() + timedelta(hours=6),
        username=user
    )


class get_s_pmsp(APIView):
    def post(self, request):
        all_pmsp = list(SPmsp.objects.all().values())
        save_log(request, 'get pmsp')
        return JsonResponse(all_pmsp, safe=False)


class get_s_region(APIView):
    def post(self, request):
        all_region = list(SRegion.objects.all().values())
        save_log(request, 'get region')
        return JsonResponse(all_region, safe=False)


class get_s_selo(APIView):
    def post(self, request):
        try:
            region_id = request.data.get('region_id')
            region = SRegion.objects.get(id=int(region_id))
            selos = list(SVillage.objects.filter(region=region).values())
            save_log(request, 'get region')
            return JsonResponse(selos, safe=False)
        except Exception as e:
            save_log(request, 'get region', 'error ' + str(e))
            return JsonResponse({'result': 'error', 'comment': str(e)})


class get_s_country(APIView):
    def post(self, request):
        save_log(request, 'get country')
        return JsonResponse(list(SCountry.objects.all().values()), safe=False)


class get_s_subtypecall(APIView):
    def post(self, request):
        save_log(request, 'get subtypecall')
        return JsonResponse(list(SSubtypeCall.objects.all().values()), safe=False)


class get_s_typecall(APIView):
    def post(self, request):
        save_log(request, 'get typecall')
        return JsonResponse(list(STypeCall.objects.all().values()), safe=False)


class get_s_appeal_status(APIView):
    def post(self, request):
        save_log(request, 'get appeal')
        return JsonResponse(list(SAppealStatus.objects.all().values()), safe=False)


class get_patient(APIView):
    def post(self, request):
        appeal = Appeal.objects.filter(phone=request.data.get('phone'))
        if appeal.count() > 0:
            save_log(request, 'get patient appeal ')
            return JsonResponse(list(appeal.values()), safe=False)
        else:
            save_log(request, 'get patient g_patient')
            patient = list(GPatient.objects.filter(
                phone=request.data.get('phone')).order_by('-id').values())
            return JsonResponse(patient, safe=False)


class get_patient_id(APIView):
    def post(self, request):
        save_log(request, 'get patient id')
        return JsonResponse(list(Appeal.objects.filter(id=request.data.get('id')).select_related('subtype_call').annotate(subtype_call_name=F('subtype_call__name')).values()), safe=False)


class get_incident(APIView):
    def post(self, request):
        save_log(request, 'get incident')
        incident = list(GIncident.objects.filter(
            id=request.data.get('incident_id')).values())
        return JsonResponse(incident, safe=False)


class save_appeal(APIView):

    def post(self, request):
        subtype_call = request.data.get('subtype_call')
        st_string = ''
        new_appeal = Appeal()
        #new_appeal.date = datetime.now() + timedelta(hours=6)

        # subtype
        try:
            if len(subtype_call) > 1:
                for st in subtype_call:
                    st_string += SSubtypeCall.objects.get(id=st).name + ' / '

                subtype_new = SSubtypeCall.objects.filter(
                    name__icontains=st_string)
                if subtype_new.count() == 0:
                    new_subtype = SSubtypeCall(name=st_string)
                    new_subtype.save()
                    new_appeal.subtype_call = new_subtype
                else:
                    new_appeal.subtype_call = subtype_new[0]
            elif len(subtype_call) == 1:
                new_appeal.subtype_call = SSubtypeCall.objects.get(
                    id=subtype_call[0])
        except:
            new_appeal.subtype_call = None

        # shift = request.data.get('shift')
        if request.data.get('shift') == 'День':
            shift = True
        elif request.data.get('shift') == 'Ночь':
            shift = False
        else:
            shift = None

        date = request.data.get('date') if request.data.get(
            'date') != None else datetime.now() + timedelta(hours=6)
        user_fio = request.data.get('user_fio')
        phone = '7' + request.data.get('phone')[1:]
        fio = request.data.get('fio')
        iin = request.data.get('iin') if request.data.get(
            'iin') not in null else None
        city = request.data.get('city')
        country = request.data.get('country')
        birthday = request.data.get('birthday')
        sex = request.data.get('sex')
        workplace = request.data.get('workplace')
        pmsp_name = request.data.get('pmsp')
        region = request.data.get('region')
        type_call = request.data.get('type_call')
        komu_peredano = request.data.get('komu')
        fio_actives = request.data.get('fio_actives')
        user_fio_alter = request.data.get('user_fio_alter')

        try:
            complaint_status = SAppealStatus.objects.get(
                id=request.data.get('complaint_status'))
        except:
            complaint_status = None

        reason = request.data.get('reason')
        complaint_result = request.data.get('complaint_result')
        status = None
        giid = request.data.get('giid')
        agent_id = request.data.get('agent_id')
        is_first = request.data.get('is_first')

        try:
            workplace_id = SWorkplace.objects.get(id=workplace)
        except:
            workplace_id = None

        try:
            type_call_id = STypeCall.objects.get(id=type_call)
        except:
            type_call_id = None

        try:
            region_id = SRegion.objects.get(id=region)
        except:
            region_id = None

        try:
            pmsp_name_id = SPmsp.objects.get(bin=pmsp_name)
        except:
            pmsp_name_id = None

        new_appeal.workplace = workplace_id
        new_appeal.user_fio = user_fio
        new_appeal.type_call = type_call_id
        new_appeal.status = status
        new_appeal.shift = shift
        new_appeal.sex = sex
        new_appeal.region = region_id
        new_appeal.reason = reason
        new_appeal.pmsp_name = pmsp_name_id
        new_appeal.phone = phone
        new_appeal.komu_peredano = komu_peredano
        new_appeal.iin = iin
        new_appeal.fio_actives = fio_actives
        new_appeal.fio = fio
        new_appeal.date = date
        new_appeal.complaint_status = complaint_status
        new_appeal.complaint_result = complaint_result
        new_appeal.birthday = birthday
        new_appeal.giid = giid
        new_appeal.agent_id = agent_id
        new_appeal.is_first = is_first
        new_appeal.user_fio_alter = user_fio_alter

        try:
            new_appeal.save()
        except:
            date = datetime.strptime(
                request.data.get('date'), '%d.%m.%Y, %H:%M:%S')
            new_appeal.date = date
            new_appeal.save()

        res = {
            'id': new_appeal.id,
            'shift': shift,
            'date': str(date),
            'user_fio': user_fio,
            'user_fio_alter': user_fio_alter,
            'phone': phone,
            'fio': fio,
            'iin': iin,
            'city': city,
            'country': country,
            'birthday': birthday,
            'sex': sex,
            'workplace': workplace,
            'pmsp_name': pmsp_name,
            'region': region,
            'type_call': type_call,
            'komu_peredano': komu_peredano,
            'fio_actives': fio_actives,
            'complaint_status': request.data.get('complaint_status'),
            'reason': reason,
            'complaint_result': complaint_result,
            'status': status
        }

        save_log(request, 'post save appeal', str(res))
        return JsonResponse(res)


class get_history(APIView):
    def post(self, request):

        res = Appeal.objects.filter(phone=request.data.get('phone')).select_related('type_call').annotate(type_call_name=F('type_call__name')
                                                                                                          ).select_related('subtype_call').annotate(subtype_call_name=F('subtype_call__name')
                                                                                                                                                    ).select_related('workplace').annotate(workplace_name=F('workplace__name')
                                                                                                                                                                                           ).select_related('pmsp_name').annotate(pmsp_name_name=F('pmsp_name__abrev_rus')
                                                                                                                                                                                                                                  ).select_related('complaint_status').annotate(complaint_status_name=F('complaint_status__name'))

        res_sz = custom_serializer(res)

        save_log(request, 'get history')

        return JsonResponse(res_sz, safe=False)


def check_group(name, user):
    if user is not None:
        for i in user.groups.all():
            if i.name == name:
                return True


class get_history_all_for_current_user(APIView):
    def post(self, request):
        try:
            user = User.objects.get(username=request.data.get('user_fio'))
        except:
            user = None

        # request.data.get('user_fio') == 'admin':
        if check_group('card_admin', user):
            return get_history_all().post(request)
        elif request.data.get('user_fio') == None:
            save_log(request, 'get history all', 'error user is None')
            return JsonResponse({'result': 'error auth'})
        elif request.data.get('user_fio') == '':
            save_log(request, 'get history all', 'error auth')
            return JsonResponse({'result': 'error auth'})

        res = Appeal.objects.filter(user_fio=request.data.get('user_fio'), is_first=True
                                    ).select_related('type_call').annotate(type_call_name=F('type_call__name')
                                                                           ).select_related('subtype_call').annotate(subtype_call_name=F('subtype_call')
                                                                                                                     ).select_related('workplace').annotate(workplace_name=F('workplace__name')
                                                                                                                                                            ).select_related('pmsp_name').annotate(pmsp_name_name=F('pmsp_name__abrev_rus')
                                                                                                                                                                                                   ).select_related('complaint_status').annotate(complaint_status_name=F('complaint_status__name'))

        res_sz = custom_serializer(res)
        return JsonResponse(res_sz, safe=False)


class get_history_all(APIView):
    def post(self, request):
        res = Appeal.objects.filter(is_first=True
                                    ).select_related('type_call').annotate(type_call_name=F('type_call__name')
                                                                           ).select_related('subtype_call').annotate(subtype_call_name=F('subtype_call')
                                                                                                                     ).select_related('workplace').annotate(workplace_name=F('workplace__name')
                                                                                                                                                            ).select_related('pmsp_name').annotate(pmsp_name_name=F('pmsp_name__abrev_rus')
                                                                                                                                                                                                   ).select_related('complaint_status').annotate(complaint_status_name=F('complaint_status__name'))

        res_sz = custom_serializer(res)
        save_log(request, 'get history all')
        return JsonResponse(res_sz, safe=False)


class api_auth(APIView):
    def post(self, request, *args, **kwargs):
        login = request.data.get('login')
        password = request.data.get('password')

        try:
            user = User.objects.get(username=login)
            if check_password(password, user.password):
                save_log(request, 'post api auth', 'user ok: ' + str(login))
                return JsonResponse({'result': 'ok'})
            else:
                save_log(request, 'post api auth',
                         'error wrong password: ' + str(login))
                return JsonResponse({'result': 'error', 'comment': 'wrong password'})
        except Exception as e:
            save_log(request, 'post api auth',
                     'error user not exist: ' + str(login))
            return JsonResponse({'result': 'error', 'comment': str(e)})


class ReportsView(APIView):
    def post(self, request, *args, **kwargs):

        if request.data.get('date_after') in null and request.data.get('date_before') in null:
            save_log(request, 'get reports view')

            try:
                user = User.objects.get(username=request.data.get('user_fio'))
                bb = BorcovskyBridge.objects.get(user=user)

                now = (datetime.now() - timedelta(hours=6)).date()
                calls = CallDetail.objects.using('tmc').filter(start_time__year=now.year, start_time__month=now.month, start_time__day=now.day
                                                               ).filter(caller_phone_type='EXTERNAL',
                                                                        callee_phone_type='INTERNAL',
                                                                        callee_login_id__isnull=False,
                                                                        callee_login_id=bb.agent_name)

                obshee = calls.count()
                prinyatie = calls.filter(talk_time__gt=0).count()
                ne_prinyatie = calls.filter(
                    talk_time=0, ivr_time__gt=0).count()
                return JsonResponse({
                    'obshee': obshee,
                    'prinyatie': prinyatie,
                    'ne_prinyatie': ne_prinyatie,
                })
            except Exception as e:
                save_log(request, 'get reports view', 'error: ' + str(e))
                return JsonResponse({
                    'obshee': 'Ошибка',
                    'prinyatie': 0,
                    'ne_prinyatie': 0,
                })

        else:
            try:
                user = User.objects.get(username=request.data.get('user_fio'))
            except:
                user = None
            if check_group('card_admin', user):
                # if request.user.groups.filter(name='card_admin').exists():
                save_log(request, 'post reports view')
                date_after = request.data.get('date_after')
                date_before = request.data.get('date_before')
                date_after_converted = datetime.strptime(
                    date_after, "%Y-%m-%d") - timedelta(hours=6)
                date_before_converted = datetime.strptime(
                    date_before, "%Y-%m-%d") - timedelta(hours=6)
                calls = CallDetail.objects.using('tmc').filter(start_time__gte=date_after_converted, start_time__lte=date_before_converted).filter(
                    caller_phone_type='EXTERNAL', callee_phone_type='INTERNAL', callee_login_id__isnull=False)
                obshee = calls.count()
                prinyatie = calls.filter(talk_time__gt=0).count()
                ne_prinyatie = calls.filter(
                    talk_time=0, ivr_time__gt=0).count()
                return JsonResponse({
                    'obshee': obshee,
                    'prinyatie': prinyatie,
                    'ne_prinyatie': ne_prinyatie,
                })
            else:
                save_log(request, 'post reports view', 'error not user')
                return JsonResponse({'error': 'user is None'})
