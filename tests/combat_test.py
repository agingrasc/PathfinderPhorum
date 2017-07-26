import unittest

import yaml

from phorum import combat


class PlayerLoaderTest(unittest.TestCase):

    def setUp(self):
        self.player_raw_yaml = yaml.dump([{'name': 'Rotovino',
                                           'hp': 10,
                                           'ac': 10,
                                           'bab': 1,
                                           'damage_die': 6}])
        self.expected_player = combat.Player('Rotovino', 10, 10, 1, 6)
        pass

    def tearDown(self):
        pass

    def test_load_player_is_null_player_on_empty_raw_yaml(self):
        player = combat.PlayerLoader.load_from_raw_yaml(self.player_raw_yaml, '')
        self.assertIsNotNone(player)

    def test_load_player_from_valid_raw_yaml(self):
        player = combat.PlayerLoader.load_from_raw_yaml(self.player_raw_yaml, '')
        self.assertEqual(self.expected_player, player)


class PlayerTest(unittest.TestCase):

    def setUp(self):
        self.ally = combat.Player("ally", 12)
        self.enemy = combat.Player("ally", 12)
        self.player_yaml = {'name': 'Rotovino',
                            'hp': 10,
                            'ac': 10,
                            'bab': 1,
                            'damage_die': 6}

    def tearDown(self):
        pass

    def test_player_is_equal_when_name_are_equals(self):
        player_one = combat.Player('test', 0)
        player_two = combat.Player('test', 0)
        unequal_player_by_name = combat.Player('unequal', 0)
        self.assertEqual(player_one, player_two)
        self.assertNotEqual(player_one, unequal_player_by_name)

    def test_player_is_equal_when_bab_are_equals(self):
        player_one = combat.Player('', 0, bab=1)
        player_two = combat.Player('', 0, bab=1)
        unequal_player_by_bab = combat.Player('', 0, bab=2)
        self.assertEqual(player_one, player_two)
        self.assertNotEqual(player_one, unequal_player_by_bab)

    def test_attack_target_has_lower_hp(self):
        old_enemy_hp = self.enemy.hp
        enemy = self.ally.attack(self.enemy)
        new_enemy_hp = enemy.hp
        self.assertIsNotNone(enemy)

        if new_enemy_hp >= old_enemy_hp:
            self.fail()

    def test_attack_no_attack_if_not_alive(self):
        dead_player = combat.Player("dead", 0)
        expected_hp = self.enemy.hp
        ennemy = dead_player.attack(self.enemy)
        actual_hp = ennemy.hp
        self.assertEqual(expected_hp, actual_hp)

    def test_load_from_valid_yaml_player_is_not_none(self):
        player = combat.Player.load_from_yaml(self.player_yaml)
        self.assertIsNotNone(player)

    def test_load_from_valid_yaml_player_has_same_attributes(self):
        expected_player = combat.Player('Rotovino', 10, 10, 1, 6)
        player = combat.Player.load_from_yaml(self.player_yaml)
        self.assertEqual(expected_player, player)


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
