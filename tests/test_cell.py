import pytest

from .utils import new_cell, new_tribute, new_item, new_weapon, new_potion, \
    state_tribute, state_item, state_free


def test_cell_initial_state():
    cell = new_cell()
    assert cell.get_state() == state_free()
    with pytest.raises(ValueError):
        cell.get_item()
    with pytest.raises(ValueError):
        cell.get_tribute()

def test_put_and_remove_tribute():
    cell = new_cell()
    tribute = new_tribute()
    cell.put_tribute(tribute)
    assert cell.get_state() == state_tribute()
    assert cell.get_tribute() == tribute
    cell.remove_tribute()
    assert cell.get_state() == state_free()
    with pytest.raises(ValueError):
        cell.get_tribute()

def test_put_and_remove_item():
    cell = new_cell()
    item = new_item()
    cell.put_item(item)
    assert cell.get_state() == state_item()
    assert cell.get_item() == item
    cell.remove_item()
    assert cell.get_state() == state_free()
    with pytest.raises(ValueError):
        cell.get_item()

def test_put_item_on_top_of_tribute():
    cell = new_cell()
    tribute = new_tribute()
    cell.put_tribute(tribute)
    item = new_item()
    with pytest.raises(ValueError):
        cell.put_item(item)

def test_put_tribute_on_top_of_item():
    cell = new_cell()
    item = new_item()
    cell.put_item(item)
    assert cell.get_item() == item

def test_remove_item_when_no_item():
    cell = new_cell()
    with pytest.raises(ValueError):
        cell.remove_item()

def test_remove_tribute_when_no_tribute():
    cell = new_cell()
    with pytest.raises(ValueError):
        cell.remove_tribute()

def test_item_and_tribute_interaction():
    cell = new_cell()
    item = new_item()
    tribute = new_tribute()
    # Coloca un ítem y verifica que esté en la celda
    cell.put_item(item)
    assert cell.get_state() == state_item()
    assert cell.get_item() == item
    # Intenta colocar un tributo y verifica que se cambie el state
    cell.put_tribute(tribute)
    assert cell.get_item() == item
    assert cell.get_tribute() == tribute
    assert cell.state == state_tribute()
    # Elimina el ítem y verifica que la celda aun tiene tribute 
    cell.remove_item()
    assert cell.get_state() == state_tribute()
    with pytest.raises(ValueError):
        cell.get_item()
    # Intenta colocar un ítem y verifica que se lance una excepción
    with pytest.raises(ValueError):
        cell.put_item(item)
    # Elimina el tributo y verifica que la celda vuelva a estar libre
    cell.remove_tribute()
    assert cell.get_state() == state_free()
    with pytest.raises(ValueError):
        cell.get_tribute()

def test_string_representation():
    cell = new_cell()
    assert str(cell) == '  '
    weapon = new_weapon()
    cell.put_item(weapon)
    assert str(cell) == weapon.__str__()
    potion = new_potion()
    cell.remove_item()
    cell.put_item(potion)
    assert str(cell) == potion.__str__()