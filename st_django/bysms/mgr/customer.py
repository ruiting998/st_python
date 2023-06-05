from django.http import JsonResponse
import json

from mgr.views import listcustomer,addcustomer, modifycustomer, deletecustomer




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
            return JsonResponse({'ret':1,'msg':'不支持该类型请求'})