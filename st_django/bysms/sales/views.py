from django.shortcuts import render
# #############################通常用与处理http请求的代码############################################## #
# Create your views here.

# ##############设计################ #
# 1。1. 凡是浏览器访问的http请求的url地址是/sales/orders/ 就是由views.py里面的函数listorders来处理，返回一段字符串给浏览器

# ################################# #

# ####1.1#### #
from django.http import HttpResponse
from common.models import Customer



# 用来处理requset 请求里对应的函数
def listorders(request):
    return HttpResponse("下面是系统中所有的订单信息...")

# ####2.1#### #
# ##前后端分离# #
html_template ='''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
table {
    border-collapse: collapse;
}
th, td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
</style>
</head>
    <body>
        <table>
        <tr>
        <th>id</th>
        <th>姓名</th>
        <th>电话号码</th>
        <th>地址</th>
        </tr>

        {% for customer.py in customers %}
            <tr>
            
            {% for name, value in customer.py.items %}    
                    
                <td>{{ value }}</td>            
            {% endfor %}
            
            </tr>
        {% endfor %}
                
        </table>
    </body>
</html>
'''

from django.template import  engines
django_engine =  engines['django']
template = django_engine.from_string(html_template)

# 获取所有的customers
def listcustomers(requese):
    qs = Customer.objects.values()

    qh = requese.GET.get('phonenumber',None)
    if qh:
        qs = qs.filter(phonenumber=qh)

    rendered = template.render({'customers':qs})
    return HttpResponse(rendered)

# ##############注意################### #
# * 后端程序处理请求 都是根据HttpRequests对象中获取
# *
# #################################### #