from django.shortcuts import render
import stripe
from cart.cart import Cart
from decimal import Decimal

stripe.api_key = 'sk_test_51HBES5Gg9T1RhklEeQ0euCiL1TvHPkfaRD2wdzF7wqdrWc8l6XhNSiB9yu8rALHP9cJGnl5cNqeZNc1aTMhbB4P900aNrweO3D'


def payment_page(request):

	cart = Cart(request)

	total = cart.get_total_price_after_discount()

	return render(request , 'payment.html' , {'total':total})




def success_payment(request):

	cart = Cart(request)
	amount = Decimal(cart.get_total_price_after_discount())

	if request.method == 'POST':

		print('Data:' , request.POST)

		customer = stripe.Customer.create(
				   email=request.POST['email'],
				   first_name=request.POST['first_name'],
			 	   source=request.POST['stripeToken']
				   )
		charge = stripe.Charge.create(
			customer=customer,
			amount = amount * 100,
			currency='usd',
			description='Payment with stripe'
			)
		request.user.orders.paid = True

	return render(request , 'success.html')