from django.test import TestCase
from cart.cart import Cart
from orderss.models import Order , OrderItem
from django.contrib.auth.models import User
from shop.models import Product
from django.shortcuts import get_object_or_404



class OrderCreateViewTest(TestCase):

    def setUp(self):

        self.user = User.objects.create(username='Mohsen' ,
                                        email='dramatic225@gmail.com' ,
                                        password='mohsen1160417237')
        self.user.save()

        self.data = {'first_name' : 'Mohsen',
                     'last_name' : 'Amoon',
                     'email' : 'dramatic225@gmail.com',
                     'address' : 'Isfahan',
                     'city' : Order.Isfahan,
                     'postal_code' : '123123',
                     'phone_number' : '123123'}
        
        self.url = '/order/'


    def test_post_200_ok(self):


        response = self.client.get(self.url)
        self.assertEqual(response.status_code , 200)


    def test_order_saved(self):


        self.client.force_login(self.user)
        response = self.client.post(self.url , data=self.data)
        order = get_object_or_404(Order , id=1)

        self.assertTrue(order is not None)
        self.assertEqual(order.first_name , 'Mohsen')
        self.assertEqual(order.last_name , 'Amoon')
        self.assertEqual(order.email , 'dramatic225@gmail.com')
        self.assertEqual(order.address , 'Isfahan')
        self.assertEqual(order.city , Order.Isfahan)
        self.assertEqual(order.postal_code , '123123')
        self.assertEqual(order.phone_number , '123123')
    

'''    def test_order_item_saved(self):

        self.client.force_login(self.user)
        self.client.post(self.url , data=self.data)
        order_items = OrderItem.objects.all()

        self.assertTrue(order_items.exists())
'''