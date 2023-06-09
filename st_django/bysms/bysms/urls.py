"""bysms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls.py import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls.py'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


# 导入对应的处理函数

# url路由入口
urlpatterns = [
    path('admin/', admin.site.urls),
    # 添加如下的路由记录
    path('sales/',include('sales.urls')),
    path('api/mgr/', include('mgr.urls')),
] + static("/",document_root='./z_dist')

