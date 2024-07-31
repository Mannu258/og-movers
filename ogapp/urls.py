from django.urls import path
from . views import *

urlpatterns = [
   path('',home),
   path('contact',contact,name="contact"),
   path('terms',terms,name="terms"),
   path('privacy',privacy,name="privacy"),
   path('service',service,name="service"),
   path('service/<str:params>',innerservice,name="iservice")



]
