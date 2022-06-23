from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from common.links_menu import link_menu
from basketapp.models import Basket
from mainapp.models import Product


@login_required
def basket(request):
    if request.user.is_authenticated:
        basket_ = Basket.objects.filter(user=request.user)

        context = {
            'basket': basket_,
            'links_menu': link_menu(),
        }

        return render(request, 'basketapp/basket.html', context)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:product', args=[pk]))

    product = get_object_or_404(Product, pk=pk)

    basket_ = Basket.objects.filter(user=request.user, product=product).first()

    if not basket_:
        basket_ = Basket(user=request.user, product=product)

    basket_.quantity += 1
    basket_.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
