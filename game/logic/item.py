# Object
#  - to string
#  - from string

POTION_EFFECT = 10
WEAPON_EFFECT = 5


class Item:

    def __init__(self):
        self.pos = None

    @staticmethod
    def from_string(object_str):
        if object_str == Potion().__str__():
            return Potion()
        elif object_str == Weapon().__str__():
            return Weapon()
        else:
            raise ValueError(f'Invalid object string: {object_str}')

    def __str__(self):
        raise NotImplementedError

    def set_pos(self, pos):
        self.pos = pos

    def get_pos(self):
        return self.pos

    def apply_effect(tribute):
        raise NotImplementedError


class Potion(Item):

    def __str__(self):
        return 'p'

    def __eq__(self, other):
        return isinstance(other, Potion)

    def apply_effect(self, tribute):
        if tribute.life == tribute.max_life:
            tribute.life += 0
        if tribute.life + POTION_EFFECT > tribute.max_life:
            effect = tribute.max_life - tribute.life
            tribute.life += effect
        if tribute.life + POTION_EFFECT < tribute.max_life:
            tribute.life += POTION_EFFECT


class Weapon(Item):

    def __str__(self):
        return 'w'

    def __eq__(self, other):
        return isinstance(other, Weapon)

    def apply_effect(self, tribute):
        if not tribute.weapon:
            tribute.force += WEAPON_EFFECT
            tribute.weapon = True
        else:
            raise ValueError("Tribute has a weapon already")
