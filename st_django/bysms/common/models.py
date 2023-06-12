import datetime

from django.db import models
class Customer(models.Model):
    name = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

##药品
class Medicine(models.Model):
    # 药品名
    name = models.CharField(max_length=200)
    # 药品编号
    sn = models.CharField(max_length=200)
    # 描述
    desc = models.CharField(max_length=200)

class Order(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    create_data = models.DateTimeField(default=datetime.datetime.now)
    #外键：
        # On_delete:CASCADE-删除主记录和相对应的外键表记录
                   #PROTECT-如果order里面有cutomer对应的数据 那么进制删除cutomer
                   #SET_NULL-删除主键记录，将外键记录中的外键字段设置为null,该字段应当设置为允许为null
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    medicine = models.ManyToManyField(Medicine,through="OrderMedicine")
class OrderMedicine(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    medicine = models.ForeignKey(Medicine,on_delete=models.PROTECT)
    # 订单中的药品数量 #
    amount = models.PositiveIntegerField()
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.PositiveIntegerField()
    country = models.ForeignKey(Country,on_delete=models.PROTECT)
