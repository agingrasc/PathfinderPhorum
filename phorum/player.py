import yaml as yaml_lib

from . import inventory


class PlayerLoader:

    @staticmethod
    def load_from_raw_yaml(raw_yaml, name):
        loaded_yamls = yaml_lib.load(raw_yaml)
        players_yaml = None
        if loaded_yamls:
            players_yaml = [yaml for yaml in loaded_yamls if yaml['name'] == name]

        player = None
        if players_yaml:
            player = Player.load_from_yaml(players_yaml[0])

        if player is None:
            return NullPlayer()

        return player


class Player:

    def __init__(self, name, hp, ac=10, bab=0):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.bab = bab
        self.inventory = inventory.Inventory()

    def attack(self, target):
        if self.is_alive():
            dmg = self._get_damage_done()
            target.hp -= dmg
        return target

    def is_alive(self):
        return self.hp > 0

    def add_equipment(self, equipment):
        self.inventory.add_equipment(equipment)

    def remove_equipment(self, slot):
        self.inventory.remove_equipment(slot)

    def _get_damage_done(self):
        return self.inventory.get_weapon_damage()

    @staticmethod
    def load_from_yaml(yaml):
        """"@rtype Player"""
        return Player(**yaml)

    def __eq__(self, other):
        return self.name == other.name and self.bab == other.bab

    def __repr__(self):
        return "Player({}, {}, {}, {}, {})".format(self.name, self.hp, self.ac, self.bab)


class NullPlayer(Player):

    def __init__(self):
        pass

    def is_alive(self):
        return False

    def attack(self, target):
        return target

    def __eq__(self):
        return False