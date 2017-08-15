from . import equipmentslot


class Equipment(object):
    def __init__(self, name, equipment_slot=equipmentslot.EquipmentSlot.CHEST):
        self.name = name
        self.equipment_slot = equipment_slot
