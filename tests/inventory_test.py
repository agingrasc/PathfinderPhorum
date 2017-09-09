import unittest

from phorum import inventory, dice
from phorum.equipment import armor, weapon, equipmentslot


class InventoryTest(unittest.TestCase):

    def setUp(self):
        self.base_inventory = inventory.Inventory()

    def tearDown(self):
        pass

    def test_add_equipment_replaces_correct_slot(self):
        sword = weapon.Weapon("ashbringer", [dice.Dice(12, 12)])
        self.base_inventory.add_equipment(sword)

        self.assertIsNotNone(self.base_inventory.equipment[equipmentslot.EquipmentSlot.HANDS])
        self.assertIsNone(self.base_inventory.equipment[equipmentslot.EquipmentSlot.CHEST])

    def test_remove_equipment_removes_correct_slot(self):
        sword = weapon.Weapon("ashbringer", [dice.Dice(12, 12)])
        shirt = armor.Armor("shirt", 2)
        self.base_inventory.add_equipment(sword)
        self.base_inventory.add_equipment(shirt)

        self.base_inventory.remove_equipment(equipmentslot.EquipmentSlot.CHEST)

        self.assertIsNotNone(self.base_inventory.equipment[equipmentslot.EquipmentSlot.HANDS])
        self.assertIsNone(self.base_inventory.equipment[equipmentslot.EquipmentSlot.CHEST])

    def test_get_weapon_damage_returns_correct_damage(self):
        sword = weapon.Weapon("ashbringer", [dice.Dice(12, 12)])
        self.base_inventory.add_equipment(sword)

        damage = self.base_inventory.weapon_damage()

        self.assertEqual(12, damage)

    def test_given_inventory_with_an_armor_when_compute_effective_armor_class_then_return_armor_class(self):
        shirt = armor.Armor("shirt", 2)
        self.base_inventory.add_equipment(shirt)

        bonus = self.base_inventory.compute_normal_armor_class()

        self.assertEqual(2, bonus)
