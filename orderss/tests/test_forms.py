from django.test import TestCase
from orderss.forms import OrderForm , OrderItemForm
from decimal import Decimal
from orderss.models import Order
from django.urls import reverse


class OrderFormTest(TestCase):

    '''
    OrderForm fields:

    first_name , last_name , email , address , city , postal_code ,
    phone_number

    '''

    def test_form_is_valid(self):

        data = {'first_name' : 'Mohsen',
                'last_name' : 'Amoon',
                'email' : 'dramatic225@gmail.com',
                'address' : 'Isfahan',
                'city' : Order.Isfahan,
                'postal_code' : '123123',
                'phone_number' : '123123'}
        
        form = OrderForm(data=data)

        self.assertTrue(form.is_valid())
        
    def test_form_invalid_email(self):

        data = {'first_name' : 'Mohsen',
                'last_name' : 'Amoon',
                'email' : 'dramatic22.com',
                'address' : 'Isfahan',
                'city' : Order.Isfahan,
                'postal_code' : '123123',
                'phone_number' : '123123'}

        form = OrderForm(data=data)
        self.assertEqual(form.errors['email'][0] , 'Enter a valid email address.')



class OrderItemFormTest(TestCase):

    def test_form_is_valid(self):

        data = {'quantity' : 4}
        form = OrderItemForm(data=data)
        self.assertTrue(form.is_valid())

        