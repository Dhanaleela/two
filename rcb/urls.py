from django.urls import path
from rcb.views import *
app_name='something'
urlspatterns=[
    path('rcb/',rcb,name='rcb'),
]