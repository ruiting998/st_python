from django.http import JsonResponse
import json
import logging
from common.models import Customer
logger = logging.getLogger("django")


def dispatcher(request):
    if request.method == 'GET':
        request.params=request.GET
    elif request.method in ['POST','PUT','DELETE']:
        request.params = json.loads(request.body)

    action = request.params['action']
    if action == 'list_customer':
        return listcustomer(request)
    elif action == 'add_customer':
        return addcustomer(request)
    elif action == 'modify_customer':
        return modifycustomer(request)
    elif action == 'del_customer':
        return deletecustomer(request)
    else:
        return JsonResponse({'ret':1,'msg':"不支持该类型请求"})

def addcustomer(request):
    pass
def modifycustomer(request):
    pass
def deletecustomer(request):
    pass
# Create your views here.
def listcustomer(request):

    print("一个萌萌的请求过来了。。。。")
    qs = Customer.objects.values()
    retlist = list(qs)
    logger.debug(retlist)
    return JsonResponse({'ret':0,'retlist' : retlist})