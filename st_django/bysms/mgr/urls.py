from django.urls import path

from common import views
from mgr import customer

urlpatterns = [
    path('customers', customer.dispatcher),
]