from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.conf import settings
from .models import Emailinfo
from django.core.mail import send_mail
# Create your views here.



def signup(request):
    if request.method=='POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"username taken")
                return redirect('signup')
                
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=user_name,password = password1,email=email,first_name=firstname,last_name=lastname)
                user.save();
                print("user created")
                return redirect('home')
    
        else:
            messages.info(request,"passord mismatch")
          
        return redirect('signup')
    else:
        return render(request,'signup.html')


def signin(request):


    if request.method=='POST':
          if request.method=='POST':
            email = request.POST['email']
            Password = request.POST['password']

            user = auth.authenticate(email=email,password=Password)
            if user is not None:
                auth.login(request,user)
                return redirect("/")
            else:
                messages.info(request,"Invalid username or password") 
                print("Invalid username or password")
                return redirect('home')
    else:

        return render(request,'signin.html')



def home(request):
    return render(request,'home.html')

def logout(request):
    return render(request,'index.html')

def Email(request):
    
    emailaddress = request.POST.get('email',False)
    Passwords = request.POST.get('password',False)
    recipient_list = request.POST['emailTO']
    subject = request.POST['subject']
    message = request.POST['message']

    user = auth.authenticate(email= emailaddress,password=Passwords,message=message,subject=subject)
    
    subject = 'welcome to GFG world'
    message = f'Hi {emailaddress}, thank you for registering in geeksforgeeks.'
    email_from = settings.EMAIL_HOST_USER
    
    send_mail( subject, message, email_from, [recipient_list] )
        
    print(recipient_list)

    print(email_from)
    
    messages.info(request,"mail sent")
    return render(request,'home.html')
