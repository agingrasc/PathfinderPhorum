from typing import Tuple

from . import player


def rounds(ally: player.Player, enemy: player.Player) -> Tuple[player.Player, player.Player]:
    while ally.is_alive() and enemy.is_alive():
        enemy = ally.attack(enemy)
        ally = enemy.attack(ally)

    return ally, enemy
