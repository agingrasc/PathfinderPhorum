import unittest
from phorum.dice import Dice


class DiceTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_roll_single_value_dice_returns_same_value(self):
        dice_value = 1
        dice = Dice(dice_value)

        result = dice.roll()
        self.assertEqual(dice_value, result)

    def test_roll_non_default_single_value_returns_same_value(self):
        dice_value = 42
        dice = Dice(dice_value, dice_value)

        result = dice.roll()
        self.assertEqual(dice_value, result)

    def test_dice_with_same_range_are_equals(self):
        first_dice = Dice(6)
        second_dice = Dice(6)

        self.assertTrue(first_dice == second_dice)

    def test_dice_with_different_max_value_not_equal(self):
        first_dice = Dice(42)
        second_dice = Dice(6)

        self.assertTrue(first_dice != second_dice)

    def test_dice_with_different_min_value_not_equal(self):
        first_dice = Dice(6, 1)
        second_dice = Dice(6, 3)

        self.assertTrue(first_dice != second_dice)
