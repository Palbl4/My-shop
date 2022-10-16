from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from basket.models import Basket
from mainapp.models import ListOfProduct, SizeRange


@login_required
def basket(request):
    basket_items = Basket.objects.filter(
        user=request.user).order_by('product__title')
    content = {
        'basket_items': basket_items,
    }
    return render(request, 'basket/basket.html', content)


@login_required
def basket_add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('main:men',
                                            args=[pk]))

    if request.method == 'POST':
        size = request.POST.copy().pop('size')
        sizes = ','.join(size)
    product = get_object_or_404(ListOfProduct, pk=pk)
    basket = Basket.objects.filter(user=request.user,
                                   product=product).first()
    if not basket:
        basket = Basket(user=request.user, product=product, size=sizes)
    basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
