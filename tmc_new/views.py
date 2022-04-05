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
        
        return 'PUSSY'


class Card_id(APIView):
    def get(self, request, id, *args, **kwargs):
        if request.user.is_authenticated:
            # CONTEXT
            g_patient = GPatient.objects.filter(id=id)
            s_regions = SRegion.objects.all()
            s_villages = SVillage.objects.all()
            s_countries = SCountry.objects.all()
            s_riskgroups = SRiskGroup.objects.all()
            s_conditions = SCondition.objects.all()
            s_countries = SCountry.objects.all()
            s_statuses_end = SStatusEnd.objects.all()
            s_pmsps = SPmsp.objects.all()
            # END CONTEXT
            return render(request, 'card_id.html',
            {
                'g_patient': g_patient,
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
        
        return 'PUSSY'



@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def additional_form(request):
    return HttpResponse(render_to_string("modal_checklist.html"))


