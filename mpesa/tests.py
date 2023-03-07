from django.test import TestCase
from mpesa.transactions import mpesa_express
# Create your tests here.
class MpesaExpressTest(TestCase):
    def test_mpesa_express(self):
        self.assertEqual(mpesa_express(254757164343,1,"payment"),"success")


