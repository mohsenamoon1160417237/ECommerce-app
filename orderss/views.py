from django.shortcuts import render , redirect
from cart.cart import Cart
from .forms import OrderForm
from .models import Order , OrderItem



def order_create(request):

	cart = Cart(request)

	if request.method == 'POST':

		form = OrderForm(data=request.POST)

		if form.is_valid():

			order = form.save(commit=False)
			order.owner = request.user
			order.save()

			for item in cart:

				OrderItem.objects.create(order=order,
										 product=item['product'],
										 quantity=item['quantity'],
										 price=item['price'])
				
			cart.clear()

			return render(request , 'order_done.html' , {'cart':cart,
														 'order':order})

	else:

		form = OrderForm()


	return render(request , 'order_create.html' , {'form':form})