import unittest
from phorum import combat

class PlayerTest(unittest.TestCase):

    def setUp(self):
        self.ally = combat.Player("ally", 12)
        self.enemy = combat.Player("ally", 12)

    def tearDown(self):
        pass

    def test_attack_target_has_lower_hp(self):
        old_enemy_hp = self.enemy.hp
        enemy = self.ally.attack(self.enemy)
        new_enemy_hp = enemy.hp
        self.assertIsNotNone(enemy)
        self.assertTrue(new_enemy_hp < old_enemy_hp)

    def test_attack_no_attack_if_not_alive(self):
        dead_player = combat.Player("dead", 0)
        expected_hp = self.enemy.hp
        enemy = dead_player.attack(self.enemy)
        actual_hp = enemy.hp
        self.assertEqual(expected_hp, actual_hp)


class CombatTest(unittest.TestCase):

    def setUp(self):
        self.ally = combat.Player(12, 20, 10, 6)
        self.enemy = combat.Player(12, 10, 1, 6)

    def tearDown(self):
        pass

    def test_rounds_enemy_lose(self):
        ally, enemy = combat.rounds(self.ally, self.enemy)
        self.assertTrue(ally.is_alive())
        self.assertFalse(enemy.is_alive())

    def test_rounds_ally_lose(self):
        self.ally = combat.Player("ally", 5)
        self.enemy = combat.Player("enemy", 20)
        ally, enemy = combat.rounds(self.ally, self.enemy)
        self.assertTrue(enemy.is_alive())
        self.assertFalse(ally.is_alive())
