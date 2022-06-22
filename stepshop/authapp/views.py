from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm

links_menu = [
    {'href': 'index', 'name': 'Домой', 'route': ''},
    {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
    {'href': 'about', 'name': 'О&nbsp;нас', 'route': 'about/'},
    {'href': 'contacts', 'name': 'Контакты', 'route': 'contacts/'},
]


def login(request):
    title = 'вход'

    login_form = ShopUserLoginForm(data=request.POST)

    _next = request.GET['next'] if 'next' in request.GET.keys() else ''

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user and user.is_active:
            auth.login(request, user)

            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])

            return HttpResponseRedirect(reverse('products:index'))

    context = {
        'title': title,
        'login_form': login_form,
        'next': _next,
        'links_menu': links_menu,
    }

    return render(request, 'authapp/login.html', context)


def register(request):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))

    else:
        register_form = ShopUserRegisterForm()

    context = {
        'title': title,
        'register_form': register_form,
        'links_menu': links_menu,
    }

    return render(request, 'authapp/register.html', context)


def edit(request):
    title = 'редактирование'

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)

        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))

    else:
        edit_form = ShopUserEditForm(instance=request.user)

    context = {
        'title': title,
        'edit_form': edit_form,
        'links_menu': links_menu,
    }

    return render(request, 'authapp/edit.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
