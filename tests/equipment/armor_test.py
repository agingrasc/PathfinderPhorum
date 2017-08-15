import unittest
from phorum.equipment import armor


class WeaponTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_armor_get_armor_bonus_equals_bonus(self):
        shirt = armor.Armor("Shirt", 6)
        armor_bonus = shirt.get_armor_bonus()

        self.assertEqual(6, armor_bonus)
