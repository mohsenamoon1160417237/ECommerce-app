from django.shortcuts import render , redirect
from cart.cart import Cart
from .forms import CouponForm
from django.utils import timezone
from .models import Coupon
from decimal import Decimal



def coupon_apply(request):

	cart = Cart(request)
	now = timezone.now()

	form = CouponForm(data=request.POST)

	if form.is_valid():

		cd = form.cleaned_data
			
		try:

			coupon = Coupon.objects.get(code__iexact=cd['code'],
									    active_from__lte=now,
										active_to__gte=now,
										valid=True)

			
			coupon.save()

			request.session['coupon_id'] = coupon.id

			coupon.user.add(request.user)
			coupon.number += 1



		except Coupon.DoesNotExist:

			request.session['coupon_id'] = None


	return redirect('cart:cart_detail')



