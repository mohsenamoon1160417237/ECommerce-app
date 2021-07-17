from django.test import TestCase
from cart.forms import CartForm


class CartFormTest(TestCase):

    def setUp(self):

        self.data = {'quantity' : 1,
                     'update' : True}
        
    def test_form_is_valid(self):

        form = CartForm(data=self.data)
        
        self.assertTrue(form.is_valid())