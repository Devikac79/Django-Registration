from django.shortcuts import render
from .models import *
# Create your views here.
def RegisterPage(request):
    return render(request,"app/register.html")


#view for user registration
def UserRegister(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        
        #first validate that user already exist
        user=User.objects.filter(Email=email)
        
        if user:
            message="user already exist"
            return render(request,"app/register.html",{'msg':message})
        else:
            if password==cpassword:
                newuser=User.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact,Password=password)
                message="User register successfully"
                return render(request,"app/login.html",{'msg':message})
            else:
                message="password doesnot match"
                return render(request,"app/register.html",{'msg':message})



def LoginPage(request):
    return render(request,"app/login.html")

#login User

def LoginUser(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']  
        
        #checking the email id with db
        user=User.objects.get(Email=email)
        
        if user:
            if user.Password==password:
                request.session['Firstname']==user.Firstname
                request.session['Lastname']==user.Lastname
                request.session['Email']==user.Email
                return render(request,"app/home.html")
            else:
                message="Password doesnot match"
                return render(request,"app/login.html"),{'msg':message}
        else:
            message="user doesnot exist"
            return render(request,"app/register.html"),{'msg':message}


              
