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
    #    print("name",name)
    #    print("email",email)
    #    print("price",price)
    #    print("date",date)
    #    print("mobile",mobile)
    #    print("from",froml)
    #    print("to",tol)
       us = contactus.objects.get_or_create(name=name,email=email,price=price,date=date,mobile=mobile,from_location=froml,to_location=tol)
                    # <option value="1001">One Bedroom</option>
                    #   <option value="1002">Two Bedrooms</option>
                    #   <option value="1003">Three Bedrooms</option>
                    #   <option value="1004">Four Bedrooms +</option>
                    #   <option value="1005">Few items</option>
                    #   <option value="1006">Piano</option>
                    #   <option value="1007">Pool Table</option>
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
