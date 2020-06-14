from django.shortcuts import render,HttpResponse
from. models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home/home.html')


def contact(request):
    if request.method== 'POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        

        # form validation
        if len(name)<3:
            messages.error(request, 'please fill your name correctly ')
        if (10>len(phone) or len(phone)>13):
            messages.error(request, 'please enter a valid mobile number ')
        
        if len(message)<5:
            messages.error(request, 'please write your message in detail ')
       
        else:
            contact = Contact(name = name, phone = phone, email = email, message = message,)
            contact.save()
            messages.success(request, 'Thank you! we will contact you soon ')
    
    return render(request, 'home/contact.html')


def about(request):
   
    return render(request,'home/about.html')