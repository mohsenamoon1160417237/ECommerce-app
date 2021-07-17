from django.test import TestCase
from coupons.models import Coupon
import datetime
from django.contrib.auth.models import User
from decimal import Decimal


class CouponTest(TestCase):

    def setUp(self):

        user = User.objects.create(username='Mohsen',
                                   email='dramatic225@gmail.com')
        
        user.set_password('mohsen1160417237')
        user.save()

        coupon = Coupon.objects.create(code='coupon',
                                       active_from=datetime.date(2021,7,5),
                                       active_to=datetime.date(2021,7,6),
                                       discount=30,
                                       max_discount='12.00')
        
        coupon.user.add(user)
        coupon.save()
    
    
    def test_model(self):

        user = User.objects.get(id=1)
        coupon = Coupon.objects.get(id=1)


        self.assertEqual(coupon.code , 'coupon')
        self.assertEqual(coupon.active_from , datetime.date(2021,7,5))
        self.assertEqual(coupon.active_to , datetime.date(2021,7,6))
        self.assertEqual(coupon.discount , 30)
        self.assertEqual(coupon.max_discount , Decimal('12.00'))
        self.assertIn(user , coupon.user.all())