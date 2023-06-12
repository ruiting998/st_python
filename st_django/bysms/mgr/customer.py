from django.http import JsonResponse
from django.http import HttpResponse
import json
import logging
from common.models import Customer

logger = logging.getLogger("django")


def dispatcher(request):
    ## 判断session用户是否符合登陆的管理员用户
    if "usertype" not in request.session:
        return JsonResponse({
            'ret':302,
            'msg':'未登录',
            'redict':'/mgr/sign.html'},status=302)
    if request.session['usertype']!='mgr':
        return JsonResponse({
            'ret': 302,
            'msg': '用户非mgr类型',
            'redirect': '/mgr/sign.html'},
            status=302)


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
    print("创建用户...")
    info = request.params['data']
    record = Customer.objects.create(
                        name=info['name'],
                        phonenumber=info['phonenumber'],
                        address =info['address'])
    return JsonResponse({'ret':0,'id':record.id})
def modifycustomer(request):
    print("修改用户...")
    customerid=request.params['id']
    newdata = request.params['newdata']

    try:
        # 根据id查找对应的客户记录
        customer = Customer.objects.get(id=customerid)
        # customer = Customer.objects.filter(id=customerid)
    except Customer.DoesNotExist:
        return JsonResponse({
            'ret':1,
            'msg':f'id `{customerid}`的客户不存在'
        })
    if 'name' in newdata:
        customer.name = newdata['name']
    if 'phonenumber' in newdata:
        customer.phonenumber = newdata['phonenumber']
    if 'address' in newdata:
        customer.address = newdata['address']

    # 修改数据后要保存在数据库中
    customer.save()
    return JsonResponse({'ret':0,'msg':'用户修改成功'})

def deletecustomer(request):
    print("删除用户...")
    customerid=request.params['id']
    try:
        customer = Customer.objects.get(id=customerid)
    except Customer.DoesNotExist:
        return JsonResponse(
            {
                'ret':1,
                'msg': f'id 为`{customerid}`的客户不存在'
            }
        )
    #从数据库中删除对应的记录
    customer.delete()
    return JsonResponse({'ret':0,'msg':'数据已经删除'})
# Create your views here.
def listcustomer(request):

    print("一个萌萌的请求过来了。。。。")
    qs = Customer.objects.values()
    retlist = list(qs)
    logger.debug(retlist)
    return JsonResponse({'ret':0,'retlist' : retlist})