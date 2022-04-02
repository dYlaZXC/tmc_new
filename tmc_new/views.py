from distutils.ccompiler import new_compiler
from multiprocessing.sharedctypes import Value
from posixpath import split
from tabnanny import check
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
        
        return render(request, 'card.html') 


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def additional_form(request):
    return HttpResponse(render_to_string("modal_checklist.html"))

