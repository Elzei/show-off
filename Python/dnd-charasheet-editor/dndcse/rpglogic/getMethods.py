__author__ = 'jedrzej.polaczek'

"""
Module name: getMethods
Module destiny: Module contains methods to getting values.
Author: Jedrzej Polaczek
Las modification: 30-08-2016
Last modification author: Jedrzej Polaczek
"""

import random

class DndHelper:
    """
    Static method to returning value of character attribute modifier.
    """
    @staticmethod
    def get_attribute_modifier(attribute):
        return ((- 5) + (int(attribute / 2)))

    """
    Static method to returning value of character proficiency bonus.
    """
    @staticmethod
    def get_proficiency_bonus(level):
        return 2+int(level)/5

    """
    Static method to returning value of character skill.
    """
    @staticmethod
    def get_skill_value(skill, proficiency_list, attribute, character_lvl):
        return DndHelper.get_proficiency_bonus(character_lvl) + DndHelper.get_attribute_modifier(attribute) \
               if skill in proficiency_list \
               else DndHelper.get_attribute_modifier(attribute)

    """
    Static method to returning passive perception.
    """
    @staticmethod
    def get_passive_perception(attribute):
        return 10 + DndHelper.get_attribute_modifier(attribute)

    """
    Static method to returning value of character saving throw.
    Method get_saving_throw is alias on method get_skill_value.
    """
    get_saving_throw = get_skill_value

    """
    Static method to returning temporary value of character hit points. Method convert input value to int because
    hit points must be Integer numbers.
    """
    @staticmethod
    def get_temp_hit_points(max_hit_points, modyficator):
        return int(max_hit_points + modyficator)

    """
    Static method to returning current value of character hit points.
    Method get_current_hit_points is alias on method get_temp_hit_points.
    """
    get_current_hit_points = get_temp_hit_points

    """
    Static method to returning current value of character initiative.
    Method get_initiative is alias on method get_attribute_modifier.
    """
    get_initiative = get_attribute_modifier

    """
    Static method to returning current value of character speed.
    """
    @staticmethod
    def get_speed(race, character_class, armor_medium_heavy=False):
        speed = 0
        if race == "Dwarf" or race == "Gnome" or race == "Halfings":
            if armor_medium_heavy and race == "Dwarf":
                speed = 20
            elif armor_medium_heavy:
                speed = 15
            else:
                speed = 20
        else:
            if armor_medium_heavy:
                speed = 20
            else:
                speed = 30
        if "Monk" in character_class:
            if character_class["Monk"]["level"] in range (2,5):
                speed += 10
            elif character_class["Monk"]["level"] in range (6,9):
                speed += 15
            elif character_class["Monk"]["level"] in range (10,13):
                speed += 20
            elif character_class["Monk"]["level"] in range (14,17):
                speed += 25
            elif character_class["Monk"]["level"] in range (18,20):
                speed += 30
        return int(speed)

    """
    Static method to returning value of character armor class.
    """
    @staticmethod
    def get_armor_class(armor_bonus, armor_max_dex_bonus, shield_bonus, dex, misc_modifiers):
        dex_bonus_final = 0
        if armor_max_dex_bonus <= DndHelper.get_attribute_modifier(dex):
            dex_bonus_final = DndHelper.get_attribute_modifier
        else:
            dex_bonus_final = armor_max_dex_bonus
        return int(10 + armor_bonus + shield_bonus + dex_bonus_final + misc_modifiers)

    """
    Static method to returning value of character maximum hit points.
    character_dice is integer describe highest value of dice ex.: d12 will be 12, d20 will be 20 etc.
    """
    @staticmethod
    def get_max_hit_points(character_level, character_dice):
        character_hp = character_dice
        for current_level in (0, character_level+1):
            character_hp += random.randrange(1, character_dice, 1)

        return character_hp
