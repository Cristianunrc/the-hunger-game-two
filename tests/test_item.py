import pytest

from game.logic.tribute import Tribute, LIFE_DEFAULT, FORCE_DEFAULT
from game.logic.item import BOW_EFFECT, SPEAR_EFFECT, Item, Potion, PotionForce, PotionLife, PotionPoison, \
    Weapon, Sword, Spear, Bow, POTION_FORCE, POTION_LIFE, POTION_POISON, SWORD_EFFECT

def new_tribute():
    return Tribute()

def test_create_potion_from_str():
    res = Item.from_string('p ')
    assert res.__eq__(Potion())

def test_create_weapon_from_str():
    res = Item.from_string('w ')
    assert res.__eq__(Weapon())

def test_potion_apply_effect():
    tribute = new_tribute()
    tribute.life = 75
    tribute.max_life = 100
    potion = Potion()
    potion.apply_effect(tribute)
    assert tribute.life.__eq__(75 + POTION_LIFE)

    tribute1 = new_tribute()
    tribute1.life = 100
    tribute1.max_life = 100
    potion1 = Potion()
    potion1.apply_effect(tribute1)
    assert tribute1.life.__eq__(100)

def test_apply_effect_potion_force_life_poison():
    t0 = new_tribute()
    potion_force = PotionForce()
    potion_force.apply_effect(t0)
    assert t0.force == (FORCE_DEFAULT + POTION_FORCE)
    t0.force = 30
    potion_force.apply_effect(t0)
    assert t0.force == 35

    t1 = new_tribute()
    t1.max_life = 100
    potion_life = PotionLife()
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
    poison = PotionPoison()
    poison.apply_effect(t2)
    assert t2.life == (LIFE_DEFAULT - POTION_POISON)
    t2.life = 3
    poison.apply_effect(t2)
    assert t2.is_dead() is True

def test_create_potion_force_life_poison():
    potion_force = PotionForce()
    num_potion_force = 10
    potion_force.create_potion(num_potion_force)
    assert potion_force.cant_items == num_potion_force

    potion_life = PotionLife()
    num_potion_life = 25
    potion_life.create_potion(num_potion_life)
    assert potion_life.cant_items == num_potion_life

    potion_poison = PotionPoison()
    num_potion_poison = 5
    potion_poison.create_potion(num_potion_poison)
    assert potion_poison.cant_items == num_potion_poison

def test_apply_effect_weapon_sword_spear_bow():
    t0 = new_tribute()
    sword = Sword()
    sword.apply_effect(t0)
    assert t0.force == FORCE_DEFAULT + SWORD_EFFECT
    assert t0.weapon is True
    with pytest.raises(ValueError):
        sword.apply_effect(t0)

    t1 = new_tribute()
    spear = Spear()
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
    bow = Bow()
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
    sword = Sword()
    sword.create_weapon(15)
    assert sword.cant_items == 15
    spear = Spear()
    spear.create_weapon(10)
    assert spear.cant_items == 10
    bow = Bow()
    bow.create_weapon(17)
    assert bow.cant_items == 17

def test_potion_get_pos():
    potion = Potion()
    potion.pos = (1, 1)
    res = potion.get_pos()
    assert res.__eq__((1, 1))

def test_weapon_get_pos():
    weapon = Weapon()
    weapon.pos = (3, 2)
    res = weapon.get_pos()
    assert res.__eq__((3, 2))