from django.test import TestCase
from orderss.models import Order , OrderItem
from django.utils.text import slugify
from django.contrib.auth.models import User
from decimal import Decimal
from shop.models import Product


class OrderAndOrderItemTest(TestCase):

    def setUp(self):

        user = User.objects.create(username='admin' , email='dramatic225@gmail.com')
        user.set_password('mohsen1160417237')
        user.save()

        order = Order.objects.create(owner=user,
                                     first_name='Mohsen',
                                     last_name='Amoon',
                                     email='dramatic225@gmail.com',
                                     address='Isfahan',
                                     city=Order.Isfahan,
                                     postal_code='123123',
                                     status=Order.Sent)

        order.save()

        product = Product.objects.create(name='scarf',
                                         description='high quality',
                                         manufacturer='Mohsen',
                                         price='120.00'
                                         )
        
        product.save()

        orderItem1 = OrderItem.objects.create(order=order,
                                              product=product,
                                              quantity=2,
                                              price='12.00')
        
        orderItem1.save()
        
        orderItem2 = OrderItem.objects.create(order=order,
                                              product=product,
                                              quantity=3,
                                              price='22.00')
        orderItem2.save()

    
    def test_model_order(self):

        user = User.objects.get(id=1)
        order = Order.objects.get(id=1)

        self.assertEqual(order.owner , user)
        self.assertEqual(order.first_name , 'Mohsen')
        self.assertEqual(order.last_name , 'Amoon')
        self.assertEqual(order.email , 'dramatic225@gmail.com')
        self.assertEqual(order.address , 'Isfahan')
        self.assertEqual(order.city , Order.Isfahan)
        self.assertEqual(order.postal_code , '123123')
        self.assertEqual(order.paid , False)
        self.assertEqual(order.status , Order.Sent)
        self.assertEqual(order.slug , 'order_{}'.format(order.id))
        self.assertEqual(order.get_total_cost() , Decimal('90.00'))

    
    def test_model_order_item(self):

        order = Order.objects.get(id=1)
        orderItem1 = OrderItem.objects.get(id=1)
        product = Product.objects.get(id=1)

        self.assertEqual(orderItem1.order , order)
        self.assertEqual(orderItem1.product , product)
        self.assertEqual(orderItem1.quantity , 2)
        self.assertEqual(orderItem1.price , Decimal('12.00'))
        self.assertEqual(orderItem1.get_cost() , Decimal('24.00'))