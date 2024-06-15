from django.urls import path
from . views import *

urlpatterns = [
   path('',home),
   path('contact',contact,name="contact"),
   path('terms',terms,name="terms"),
   path('privacy',privacy,name="privacy"),


]
