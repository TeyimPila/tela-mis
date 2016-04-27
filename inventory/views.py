from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Product
from cart.forms import CartAddProductForm


@login_required(login_url='admin:login')
def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'inventory/product/list.html', {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id, available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'inventory/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})
