from django.http import JsonResponse
from django.db.models import F
from django.db import InternalError,transaction
from common.models import Order,OrderMedicine
import json


def listorder(request):
    qs=Order.objects.values()
    return JsonResponse({'ret':0,'retlist':list(qs)})

def addorder(request):
    newdata = request.params['data']
    name = newdata["name"]
    order = Order.objects.get(name)
    print("开始添加"+name)
    if order is not None:
        return JsonResponse({
            'ret':1,
            "msg": f'订单名`{name}`已经存在'
        })

    # 第一次插入成功第二次插入失败
    with transaction.atomic():
        new_order =  Order.objects.create(name=newdata['name'],customerid=newdata['customerid'],medicineids=newdata["medicineids"])
        batch = [OrderMedicine(order_id=new_order.id,medicine=mid,amount=1)for mid in newdata['medicineids']]
        OrderMedicine.objects.bulk_create(batch)



    return JsonResponse({'ret':0,'id':new_order.id})




def dispatcher(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
            'msg': '未登录',
            'redirect': '/mgr/sign.html'},
            status=302)
    if request.session['usertype'] != 'mgr':
        return JsonResponse({
            'ret': 302,
            'msg': '用户非mgr类型',
            'redirect': '/mgr/sign.html'},
            status=302)
    if request.method =='GET':
        request.params = request.GET
        # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST', 'PUT', 'DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)

        # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_order':
        return listorder(request)
    elif action == 'add_order':
        return addorder(request)

    # 订单 暂 不支持修改 和删除

    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})