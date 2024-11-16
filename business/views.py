from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# from django.shortcuts import render


# def buss(request):
#   return HttpResponse("My business page here Please!")

def menu(request):
  return render(request, "business/accueil.html")


def authenticite(request):
  if request.method=="POST":
    username=request.POST["username"]
    password=request.POST["password"]
    user = authenticate(request,username=username, password=password)
    if user is not None:
      login(request, user)
      # redirect to tghe sucess page
      return redirect('raport') 
     
    else:
      return redirect('authenticite')
      messages.error(request, 'the is not the good!')
  
  else:
     return render(request,"business/authenticite.html" )

    
def end(request):
  return render(request, "business/end.end")

 
@login_required()
def raport(request):
  return render(request, "business/raport.html")

def deconnexion(request):
  logout(request)
  return redirect('home')

 


# Create your views here.
