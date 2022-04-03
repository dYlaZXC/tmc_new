from distutils.ccompiler import new_compiler
from multiprocessing.sharedctypes import Value
from posixpath import split
from tabnanny import check
from tkinter.tix import S_REGION
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.views.generic import TemplateView
from .models import *
from datetime import datetime, date
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import mixins, permissions
from random import randint
from rest_framework.decorators import (
    action,
    api_view,
    parser_classes,
    permission_classes,
)
from rest_framework.response import Response
from django.template.loader import render_to_string


class Card(APIView):
    def get(self, request, *args, **kwargs):
        # CONTEXT
        s_categories = SCategory.objects.all()
        s_ratios = SRatio.objects.all()
        s_regions = SRegion.objects.all()
        s_villages = SVillage.objects.all()
        s_streets = SStreet.objects.all()
        s_countries = SCountry.objects.all()
        s_riskgroups = SRiskGroup.objects.all()
        s_conditions = SCondition.objects.all()
        # END CONTEXT
        return render(request, 'card.html',
        {
            's_categories': s_categories,
            's_ratios': s_ratios,
            's_regions': s_regions,
            's_villages': s_villages,
            's_streets': s_streets,
            's_countries': s_countries,
            's_riskgroups': s_riskgroups,
            's_conditions': s_conditions,
        }) 


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def additional_form(request):
    return HttpResponse(render_to_string("modal_checklist.html"))

