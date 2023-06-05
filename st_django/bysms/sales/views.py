from django.shortcuts import render
# #############################通常用与处理http请求的代码############################################## #
# Create your views here.

# ##############设计################ #
# 1。1. 凡是浏览器访问的http请求的url地址是/sales/orders/ 就是由views.py里面的函数listorders来处理，返回一段字符串给浏览器

# ################################# #

# ####1.1#### #
from django.http import HttpResponse

# 用来处理requset 请求里对应的函数
def listorders(request):
    return HttpResponse("下面是系统中所有的订单信息...")

# ##############注意################### #
# * 后端程序处理请求 都是根据HttpRequests对象中获取
# *
# #################################### #