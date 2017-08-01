import unittest

from phorum import inventory, dice
from phorum.equipment import weapon, equipmentslot


class InventoryTest(unittest.TestCase):

    def setUp(self):
        self.base_inventory = inventory.Inventory()

    def tearDown(self):
        pass

    def test_add_equipment_replaces_correct_slot(self):
        sword = weapon.Weapon("ashbringer", [dice.Dice(12, 12)])
        self.base_inventory.add_equipment(sword)

        self.assertEqual(sword, self.base_inventory.equipment[equipmentslot.EquipmentSlot.HANDS])
        self.assertTrue(self.base_inventory.equipment[equipmentslot.EquipmentSlot.CHEST] is None)

    def test_remove_equipment_removes_correct_slot(self):
        sword = weapon.Weapon("ashbringer", [dice.Dice(12, 12)])
        shoulderblade = weapon.Weapon("shoulderblade", [dice.Dice(12, 12)], equipmentslot.EquipmentSlot.CHEST)
        self.base_inventory.add_equipment(sword)
        self.base_inventory.add_equipment(shoulderblade)

        self.base_inventory.remove_equipment(equipmentslot.EquipmentSlot.CHEST)

        self.assertEqual(sword, self.base_inventory.equipment[equipmentslot.EquipmentSlot.HANDS])
        self.assertTrue(self.base_inventory.equipment[equipmentslot.EquipmentSlot.CHEST] is None)

    def test_get_weapon_damage_returns_correct_damage(self):
        sword = weapon.Weapon("ashbringer", [dice.Dice(12, 12)])
        self.base_inventory.add_equipment(sword)

        damage = self.base_inventory.get_weapon_damage()

        self.assertEqual(12, damage)
