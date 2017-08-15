from .equipment import equipmentslot, weapon
from . import dice


class Inventory(object):
    def __init__(self):
        self.equipment = {slot: None for slot in equipmentslot.EquipmentSlot}
        self.equipment[equipmentslot.EquipmentSlot.HANDS] = weapon.Weapon("Unarmed", [dice.Dice(6)])

    def add_equipment(self, equipment):
        self.equipment[equipment.equipment_slot] = equipment

    def remove_equipment(self, slot):
        self.equipment[slot] = None

    def weapon_damage(self):
        weapon_slot = equipmentslot.EquipmentSlot.HANDS
        return self.equipment[weapon_slot].damage()

    def get_total_armor_value(self):
        armor_slot = equipmentslot.EquipmentSlot.CHEST
        return self.equipment[armor_slot].get_armor_bonus()
