# 注册定义的model类
from django.contrib import admin

from .models import Customer

admin.site.register(Customer)
# Register your models here.
