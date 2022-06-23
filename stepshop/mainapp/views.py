from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from common.links_menu import link_menu
from mainapp.models import Product, ProductCategory


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    return []


def get_same_products(current_product):
    return Product.objects.filter(category=current_product.category).exclude(pk=current_product.pk)


def products(request, pk=None):
    title = 'Продукты'

    products_ = Product.objects.all().order_by('-price')  # .filter(category__name='Джинсы').order_by('-price') [:3]
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
            'category': category,
            'basket': basket,
        }

        return render(request, 'products.html', context)

    context = {
        'title': title,
        'links_menu': link_menu(),
        'products': products_,
        'categories': categories,
        'basket': basket,
    }

    return render(request, 'products.html', context)


def product(request, pk=None):
    title = 'продукт'

    context = {
        'title': title,
        'links_menu': link_menu(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
        'same_products': get_same_products(get_object_or_404(Product, pk=pk)),
    }

    return render(request, 'product.html', context)
