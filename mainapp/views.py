from django.shortcuts import render


# Create your views here.


def main(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {'title': 'GeekShop - Products',
               'products': {'name': 'Отличный стул',
                            'propose': 'горячее предложение',
                            'price': 2585.9,
                            'description': {'headInfo': 'Расположитесь комфортно.',
                                            'materialsInfo': 'Отличное качество материалов '
                                                             'позволит вам это.',
                                            'colors': 'Различные цвета',
                                            'security': 'высочайший уровень '
                                                        'эргономики и прочность.', }}
               }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    context = {'title': 'GeekShop - Contacts'}
    return render(request, 'mainapp/contact.html', context)
