from django.shortcuts import render
from . models import *
import time
from . email import *
import threading

# Create your views here.

def home(request):
    if request.method == "POST":
       name =  request.POST.get('name')
       customer_email =  request.POST.get('email')
       price =  request.POST.get('price')
       date =  request.POST.get('date')
       mobile =  request.POST.get('mobile')
       froml =  request.POST.get('froml')
       tol =  request.POST.get('tol')

       us = contactus.objects.get_or_create(name=name,email=customer_email,price=price,date=date,mobile=mobile,from_location=froml,to_location=tol)

       try:
            if price == '1001':
                price = "One Bedroom"
            elif price == '1002':
                price = "Two Bedrooms"
            elif price == '1003':
                price = "Three Bedrooms"
            elif price == '1004':
                price = "Four Bedrooms"
            elif price == '1005':
                price = "Few items "
            elif price == '1006':
                price = "Piano"
            elif price == '1007':
                price = "Pool Table"

            order_thread = threading.Thread(target=send_order_email, args=(name, customer_email, price, date, mobile, froml, tol))
            
            order_thread.start()

       except Exception as e:
           print(e)
       return render(request,'thankyou.html')
    
    
    return render(request,'index.html')
def contact(request):
    if request.method == "POST":
       name =  request.POST.get('name')
       customer_email =  request.POST.get('email')
       price =  request.POST.get('price')
       date =  request.POST.get('date')
       mobile =  request.POST.get('mobile')
       froml =  request.POST.get('froml')
       tol =  request.POST.get('tol')

       us = contactus.objects.get_or_create(name=name,email=customer_email,price=price,date=date,mobile=mobile,from_location=froml,to_location=tol)

       try:
            if price == '1001':
                price = "One Bedroom"
            elif price == '1002':
                price = "Two Bedrooms"
            elif price == '1003':
                price = "Three Bedrooms"
            elif price == '1004':
                price = "Four Bedrooms"
            elif price == '1005':
                price = "Few items "
            elif price == '1006':
                price = "Piano"
            elif price == '1007':
                price = "Pool Table"

            order_thread = threading.Thread(target=send_order_email, args=(name, customer_email, price, date, mobile, froml, tol))
            
            order_thread.start()

       except Exception as e:
           print(e)
       return render(request,'thankyou.html')
    
    return render(request,'contact.html')


def terms(request):
    return render(request,'terms.html')

def privacy(request):
    return render(request,'privacy.html')

def service(request):
    return render(request,"service.html")
