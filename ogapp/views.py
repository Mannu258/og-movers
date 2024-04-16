from django.shortcuts import render

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


    return render(request,'contact.html')
