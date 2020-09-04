from django import forms


class CartForm(forms.Form):

	UPDATE_QUANTITY = [(i , str(i)) for i in range(1,21)]

	quantity = forms.TypedChoiceField(choices=UPDATE_QUANTITY , coerce=int)
	update = forms.BooleanField(required=False , initial=False , widget=forms.HiddenInput)
