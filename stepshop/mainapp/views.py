from django.shortcuts import render

links_menu = [
    {'href': 'index', 'name': 'Домой', 'route': ''},
    {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
    {'href': 'about', 'name': 'О&nbsp;нас', 'route': 'about/'},
    {'href': 'contacts', 'name': 'Контакты', 'route': 'contacts/'},
]


def products(request):
    title = 'Продукты'

    context = {
        'title': title,
        'links_menu': links_menu
    }
    return render(request, 'products.html', context)


def product(request):
    title = 'продукт'

    context = {
        'title': title,
        'links_menu': links_menu,
    }

    return render(request, 'product.html', context)
