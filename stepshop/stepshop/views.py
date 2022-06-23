from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from common.links_menu import link_menu
from mainapp.models import Product, ProductCategory


def index(request, pk=None):
    title = 'главная страница'

    products_ = Product.objects.all()[:3]
    categories = ProductCategory.objects.all()

    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products_ = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products_ = Product.objects.filter(category__pk=pk).order_by('price')

    context = {
        'title': title,
        'links_menu': link_menu(),
        'products': products_,
        'categories': categories,
        'basket': basket,
    }

    return render(request, 'index.html', context)
    # return render(request=request, template_name='index.html', context=context)


def contacts(request):
    title = 'контакты'

    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'links_menu': link_menu(),
        'basket': basket,
    }

    return render(request, 'contact.html', context)


def about(request):
    title = 'о нас'

    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'links_menu': link_menu(),
        'basket': basket,
    }

    return render(request, 'about.html', context)
