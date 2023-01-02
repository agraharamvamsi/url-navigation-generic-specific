from django.urls import path
from app1.views import *
app_name='Chittoorkurradu'
urlpatterns=[
    path('dinesh/',Dinesh,name='Dinesh'),
]