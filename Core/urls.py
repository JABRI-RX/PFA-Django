 
from django.urls import path
from Core.views import index,contact
urlpatterns = [
    path('',index,name='index'),
    path('contact',contact,name='contact')
]
