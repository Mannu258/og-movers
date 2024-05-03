from django.shortcuts import render
from . models import *
from django.core.mail import EmailMessage


# Create your views here.

def home(request):
    return render(request,'index.html')

def contact(request):
    if request.method == "POST":
       name =  request.POST.get('name')
       email =  request.POST.get('email')
       price =  request.POST.get('price')
       date =  request.POST.get('date')
       mobile =  request.POST.get('mobile')
       froml =  request.POST.get('froml')
       tol =  request.POST.get('tol')
       print("name",name)
       print("email",email)
       print("price",price)
       print("date",date)
       print("mobile",mobile)
       print("from",froml)
       print("to",tol)
       us = contactus.objects.get_or_create(name=name,email=email,price=price,date=date,mobile=mobile,from_location=froml,to_location=tol)
       try:
            email = EmailMessage(
                subject='Order Received',
                body=f"Name:\t{name}\nEmail:\t{email}\nPrice:\t{price}\nDate:\t{date}\nMobile:\t{mobile}\nFrom:\t{froml}\nTo:\t{tol}\n\nRegards,\nOG Movers\n\nContact Us:\nPhone: +1 (123) 456-7890\nEmail: info@ogmovers.com",
                to=['mandeepkumarmannu123@gmail.com']
)

            email.send()
       except Exception as e:
           price(e)
       return render(request,'thankyou.html')
    
    return render(request,'contact.html')
