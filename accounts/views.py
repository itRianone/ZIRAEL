from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from orders.models import Order
from .forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django import forms
from django.contrib.auth.models import User

def user_login(request):

  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      user = authenticate(username=cd['username'], password=cd['password'])
      if user is not None:
        if user.is_active:
          login(request, user)
          return redirect('catalog:catalog_page')
        else:
          return render(request, 'registration/login.html', {'form': form, 'page_title': 'Логин', 'err': 'Юзер неактивен'})

      else:
        return render(request, 'registration/login.html', {'form': form, 'page_title': 'Логин', 'err': 'Нет такого юзера/пароль неверен'})
  else:

    form = LoginForm()
  
  return render(request, 'registration/login.html', {'form': form, 'page_title': 'Логин'})

def user_logout(request):
  if request.user.is_authenticated:
    logout(request)
    return redirect('catalog:catalog_page')
  else:
    return redirect('catalog:catalog_page') 

@login_required
def user_data(request):
  orders = Order.objects.filter(user=request.user)
  return render(request, 'accounts/user_detail.html', {'orders': orders, 'page_title': f'Страница юзера {request.user}'})

from .forms import LoginForm, UserRegistrationForm

def signup(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('accounts:login')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'user_form': user_form, 'page_title': 'Регистрация'})


  