from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def signin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard/')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            print('Login Successful')
            login(request, user)
            return redirect('/')
        else:
            print('Login Failed 1')
            form = AuthenticationForm(request.POST)
            return render(request, 'authorization/login.html', {'form': form})
    else:
        print('Login Failed 2')
        form = AuthenticationForm()
        return render(request, 'authorization/login.html', {'form': form})
