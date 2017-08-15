from . import equipmentslot, baseequipment


class Weapon(baseequipment.Equipment):
    def __init__(self, name, damage_dice, equipment_slot=equipmentslot.EquipmentSlot.HANDS):
        super().__init__(name, equipment_slot)
        self.damage_dice = damage_dice

    def damage(self):
        return sum([dice.roll() for dice in self.damage_dice])
