from unittest import TestCase

from chapter2.logistics_services import decide_parcel_amount


class Test(TestCase):
    def test_decide_parcel_amount(self):
        self.assertEqual(decide_parcel_amount(60), 250)

