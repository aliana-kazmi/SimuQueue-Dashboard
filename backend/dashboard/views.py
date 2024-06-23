from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers

from generate.models import Simulator_Data

def dashboard(request):
    return render(request, 'dashboard.html', {})

def data_display(request):
    return render(request, 'datatables.html' )