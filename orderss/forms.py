from django import forms
from .models import Order , OrderItem


class OrderForm(forms.ModelForm):

	class Meta:

		model = Order
		exclude = ['owner' , 'created' , 'updated' , 'paid']


class OrderItemForm(forms.ModelForm):

	QUANTITY = [(i,str(i)) for i in range(1,21)]


	quantity = forms.TypedChoiceField(QUANTITY , coerce=int , required=True) 

	class Meta:

		model = OrderItem
		exclude = ['order' , 'product' , 'quantity' , 'price']
