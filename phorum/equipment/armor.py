from . import equipmentslot, baseequipment


class Armor(baseequipment.Equipment):
    def __init__(self, name, armor_bonus, equipment_slot=equipmentslot.EquipmentSlot.CHEST):
        super().__init__(name, equipment_slot)
        self._armor_bonus = armor_bonus

    def get_armor_bonus(self):
        return self._armor_bonus
