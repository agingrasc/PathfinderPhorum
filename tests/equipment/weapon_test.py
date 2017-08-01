import unittest
from phorum import dice
from phorum.equipment import weapon


class WeaponTest(unittest.TestCase):
    def setUp(self):
        self.dice_six = dice.Dice(6, 6)
        self.dice_three = dice.Dice(3, 3)

    def tearDown(self):
        pass

    def test_weapon_one_dice_damage_equals_dice(self):
        damage_dice = [self.dice_six]
        sword = weapon.Weapon("sword", damage_dice)
        damage = sword.get_damage()

        self.assertEqual(6, damage)

    def test_weapon_two_dice_damage_equals_sum(self):
        damage_dice = [self.dice_six, self.dice_three]
        sword = weapon.Weapon("sword", damage_dice)
        damage = sword.get_damage()

        self.assertEqual(9, damage)