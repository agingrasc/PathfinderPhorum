import unittest

from phorum import player
from phorum import combat


class CombatTest(unittest.TestCase):

    def setUp(self):
        self.ally = player.Player(12, 20, 10, 6)
        self.enemy = player.Player(12, 10, 1, 6)

    def tearDown(self):
        pass

    def test_rounds_enemy_lose(self):
        ally, enemy = combat.rounds(self.ally, self.enemy)
        self.assertTrue(ally.is_alive())
        self.assertFalse(enemy.is_alive())

    def test_rounds_ally_lose(self):
        self.ally = player.Player("ally", 5)
        self.enemy = player.Player("enemy", 20)
        ally, enemy = combat.rounds(self.ally, self.enemy)
        self.assertTrue(enemy.is_alive())
        self.assertFalse(ally.is_alive())
