from django.shortcuts import render


# Create your views here.


def main(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {'title': 'GeekShop - Products'}
    return render(request, 'mainapp/products.html', context)


def contact(request):
    context = {'title': 'GeekShop - Contacts'}
    return render(request, 'mainapp/contact.html', context)
