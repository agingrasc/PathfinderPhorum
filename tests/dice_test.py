import unittest
from phorum import dice


class DiceTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_roll_single_value_dice_returns_same_value(self):
        dice_value = 1
        test_dice = dice.Dice(dice_value)

        result = test_dice.roll()
        self.assertEqual(dice_value, result)

    def test_roll_non_default_single_value_returns_same_value(self):
        dice_value = 42
        test_dice = dice.Dice(dice_value, dice_value)

        result = test_dice.roll()
        self.assertEqual(dice_value, result)

    def test_dice_with_same_range_are_equals(self):
        first_dice = dice.Dice(6)
        second_dice = dice.Dice(6)

        self.assertTrue(first_dice == second_dice)

    def test_dice_with_seed_determinist(self):
        first_dice = dice.Dice(6, seed=1)
        result = first_dice.roll()

        self.assertEqual(2, result)

    def test_dice_with_different_max_value_not_equal(self):
        first_dice = dice.Dice(42)
        second_dice = dice.Dice(6)

        self.assertTrue(first_dice != second_dice)

    def test_dice_with_different_min_value_not_equal(self):
        first_dice = dice.Dice(6, 1)
        second_dice = dice.Dice(6, 3)

        self.assertTrue(first_dice != second_dice)
