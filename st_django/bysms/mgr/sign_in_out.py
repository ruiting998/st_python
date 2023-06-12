from django.http import JsonResponse
from django.contrib.auth import  authenticate,login,logout

def signin(requset):
    username = requset.POST.get('username')
    password  = requset.POST.get('password')
    #校验
    user = authenticate(username = username,password=password)
    if user is not None:
        # 是否可用
        if user.is_active:
            login(requset,user)
            #在session中存储用户类型
            requset.session['usertype']='mgr'
            return JsonResponse({'ret':0,'msg':'登录成功'})
        else:
            return JsonResponse({'ret':1,'msg':'用户已经被禁用'})
    # 用户名、密码有误
    else:
        return JsonResponse({'ret':1,'msg':'用户名或者密码错误'})

# 登出操作
def signout(requset):
    # 使用登出方法
    logout(requset)
    return JsonResponse({'ret':0})
