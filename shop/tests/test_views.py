from django.test import TestCase
from shop.models import Product
from django.http import HttpRequest


class ProductListAllTest(TestCase):

    def setUp(self):

        product1 = Product.objects.create(name='scraf',
                                          price='120.00')
        product1.save()

        product2 = Product.objects.create(name='planket',
                                          price='11.00')
        product2.save()

        product3 = Product.objects.create(name='planke',
                                          price='11.00')
        product3.save()

        product4 = Product.objects.create(name='plank',
                                          price='11.00')
        product4.save()

        self.url = '/'
    
    def test_url(self):

        
        response = self.client.post(self.url , {})
        self.assertEqual(response.status_code , 200)
        print(response.content)
    