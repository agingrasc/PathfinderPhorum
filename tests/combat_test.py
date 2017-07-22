import unittest
from phorum import combat

class PlayerTest(unittest.TestCase):

    def setUp(self):
        self.ally = combat.Player(12, 10, 10, 6)
        self.ennemy = combat.Player(12, 10, 10, 6)

    def tearDown(self):
        pass

    def test_attack_determinist_target_has_lower_hp(self):
        ennemy = self.ally.attack(self.ennemy)
        self.assertIsNotNone(ennemy)
        self.assertNotEqual(self.ally.hp, ennemy.hp)

    def test_attack_no_attack_if_not_alive(self):
        dead_player = combat.Player(0)
        expected_hp = self.ennemy.hp
        ennemy = dead_player.attack(self.ennemy)
        actual_hp = ennemy.hp
        self.assertEqual(expected_hp, actual_hp)


class CombatTest(unittest.TestCase):

    def setUp(self):
        self.ally = combat.Player(12, 20, 10, 6)
        self.enemy = combat.Player(12, 10, 1, 6)

    def tearDown(self):
        pass

    def test_rounds_determinist_enemy_lose(self):
        ally, enemy = combat.rounds(self.ally, self.enemy)
        self.assertTrue(ally.is_alive())
        self.assertFalse(enemy.is_alive())

    def test_rounds_determinist_ally_lose(self):
        self.ally = combat.Player(5)
        self.enemy = combat.Player(20)
        ally, enemy = combat.rounds(self.ally, self.enemy)
        self.assertTrue(enemy.is_alive())
        self.assertFalse(ally.is_alive())
