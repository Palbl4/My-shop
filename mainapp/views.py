from django.shortcuts import render, get_object_or_404

from .models import ListOfProduct

ListOfProduct = ListOfProduct.objects.filter(is_active=True)
Men = ListOfProduct.filter(sex=1)
Woman = ListOfProduct.filter(sex=2)


def main(request):
    return render(request, 'mainapp/index.html')


def mens_shoes(request):
    return render(request, 'mainapp/mens_shoes.html',
                  {'ListOfProduct': Men})


def womans_shoes(request):
    return render(request, 'mainapp/womans-shoes.html',
                  {'ListOfProduct': Woman})


def product(request, pk):
    title = 'Продукты'
    content = {
        'ListOfProduct': ListOfProduct,
        'title': title,
        'ListOfProduct': get_object_or_404(ListOfProduct, pk=pk),
    }
    return render(request, 'mainapp/product.html', content)
