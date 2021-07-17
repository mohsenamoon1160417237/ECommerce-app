from django.test import TestCase
from shop.models import Product
from django.contrib.auth.models import User
from coupons.forms import CouponForm


class CartAddViewTest(TestCase):

    def setUp(self):

        self.data = {"quantity" : 2,
                     "update" : False}

        self.product = Product.objects.create(name='clothes',
                                              description='clothes',
                                              price=12.00
                                              )
        self.product.save()

        self.user = User.objects.create(username='mohsen' ,
                                        email='dramatic225@gmail.com' ,
                                        password='mohsen1160417237')
        self.user.save()

        self.url = '/cart/add/{}/'.format(self.product.id)
    
    
    def test_get_method_not_allowed(self):

        response = self.client.get(self.url , follow=True)
        self.assertEqual(response.status_code , 405)

    
    
    def test_cart_add_user_authenticated(self):

        self.client.force_login(self.user)
        response = self.client.post(self.url , data=self.data , follow=True)

        redirect_url = response.request['PATH_INFO']

        self.assertEqual(response.status_code , 200)
        self.assertEqual(redirect_url , '/cart/detail/')
    

    def test_cart_add_user_not_authenticated(self):
    
        self.client.logout()
        response = self.client.post(self.url , data=self.data , follow=True)
        redirect_url = response.request['PATH_INFO']

        self.assertEqual(response.status_code , 200)
        self.assertEqual(redirect_url , '/account/login/')




class CartRemoveViewTest(TestCase):

    def setUp(self):

        self.product = Product.objects.create(name='clothes',
                                              description='clothes',
                                              price=12.00
                                              )
        self.product.save()

        self.url = '/cart/remove/{}/'.format(self.product.id)


    def test_get_method_not_allowed(self):

        response = self.client.get(self.url , follow=True)
        self.assertEqual(response.status_code , 405)
    
    def test_cart_remove_ok(self):

        response = self.client.post(self.url , follow=True)
        redirect_url = response.request['PATH_INFO']

        self.assertEqual(response.status_code , 200)
        self.assertEqual(redirect_url , '/cart/detail/')
    



class CartDetailViewTest(TestCase):

    def setUp(self):

        self.data = {''}
        self.url = '/cart/detail/'
    
    def test_cart_detail_ok(self):

        response = self.client.post(self.url)

        self.assertEqual(response.status_code , 200)
