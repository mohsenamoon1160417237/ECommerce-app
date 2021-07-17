from django.test import TestCase


class PaymentPageViewTest(TestCase):

    def setUp(self):

        self.url = '/payment/stripe/'
    
    def test_url_ok(self):

        response = self.client.post(self.url)

        self.assertEqual(response.status_code , 200)

