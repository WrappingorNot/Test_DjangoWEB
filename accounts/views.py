from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
def signup(request):
     if request.method == 'POST':
          if request.POST['password1'] == request.POST['password2']:
               user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                    email=request.POST['email'], )
               auth.login(request, user)
               return redirect('/')
          return render(request, 'home.html')
     return render(request, 'home.html')

def login(request):
     if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = auth.authenticate(request, username=username, password=password)
          if user is not None:
               auth.login(request, user)
               return redirect('login.html')
          else:
               return render(request, 'login.html')
     else:
          return render(request, 'login.html')


def logout(request):
     auth.logout(request)
     return redirect('login.html')

def initself(request):
     pass
# 여기 까지
# home
def home(request):
    return render(request, 'home.html')