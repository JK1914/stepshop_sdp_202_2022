from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from authapp.forms import ShopUserLoginForm


def login(request):
    title = 'вход'

    login_form = ShopUserLoginForm(data=request.POST)

    context = {
        'title': title,
        'login_form': login_form,
    }

    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
