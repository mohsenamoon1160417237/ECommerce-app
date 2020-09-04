from django.shortcuts import render , get_object_or_404 , redirect
from .cart import Cart
from shop.models import Product
from .forms import CartForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from coupons.forms import CouponForm





@require_POST
def cart_add(request , product_id):

	product = get_object_or_404(Product , id=product_id , available=True)
	cart = Cart(request)
	form = CartForm(data=request.POST)

	if form.is_valid():
		if request.user.is_authenticated:

			cd = form.cleaned_data
			cart.add(product=product,
				 	quantity=cd['quantity'],
					 update_quantity=cd['update'])

	
			return redirect('cart:cart_detail')

		else:
			return redirect('login')
			




def cart_remove(request , product_id):


	cart = Cart(request)
	product = get_object_or_404(Product , id=product_id)
	cart.remove(product)

	return redirect('cart:cart_detail')




def cart_detail(request):

	cart = Cart(request)
	for item in cart:
		item['update_product_quantity'] = CartForm(initial={'quantity':item['quantity'] , 'update':True})

	form = CouponForm()

	return render(request , 'cart_detail.html' , {'cart':cart,
												  'form':form})