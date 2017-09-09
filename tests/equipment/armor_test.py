import unittest
from phorum.equipment import armor


class WeaponTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_given_normal_armor_when_compute_normal_armor_class_then_return_armor_class(self):
        shirt = armor.Armor("Shirt", 6)
        armor_bonus = shirt.compute_normal_armor_class()

        self.assertEqual(6, armor_bonus)
