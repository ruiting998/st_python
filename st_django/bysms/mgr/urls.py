from django.urls import path

from common import views
from mgr import customer,order, sign_in_out, medicine

urlpatterns = [
    path('customers', customer.dispatcher),
    path('medicines', medicine.dispatcher),  # 加上这行
    path('orders',order.dispatcher),
    path('signin', sign_in_out.signin),
    path('signout', sign_in_out.signout),

]