from django.test import TestCase
from coupons.forms import CouponForm


class CouponFormTest(TestCase):

    def setUp(self):

        self.data = {'code' : 'abcdef'}
    
    def test_form_is_valid(self):

        form = CouponForm(data=self.data)
        self.assertTrue(form.is_valid())