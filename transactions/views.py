from django.shortcuts import render
from .models import CheckoutItem
from .forms import CheckoutCreateForm
from cart.cart import Cart


def checkout_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CheckoutCreateForm(request.POST)
        if form.is_valid():
            checkout = form.save()
            for item in cart:
                CheckoutItem.objects.create(checkout=checkout,
                                            product=item['product'],
                                            status=item['status'],
                                            quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asynchronous task
            # order_created.delay(order.id)
            return render(request, 'transactions/checkout/checked_out.html', {'checkout': checkout})
    else:
        form = CheckoutCreateForm()
    return render(request, 'transactions/checkout/create.html', {'cart': cart,
                                                                 'form': form})
