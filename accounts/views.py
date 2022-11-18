from django.shortcuts import render, redirect
from django.contrib import auth

def signup(request):
     pass


def login(request):
     if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = auth.authenticate(request, username=username, password=password)
          if user is not None:
               auth.login(request, user)
               return redirect('accounts/login.html')
          else:
               return render(request, 'accounts/login.html')
     else:
          return render(request, 'accounts/login.html')


def logout(request):
     auth.logout(request)
     return redirect('accounts/login.html')