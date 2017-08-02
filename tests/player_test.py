import unittest

import yaml

from phorum import player, dice
from phorum.equipment import weapon


class PlayerLoaderTest(unittest.TestCase):

    def setUp(self):
        player_one_yaml = {'name': 'Rotovino',
                           'hp': 10,
                           'ac': 10,
                           'bab': 1}
        player_two_yaml = {'name': 'Fubar',
                           'hp': 12,
                           'ac': 10,
                           'bab': 0}
        self.player_single_raw_yaml = yaml.dump([player_one_yaml])
        self.player_multi_raw_yaml = yaml.dump([player_one_yaml, player_two_yaml])
        self.expected_player_one = player.Player('Rotovino', 10, 10, 1)
        self.expected_player_two = player.Player('Fubar', 12, 10, 0)
        pass

    def tearDown(self):
        pass

    def test_load_player_is_null_player_on_empty_raw_yaml(self):
        null_player = player.PlayerLoader.load_from_raw_yaml('', '')
        self.assertEqual(player.NullPlayer, type(null_player))

    def test_load_player_is_not_null_player_on_valid_raw_yaml(self):
        not_null_player = player.PlayerLoader.load_from_raw_yaml(self.player_single_raw_yaml, 'Rotovino')
        self.assertIsNotNone(not_null_player)
        self.assertNotEqual(player.NullPlayer, type(not_null_player))

    def test_load_player_from_valid_raw_yaml(self):
        valid_player = player.PlayerLoader.load_from_raw_yaml(self.player_single_raw_yaml, 'Rotovino')
        self.assertEqual(self.expected_player_one, valid_player)

    def test_load_player_is_not_first_player_from_valid_multi_raw_yaml(self):
        second_player_from_raw = player.PlayerLoader.load_from_raw_yaml(self.player_multi_raw_yaml, 'Fubar')
        self.assertNotEqual(self.expected_player_one, second_player_from_raw)

    def test_load_player_is_second_player_from_valid_multi_raw_yaml(self):
        second_player_from_raw = player.PlayerLoader.load_from_raw_yaml(self.player_multi_raw_yaml, 'Fubar')
        self.assertEqual(self.expected_player_two, second_player_from_raw)

    def test_load_player_has_a_dice(self):
        expected_dice_type = dice.Dice
        player_dice_type = type(self.expected_player_one.damage_die)
        self.assertEqual(expected_dice_type, player_dice_type)


class PlayerTest(unittest.TestCase):

    def setUp(self):
        self.ally = player.Player("ally", 12)
        self.enemy = player.Player("ennemy", 12)
        self.player_yaml = {'name': 'Rotovino',
                            'hp': 10,
                            'ac': 10,
                            'bab': 1}

    def tearDown(self):
        pass

    def test_player_is_equal_when_name_are_equals(self):
        player_one = player.Player('test', 0)
        player_two = player.Player('test', 0)
        unequal_player_by_name = player.Player('unequal', 0)
        self.assertEqual(player_one, player_two)
        self.assertNotEqual(player_one, unequal_player_by_name)

    def test_player_is_equal_when_bab_are_equals(self):
        player_one = player.Player('', 0, bab=1)
        player_two = player.Player('', 0, bab=1)
        unequal_player_by_bab = player.Player('', 0, bab=2)
        self.assertEqual(player_one, player_two)
        self.assertNotEqual(player_one, unequal_player_by_bab)

    def test_attack_target_has_lower_hp(self):
        old_enemy_hp = self.enemy.hp
        enemy = self.ally.attack(self.enemy)
        new_enemy_hp = enemy.hp
        self.assertIsNotNone(enemy)
        self.assertTrue(new_enemy_hp < old_enemy_hp)

    def test_attack_no_attack_if_not_alive(self):
        dead_player = player.Player("dead", 0)
        expected_hp = self.enemy.hp
        enemy = dead_player.attack(self.enemy)
        actual_hp = enemy.hp
        self.assertEqual(expected_hp, actual_hp)

    def test_load_from_valid_yaml_player_is_not_none(self):
        not_null_player = player.Player.load_from_yaml(self.player_yaml)
        self.assertIsNotNone(not_null_player)

    def test_load_from_valid_yaml_player_has_same_attributes(self):
        expected_player = player.Player('Rotovino', 10, 10, 1)
        not_null_player = player.Player.load_from_yaml(self.player_yaml)
        self.assertEqual(expected_player, not_null_player)

    def test_attack_with_weapon_gives_weapon_damage(self):
        sword = weapon.Weapon("ashbringer", [dice.Dice(10, 10)])
        self.ally.add_equipment(sword)
        self.ally.attack(self.enemy)
        self.assertEqual(2, self.enemy.hp)
