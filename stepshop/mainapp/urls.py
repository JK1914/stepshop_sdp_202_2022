from django.urls import path

from mainapp.views import products, product

urlpatterns = [
    path('', products),
    path('product/', product),
]
