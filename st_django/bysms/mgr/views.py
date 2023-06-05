from django.http import JsonResponse
from django.shortcuts import render

from common.models import Customer


def addcustomer(request):
    pass
def modifycustomer(request):
    pass
def deletecustomer(request):
    pass
# Create your views here.
def listcustomer(request):
    qs = Customer.objects.values()
    retlist = list(qs)
    return JsonResponse({'ret' : 0,'retlist' : retlist})