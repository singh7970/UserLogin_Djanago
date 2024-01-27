from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponse 


from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout 

# Create your views here.
@login_required(login_url="/login")
def home(request):
   return render (request,'home.html')

def Signup(request):
   if request.method =="POST":
      uname=request.POST.get('username')
      email=request.POST.get('email')
      pass1=request.POST.get('password')
      my_user=User.objects.create_user(uname,email,pass1)
      my_user.save()
      return redirect('/login')

   return render (request,'signup.html')

def LoginPage(request):
    if request.method=="POST":
       usrname=request.POST.get('username')
       pass1=request.POST.get('pass')
       print(usrname,pass1)
       user=authenticate(request,username=usrname,password=pass1)
       if user is not None:
          login(request,user)
          return redirect("/home")
       else:
          return HttpResponse("username or password is incorrect")  


    return render (request,'login.html')
def Logoutpage(request):
   logout(request)
   return redirect('/login')
