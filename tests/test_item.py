import pytest

from game.logic.tribute import LIFE_DEFAULT, FORCE_DEFAULT
from game.logic.item import BOW_EFFECT, SPEAR_EFFECT, POTION_FORCE, POTION_LIFE, POTION_POISON, SWORD_EFFECT
from .utils import new_tribute, new_item, new_potion, new_potion_force, new_potion_life, \
    new_potion_poision, new_weapon, new_weapon_sword, new_weapon_spear, new_weapon_bow


def test_create_potion_from_str():
    res = new_item().from_string('p ')
    assert res.__eq__(new_potion())

def test_create_weapon_from_str():
    res = new_item().from_string('w ')
    assert res.__eq__(new_weapon())

def test_potion_apply_effect():
    tribute = new_tribute()
    tribute.life = 75
    tribute.max_life = 100
    potion = new_potion()
    potion.apply_effect(tribute)
    assert tribute.life.__eq__(75 + POTION_LIFE)

    tribute1 = new_tribute()
    tribute1.life = 100
    tribute1.max_life = 100
    potion1 = new_potion()
    potion1.apply_effect(tribute1)
    assert tribute1.life.__eq__(100)

def test_apply_effect_potion_force_life_poison():
    t0 = new_tribute()
    potion_force = new_potion_force()
    potion_force.apply_effect(t0)
    assert t0.force == (FORCE_DEFAULT + POTION_FORCE)
    t0.force = 30
    potion_force.apply_effect(t0)
    assert t0.force == 35

    t1 = new_tribute()
    t1.max_life = 100
    potion_life = new_potion_life()
    potion_life.apply_effect(t1)
    assert t1.life == (LIFE_DEFAULT + POTION_LIFE)
    t1.life = 91
    t1.max_life = 100
    potion_life.apply_effect(t1)
    assert t1.life == 100
    t1.life = 100
    t1.max_life = 100
    potion_life.apply_effect(t1)
    assert t1.life == 100

    t2 = new_tribute()
    poison = new_potion_poision()
    poison.apply_effect(t2)
    assert t2.life == (LIFE_DEFAULT - POTION_POISON)
    t2.life = 3
    poison.apply_effect(t2)
    assert t2.is_dead() is True

def test_create_potion_force_life_poison():
    potion_force = new_potion_force()
    num_potion_force = 10
    potion_force.create_potion(num_potion_force)
    assert potion_force.cant_items == num_potion_force

    potion_life = new_potion_life()
    num_potion_life = 25
    potion_life.create_potion(num_potion_life)
    assert potion_life.cant_items == num_potion_life

    potion_poison = new_potion_poision()
    num_potion_poison = 5
    potion_poison.create_potion(num_potion_poison)
    assert potion_poison.cant_items == num_potion_poison

def test_apply_effect_weapon_sword_spear_bow():
    t0 = new_tribute()
    sword = new_weapon_sword()
    sword.apply_effect(t0)
    assert t0.force == FORCE_DEFAULT + SWORD_EFFECT
    assert t0.weapon is True
    with pytest.raises(ValueError):
        sword.apply_effect(t0)

    t1 = new_tribute()
    spear = new_weapon_spear()
    spear.apply_effect(t1)
    assert t1.range == 2
    assert t1.force == FORCE_DEFAULT + SPEAR_EFFECT
    assert t1.weapon is True
    with pytest.raises(ValueError):
        spear.apply_effect(t1)

    t1.force = 5
    t1.weapon = False
    spear.apply_effect(t1)
    assert t1.force == FORCE_DEFAULT + SPEAR_EFFECT

    t2 = new_tribute()
    bow = new_weapon_bow()
    bow.apply_effect(t2)
    assert t1.range == 3
    assert t2.force == FORCE_DEFAULT + BOW_EFFECT
    assert t2.weapon is True
    with pytest.raises(ValueError):
        bow.apply_effect(t2)

    t2.force = 15
    t2.weapon = False
    bow.apply_effect(t2)
    assert t2.force == 15 + BOW_EFFECT

def test_create_weapon_sword_spear_bow():
    sword = new_weapon_sword()
    sword.create_weapon(15)
    assert sword.cant_items == 15
    spear = new_weapon_spear()
    spear.create_weapon(10)
    assert spear.cant_items == 10
    bow = new_weapon_bow()
    bow.create_weapon(17)
    assert bow.cant_items == 17

def test_potion_get_pos():
    potion = new_potion()
    potion.pos = (1, 1)
    res = potion.get_pos()
    assert res.__eq__((1, 1))

def test_weapon_get_pos():
    weapon = new_weapon()
    weapon.pos = (3, 2)
    res = weapon.get_pos()
    assert res.__eq__((3, 2))