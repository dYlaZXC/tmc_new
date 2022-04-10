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
# from django.contrib.auth import logout as auth_logout, login as auth_login, authenticate


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
"""

from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.shortcuts import resolve_url
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib.sites.shortcuts import get_current_site
from django.utils.translation import gettext_lazy as _


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

        LOGOUT_REDIRECT_URL='main'

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
        iin = request.POST.get('iin') #ИИН 
        is_rezident = request.POST.get('is_rezident')# Резидент
        if is_rezident == 'on':
            is_rezident = True
        else:
            is_rezident = False
            
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
        presc_therapy =request.POST.get('presc_therapy') # Назначения







        # END FORM DATA
        d_t = str(date_vz) + ' ' + str(time_vz)
        date_time = datetime.strptime(d_t, "%Y-%m-%d %H:%M")

        # SAVING TO MODEL (LOG)

        g_patient = GPatient.objects.get(id=id)
        g_patient_log = GPatientLog(
            iin = iin,
            num_crossdoc = num_doc,
            pmsp_name = pmsp,
            phone = phone,
            status_end = result_of_end,
            status_end_date = date_of_end,
            pcr_reason = pcr_reason,
            pcr_result = pcr_result,
            result_kt = kt_result,
            
        )
        g_patient_log.save()

        g_incident = GIncident.objects.get(id=g_patient.incident_id)
        g_incident_log = GIncidentLog(
            resident = is_rezident,
            iin= iin,
            birthday = birthday,
            sex =sex,
            citizenship_id = s_country,
            num_crossdoc = num_doc,
            loc_region = s_region,
            village = s_village,
            loc_street = s_street,
            loc_home = home,
            loc_block = block,
            loc_flat = kv,
            date_time = date_time,
            pmsp_name = pmsp,
            phone = phone,
            phone_contact_m = phone, 
            phone_contact = phone_home,
            phone_other = additional_contacts,
            coment = info_for_tmc_agent,
            risk_group = s_risk_group,
            ojirenie = pmsp_ojirenie,
            serdce = pmsp_serdce,
            hypertension = pmsp_ag,    
            astma = pmsp_bronh,
            pechen = pmsp_pechen,
            gema_rast = pmsp_gemat,
            pochki = pmsp_pochek,
            cancer = pmsp_onko,
            h_oth_zabolev = pmsp_other_chronic,
            h_pnevmonia = pmsp_pneumonia,
            h_sahar_diabet = pmsp_diabetes,
            h_oth_endocrin = pmsp_other_endo,
            h_hobl = pmsp_hobl,
            pregnancy = pregnancy,
            type_call = 2,
            type_sess = 1,
            category_id = 4,
        )
        g_incident_log.save()

        g_patient.iin = iin
        g_patient.num_crossdoc = num_doc
        g_patient.pmsp_name = pmsp
        g_patient.phone = phone
        g_patient.status_end = result_of_end
        g_patient.status_end_date = date_of_end
        g_patient.save()
        
        g_incident.rezident = is_rezident
        g_incident.iin= iin
        g_incident.birthday = birthday
        g_incident.sex =sex
        g_incident.citizenship_id = s_country
        g_incident.num_crossdoc = num_doc
        g_incident.loc_region = s_region
        g_incident.village = s_village
        g_incident.loc_street = s_street
        g_incident.loc_home = home
        g_incident.loc_block = block
        g_incident.loc_flat = kv
        g_incident.date_time = date_time
        g_incident.pmsp_name = pmsp
        g_incident.phone = phone
        g_incident.phone_contact_m = phone
        g_incident.phone_contact = phone_home
        g_incident.phone_other = additional_contacts
        g_incident.coment = info_for_tmc_agent
        g_incident.risk_group = s_risk_group
        g_incident.ojirenie = pmsp_ojirenie
        g_incident.serdce = pmsp_serdce
        g_incident.hypertension = pmsp_ag
        g_incident.astma = pmsp_bronh
        g_incident.pechen = pmsp_pechen
        g_incident.gema_rast = pmsp_gemat
        g_incident.pochki = pmsp_pochek
        g_incident.cancer = pmsp_onko
        g_incident.h_oth_zabolev = pmsp_other_chronic
        g_incident.h_pnevmonia = pmsp_pneumonia
        g_incident.h_sahar_diabet = pmsp_diabetes
        g_incident.h_other_endocrin = pmsp_other_endo
        g_incident.h_hobl = pmsp_hobl
        g_incident.pregnancy = pregnancy
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




@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def additional_form(request, id):

    return HttpResponse(render_to_string("modal_checklist.html"), {'id': id})


