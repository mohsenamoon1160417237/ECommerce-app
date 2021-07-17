from django.test import TestCase
from coupons.models import Coupon
from coupons.forms import CouponForm
from coupons.views import coupon_apply
import datetime
from django.contrib.auth.models import User


class CouponApplyViewTest(TestCase):

    def setUp(self):

        self.coupon = Coupon.objects.create(code='summer_coupon',
                                            active_from=datetime.date(2021,7,6),
                                            active_to=datetime.date(2021,7,17),
                                            discount=40,
                                            max_discount='120.00')
        
        self.coupon.save()

        self.data = {'code' : 'summer_coupon'}

        self.user = User.objects.create(username='mohsen',
                                        email='dramatic225@gmail.com',
                                        password='mohsen1160417237')
        
        self.user.save()

        self.url = '/coupons/'
    
    def test_self_coupon_user_is_blank(self):

        users = self.coupon.user.all()
        self.assertFalse(users.exists())
        self.assertEqual(users.count() , 0)
    

    def test_self_coupon_number_is_zero(self):

        self.assertEqual(self.coupon.number , 0)


    def test_200_ok(self):

        self.client.force_login(self.user)

        response = self.client.post(self.url , data=self.data , follow=True)

        coupons = Coupon.objects.all()
        coupon = coupons.first()

        redirect_path = response.request['PATH_INFO']

        self.assertEqual(coupons.count() , 1)
        self.assertIn(self.user , coupon.user.all())
        self.assertEqual(coupon.number , 1)
        self.assertEqual(response.status_code , 200)
        self.assertEqual(redirect_path , '/cart/detail/')
        
