# HTTP请求的url路由
* url路由
* http请求处理
* ORM数据库操作
## 创建项目app

> 添加log功能：https://blog.csdn.net/lanyang123456/article/details/75175331#:~:text=Django%20%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8logging%E6%89%93%E5%8D%B0%E6%97%A5%E5%BF%97%201%20Logger%20%E7%94%A8%E6%88%B7%E4%BD%BF%E7%94%A8%E7%9A%84%E7%9B%B4%E6%8E%A5%E6%8E%A5%E5%8F%A3%EF%BC%8C%E5%B0%86%E6%97%A5%E5%BF%97%E4%BC%A0%E9%80%92%E7%BB%99Handler%202%20Handler,%E6%8E%A7%E5%88%B6%E6%97%A5%E5%BF%97%E8%BE%93%E5%87%BA%E5%88%B0%E5%93%AA%E9%87%8C%EF%BC%8Cconsole%EF%BC%8Cfile%E2%80%A6%20%E4%B8%80%E4%B8%AAlogger%E5%8F%AF%E4%BB%A5%E6%9C%89%E5%A4%9A%E4%B8%AAHandler%203%20Filter%20%E6%8E%A7%E5%88%B6%E5%93%AA%E4%BA%9B%E6%97%A5%E5%BF%97%E5%8F%AF%E4%BB%A5%E4%BB%8Elogger%E6%B5%81%E5%90%91Handler%204%20Formatter%20%E6%8E%A7%E5%88%B6%E6%97%A5%E5%BF%97%E7%9A%84%E6%A0%BC%E5%BC%8F

* django中一个app就是项目里面的一个应用的意思
  * 一个项目包含多个app
  * 每个app本质上是一个相对独立的模块
> 例子：1.把系统的管理员管理的功能  做成一个mgr的app里
>      2.把系统的销售员的操作     做成一个sales的app里

* 创建app可以通过执行命令，创建一个app目录，并在里面自动创建app常用的文件
```bash
python manage.py startapp sales
```
创建的目录文件：
sales/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
#### 启动服务
```angular2html
python manage.py runserver localhost:80
```
#### 创建项目app
1. 创建app项目
```angular2html
python manage.py startapp sales
```
2. 编写处理函数
* 在sales/目录下 修改view 文件
```angular2html
from django.http import HttpResponse

def listorders(request):
    return HttpResponse("下面是系统中所有的订单信息。。。")
```
* 在/bysms/urls.py 文件中修改url
```angular2html
from django.contrib import admin
from django.urls import path

# 别忘了导入 listorders 函数
from sales.views import listorders

urlpatterns = [
    path('admin/', admin.site.urls),

    # 添加如下的路由记录
    path('sales/orders/', listorders),
]
```
* 启动服务
* 访问 http://localhost:80/sales/orders/
只要修改url文件后，对应的主页小火箭页面就会消失

## 路由子表
* 通常业务比较多的情况下，可以按照app划分路由
例如：sales的请求服务：
1. 在sales目录下创建一个新的文件：sales\urls.py
```angular2html
from django.urls import path
from . import views
urlpatterns = [
    path('orders/',views.listorders)
]
```
2. 修改主url路由文件bysms/url.py 
```
from django.contrib import admin
from django.views import listrorders
utlpatterns = [
    path(" admin/",admin.site.urls),
    
    # 以sales开头的 都由子路由表进行路由
    include(是子路由)
    path('sales/',include('sales.urls')),
]
```
## 创建数据库的服务
* 设置bysms/setting.py
```pytnon
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
* 创建数据库
```angular2html
python manager.py migrate
```
#### ORM
表和数据像是 对象和实例
* Django中，定义了一个数据库的表，继承自django.db.models.Model类
* 字段，就是类里面的一些属性
* 类方法就是对表中数据的处理方法，数据进行增删改查

创建common的app，用来定义数据库
* model.py函数
```angular2html
from django.db import models
class Customer(models.Model):
  # 客户名称
    name = models.CharField(max_length=200)

    # 联系电话
    phonenumber = models.CharField(max_length=200)

    # 地址
    address = models.CharField(max_length=200)
```
#### 创建数据库表
在需要告诉Django 在common应用中 包含了model的定义
在setting.py中，INSTALLED_APPS配置项 加入如下的内容
```angular2html
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 加入下面这行
    'common.apps.CommonConfig',
]
```
* 在根目录执行
```angular2html
python manage.py makemigrations common
```
* 执行命令
```angular2html
python manage.py migrate
```
#### 管理数据
* Django 提供一个管理员界面可以方便添加、修改、删除定义的model表数据
* 首先创建一个管理员账号
```angular2html
python manage.py createsuperuser
Username (leave blank to use 'byhy'): byhy
Email address: byhy@163.com
Password:
Password (again):
Superuser created successfully.
```
* 配置文件 common/admin.py 注册定义的model类 
```angular2html
from django.contrib import admin
from .model import Customer
admin.site.register(Customer)
```
#### admin管理数据
* 提供一个操作页面方便添加、修改、删除定义的model表数据
1. 创建管理员用户
```angular2html
python manage.py createsuperuser
```
2. 配置文件common/admin.py 注册我们定义的model类
```angular2html
form django.contrib import admin
from .models import Customer
admin.site.register(Customer)
```
3. 访问’http://localhost/admin/‘，输入注册的用户密码登录
> 如果报表名不存在，可能是因为:django版本不符，查看便是
> https://blog.csdn.net/zhuyongru/article/details/99677313

** 设置中文的操作界面 **
1. 再setting.py 文件中配置MIDDLEWARE
2. admin界面语言本地化
```angular2html
django.middleware.locale.LocalMiddleware
```

## 读取数据库数据
* 写一个需求：浏览器访问sales/customers/。服务端就返回系统中素有客户记录给浏览器
* 需要返回数据库中customer表中所有记录，通过Customer类管理
1. 在sales/views.py中，定义一个listcustomers函数
```python
# 导入 Customer对象定义
from common.models import Customer
import Requser.HttpResponse
def listcustomers(requset):
    # 返回一个字典表对象
    # key 是字段名 value是字段值
    qs = Customer.objects.values()
    retStr = ''
    for customer in qs:
        for name,value in customer.items():
            retStr += f" {name}:{value}| "
        retStr = '<br>'
    return HttpResponse(retStr)
```

#### 设置筛选条件
* 可以使用filter方法加入过滤条件
```python
def listcustomers(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Customer.objects.values()

    # 检查url中是否有参数phonenumber
    ph =  request.GET.get('phonenumber',None)

    # 如果有，添加过滤条件
    if ph:
        qs = qs.filter(phonenumber=ph)

    # 定义返回字符串
    retStr = ''
    for customer in  qs:
        for name,value in customer.items():
            retStr += f'{name} : {value} | '
        # <br> 表示换行
        retStr += '<br>'

    return HttpResponse(retStr)
```
#### 前后端分离
* 其实可以python生成html模板 填写对应的数据进去
```python
# 定义html模板
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
```
```python
from django.template import engines
django_engine = engines['django']
tamplate = django_engine.from_string(html_tamplate)
def listcustomers(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Customer.objects.values()

    # 检查url中是否有参数phonenumber
    ph =  request.GET.get('phonenumber',None)

    # 如果有，添加过滤条件
    if ph:
        qs = qs.filter(phonenumber=ph)

    # 传入渲染模板需要的参数
    rendered = template.render({'customers':qs})

    return HttpResponse(rendered)
```
#### 列出用户
```agsl
def listcustomer(request):
    qs = Customer.objects.values()
    retlist = list(qs)
    return JsonResponse({'ret':0,'retlist' : retlist})
```
#### 添加用户
```python
def addcustomer(request):
    info = request.params['data']
    record = Customer.objects.create(
                        name=info['name'],
                        phonenumber=info['phonenumber'],
                        address =info['address'])
    return JsonResponse({'ret':0,'id':record.id})
```
* 使用postman发送 但是报错 CSRF verification failed整数错误认证
* Django缺省会启用CSRF(跨站请求伪造) 安全防护机制
  * 这种情况下，Post和Put类型的请求都必须在HTTP请求头中携带用于校验的数据
  * 需要取消CSRF的校验机制，bysms/settings.py中MIDDELEWARE配置项里注释‘django.middleware.csrf.CsrfViewMiddleware’
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```
打印错误栈，可以在setting中把debug 设置为true
#### 更新数据
```python
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
```
#### 删除数据
* 和更新一样，找到数据后添加删除操作
* customer.delete()

## 添加前端静态文件
* 前端静态文件打包成z_dist.zip
* 解压该文件到根目录上
* 在/bysms/urls.py文件，添加配置
```python
from django.contrib import admin

# 导入一个include函数
from django.urls import path, include

# 静态文件服务
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # 凡是 url 以 sales/  开头的，
    # 都根据 sales.urls 里面的 子路由表进行路由
    path('sales/', include('sales.urls')),

    # 凡是 url 以 api/mgr  开头的，
    # 都根据 mgr.urls 里面的 子路由表进行路由
    path('api/mgr/', include('mgr.urls')),

]  +  static("/", document_root="./z_dist")
```
就是在url路由中添加前端静态文件的查找路径

## 登录登出
- 创建mgr目录里的sign_in_out.py文件，用来管理管理员登入登出的API请求
- Django的内置app django.contrib.auth,缺省包含在项目installedAPP中，models定义了一张auth_user
```python
from django.http import JsonResponse

from django.contrib.auth import authenticate, login, logout

# 登录处理
def signin( request):
    # 从 HTTP POST 请求中获取用户名、密码参数
    userName = request.POST.get('username')
    passWord = request.POST.get('password')

    # 使用 Django auth 库里面的 方法校验用户名、密码
    user = authenticate(username=userName, password=passWord)
    
    # 如果能找到用户，并且密码正确
    if user is not None:
        if user.is_active:
            if user.is_superuser:
                login(request, user)
                # 在session中存入用户类型
                request.session['usertype'] = 'mgr'

                return JsonResponse({'ret': 0})
            else:
                return JsonResponse({'ret': 1, 'msg': '请使用管理员账户登录'})
        else:
            return JsonResponse({'ret': 0, 'msg': '用户已经被禁用'})
        
    # 否则就是用户名、密码有误
    else:
        return JsonResponse({'ret': 1, 'msg': '用户名或者密码错误'})


# 登出处理
def signout( request):
    # 使用登出方法
    logout(request)
    return JsonResponse({'ret': 0})
```

## session 机制 和cookie
#### session机制
* 服务器在数据库中保存一张session表，记录了一次用户登录的相关信息
  * 用户ID、姓名、登录名之类的
  * django中的表名为django_session
* 用户登录后，服务端就在数据库session表中，创建一条数据，创建一个新的session插入表中
* 然后在登录请求的HTTP响应信息中，头字段set-Cookie中填入sessionid数据
* 每次客户端发送请求，服务端只需查询是否有该sessionid的记录，如果不是拒绝服务

---
* 缺点：性能：用户比较多的时候，查询session表可能成为性能瓶颈；扩展；当服务部署在多个节点上时候，都要访问session表，多服务器查询影响性能
#### token机制
* 包含：数据信息和校验信息的数据包
---
* 服务器配置一个密钥，服务器私有的
* 用户登录成功后，服务端将用户信息数据+密钥一起进行一个哈希计算，得到哈希值
  * 数据信息+hash数值一起叫做一个字节串，token
  * 每次用户发送数据必须带上这个token数值，如果不知道密钥，用户修改了数据也会被拒绝访问
* 如果客户没有修改数据，服务器根据原来的数据+密钥 得到哈希值，和保存在原来的哈希值一直，就校验通过
