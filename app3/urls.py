from app3.views import *
from django.urls import path
app_name='bus'
urlpatterns=[
    path('redbus/',redbus,name='redbus'),
    path('yellowbus/',yellowbus,name='yellowbus'),
]