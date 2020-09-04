from django.urls import path
from . import views


app_name = 'payment'

urlpatterns = [


	path('stripe/' , views.payment_page , name='payment'),
	path('success/' , views.success_payment , name='success'),

]