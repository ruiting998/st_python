# HTTP请求的url路由
* url路由
* http请求处理
* ORM数据库操作
## 创建项目app

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