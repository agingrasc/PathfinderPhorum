import random
from typing import Tuple

SEED = 1

class Player():

    def __init__(self, hp, ac=10, bab=0, damage_die=6):
        self.hp = hp
        self.ac = ac
        self.bab = bab
        self.damage_die = damage_die

    def attack(self, target):
        if self.is_alive():
            random.seed(SEED)
            dmg = random.randint(0, self.damage_die)
            target.hp -= dmg
        return target

    def is_alive(self):
        return self.hp > 0

    def __eq__(self, other):
        return self.hp == other.hp and self.ac == other.ac and self.bab == other.bab

    def __repr__(self):
        return "Player({}, {}, {}, {})".format(self.hp, self.ac, self.bab, self.damage_die)


def rounds(ally: Player, enemy: Player) -> Tuple[Player, Player]:
    while ally.is_alive() and enemy.is_alive():
        enemy = ally.attack(enemy)
        ally = enemy.attack(ally)

    return ally, enemy
