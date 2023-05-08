from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from order.models import pay_status
from django.http import HttpResponseRedirect;
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            #cart.clear()
        if request.session['userid']:
            return render(request, 'orders/order/pay.html', {'order': order,'cart':cart})
        else:
            return HttpResponseRedirect('/login')
    else:
        form = OrderCreateForm()
        cart = Cart(request)
        if(request.session['userid']):
            return render(request, 'orders/order/create.html', {'form': form,'cart':cart})
        else:
            request.session['url_key']='/orders/create'
            return HttpResponseRedirect('/login')


def pay(request):
    cart = Cart(request)
    if request.method == 'POST':
        user_id=request.session['userid']
        email = request.POST.get('email')
        oid = request.POST.get('oid')
        amout = request.POST.get('amount')
        pay = pay_status(userId=user_id,email=email,ORDERID=oid,amount=amout)
        pay.save()
        cart= Cart(request)
        cart.clear()
        return render(request,'orders/order/created.html',{'title':'Order Success','orderid':oid})



