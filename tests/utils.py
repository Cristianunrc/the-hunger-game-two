from game.logic.board import Board
from game.logic.tribute import Tribute
from game.logic.district import District
from game.logic.cell import Cell, State
from game.logic.item import Item, Potion, PotionForce, PotionLife, PotionPoison, \
    Weapon, Sword, Spear, Bow

def new_board(row, column):
    return Board(row, column)

def new_tribute():
    return Tribute()

def new_district():
    return District()

def new_cell():
    return Cell()

def new_item():
    return Item()

def new_potion():
    return Potion()

def new_potion_force():
    return PotionForce()

def new_potion_life():
    return PotionLife()

def new_potion_poision():
    return PotionPoison()

def new_weapon():
    return Weapon()

def new_weapon_sword():
    return Sword()

def new_weapon_spear():
    return Spear()

def new_weapon_bow():
    return Bow()

def state_free():
    return State.FREE

def state_item():
    return State.ITEM

def state_tribute():
    return State.TRIBUTE