from app2.views import *
from django.urls import path
app_name='rcb'
urlpatterns=[
    path('virat/',virat,name='virat'),
    path('malinga/',malinga,name='malinga'),
]