from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from order.models import pay_status
from django.http import HttpResponseRedirect;
def order_create(request):
    cart = Cart(request)
    if not request.session['cart']:
        return HttpResponseRedirect('/home') 
    if request.method == 'POST':
        pay_method = request.POST.get('pay_method')
        form = OrderCreateForm(request.POST)
        order = ''
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
        if pay_method == 'cash_on':
            cart.clear()
            
            request.session['orderid']=order.id
            return HttpResponseRedirect('/orders/order-success')
        else:
            if request.session['userid']:
                return render(request, 'orders/order/pay.html', {'cart':cart})
            else:
                return HttpResponseRedirect('/login')
    else:
        form = OrderCreateForm()
        cart = Cart(request)
        if 'userid' in request.session:
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



def order_success(request):
    return render(request,'orders/order/created.html',{'title':'Order Success','orderid':request.session['orderid']})