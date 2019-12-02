from django.shortcuts import render, redirect
from .models import User
from .forms import UserCreate
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from datetime import date
from django.urls import reverse
import json
from .forms import UserLogin
from django.http.response import HttpResponseRedirect

def index(request, auth_id=0):
    user_id = int(auth_id)
    users = User.objects.all()
    for user in users:
        user.age = date.today().year - user.birthdate.year
    try:
        user_sel = User.objects.get(id = user_id)
        is_admin = user_sel.is_admin
    except User.DoesNotExist:
        is_admin = False
    return render(request, 'gamecrush/index.html', {'users': users,'auth_id':int(auth_id),'is_admin':is_admin})

def signin(request, auth_id=0):
    login = UserLogin()
    if request.method == 'POST':
        login = UserLogin(request.POST, request.FILES)
        user_email = login['email'].value()
        password = login['password'].value()
        try:
            user_sel = User.objects.get(email=user_email)
        except User.DoesNotExist:
            return render(request, 'gamecrush/signin.html', {'login_form': login, 'auth_id':int(auth_id)})
        if(password != user_sel.password):
            return render(request, 'gamecrush/signin.html', {'login_form': login, 'auth_id':int(auth_id)})
        return redirect(reverse('index', kwargs={'auth_id': user_sel.id}))
    else:
        return render(request, 'gamecrush/signin.html', {'login_form':login, 'auth_id':int(auth_id)})

def profile(request, user_id, auth_id=0):
    user_id = int(user_id)
    try:
        user_sel = User.objects.get(id = user_id)
    except User.DoesNotExist:
        return redirect(reverse('index', kwargs={'auth_id': auth_id}))
       
    return render(request, 'gamecrush/profile.html', {
        'auth_id': int(auth_id),
        'user_id': user_id,
        'name': user_sel.name,
        'age': date.today().year - user_sel.birthdate.year,
        'describe': user_sel.describe
    })

def upload(request, auth_id=0):
    upload = UserCreate()
    if request.method == 'POST':
        upload = UserCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            user_sel = User.objects.get(email=upload['email'].value())
            return redirect(reverse('index', kwargs={'auth_id': user_sel.id}))
        else:
            return render(request, 'gamecrush/register.html', {'upload_form': upload, 'auth_id':int(auth_id)})
    else:
        return render(request, 'gamecrush/register.html', {'upload_form':upload, 'auth_id':int(auth_id)})

def update_user(request, user_id, auth_id=0):
    user_id = int(user_id)
    try:
        user_sel = User.objects.get(id = user_id)
    except User.DoesNotExist:
        return redirect(reverse('index', kwargs={'auth_id': auth_id}))
    user_form = UserCreate(request.POST or None, instance = user_sel)
    if user_form.is_valid():
        user_form.save()
        return redirect(reverse('update', kwargs={'auth_id':auth_id, 'user_id':user_id}))
    return render(request, 'gamecrush/register.html', {'upload_form':user_form, 'auth_id':int(auth_id), 'user_id':int(user_id)})

def delete_user(request, user_id, auth_id=0):
    user_id = int(user_id)
    try:
        user_sel = User.objects.get(id = user_id)
    except User.DoesNotExist:
        return redirect(reverse('index', kwargs={'auth_id': auth_id}))
    user_sel.delete()
    return redirect(reverse('index', kwargs={'auth_id': auth_id}))