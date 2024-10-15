import pytest

from .utils import new_board, new_tribute, new_weapon, state_free, state_tribute

def test_create_tribute_error():
    with pytest.raises(ValueError):
        res = new_tribute().from_string('-')

def test_tribute_is_dead_or_is_alive():
    tribute = new_tribute()
    tribute.life = 0
    assert tribute.is_dead().__eq__(True)
    tribute.life = 10
    assert tribute.is_alive().__eq__(True)

def test_tribute_to_string():
    tribute1 = new_tribute()
    tribute1.name = 't0'
    tribute1.set_config_parameters(50, 5, 3, 0, 0)
    assert (tribute1.__str__()).__eq__('t0')

def test_set_config_parameters_tribute():
    tribute = new_tribute()
    tribute.set_config_parameters(50, 5, 3, 5, 3)
    assert tribute.life == 50
    assert tribute.force == 5
    assert tribute.alliance == 3
    assert tribute.district == 5
    assert tribute.cowardice == 3

def test_attack_to():
    board = new_board(3, 3)
    t1 = new_tribute()
    t2 = new_tribute()
    t3 = new_tribute()
    t1.district = 1
    t2.district = 2
    t1.life = 100
    t2.life = 100
    t1.force = 10
    t2.force = 10
    board.put_tribute(2, 2, t3)
    board.put_tribute(0, 0, t1)
    board.put_tribute(1, 0, t2)
    before_life = t2.life
    t1.attack_to(t2)
    assert t2.life == (before_life - t1.force)

def test_of_alliance_to():
    tribute1 = new_tribute()
    tribute_neutral = new_tribute()
    tribute1.district = 1
    tribute_neutral.district = 2
    with pytest.raises(ValueError):
        tribute1.alliance_to(tribute_neutral)
    tribute1.alliance = -25
    n1 = new_tribute()
    tribute1.alliance_to(n1)
    assert n1.enemy == tribute1

def test_generates_alliance_value():
    tribute1 = new_tribute()
    tribute1.alliance = 10
    neutral_value = 5
    assert tribute1.generates_alliance_value(tribute1.alliance, neutral_value) is True
    tribute1.alliance = 10
    neutral_value = 1
    assert (tribute1.generates_alliance_value(tribute1.alliance, neutral_value)) is False

def test_move_to_random():
    board = new_board(3, 3)
    tribute = new_tribute()
    board.put_tribute(1, 1, tribute)
    initial_pos = board.get_pos(tribute)
    tribute.move_to_random(board)
    new_pos = board.get_pos(tribute)
    assert board.get_element(initial_pos[0], initial_pos[1]).get_state() == state_free()
    assert initial_pos != new_pos
    assert board.get_element(new_pos[0], new_pos[1]).get_state() == state_tribute()
    assert tribute.pos == new_pos
    assert initial_pos != new_pos

def test_move_to():
    board = new_board(3, 3)
    tribute = new_tribute()
    board.put_tribute(1, 1, tribute)
    initial_pos = board.get_pos(tribute)
    x, y = 0, 2
    tribute.move_to(x, y, board)
    new_pos = board.get_pos(tribute)
    assert board.get_element(initial_pos[0], initial_pos[1]).get_state() == state_free()
    assert initial_pos != new_pos
    assert (new_pos[0], new_pos[1]) == (x, y)
    assert board.get_element(x, y).get_state() == state_tribute()
    assert tribute.pos == new_pos
    tribute2 = new_tribute()
    board.put_tribute(1, 1, tribute2)
    board.put_item(2, 2, new_weapon())
    tribute2.move_to(2, 2, board)

def test_move_closer_to():
    board = new_board(5, 5)
    tribute = new_tribute()
    board.put_tribute(1, 1, tribute)
    (x, y) = tribute.return_clossest(1, 2, board)
    tribute.move_to(x, y, board)
    assert tribute.pos == (1, 2)
    (x, y) = tribute.return_clossest(4, 4, board)
    tribute.move_to(x, y, board)
    (x, y) = tribute.return_clossest(4, 4, board)
    tribute.move_to(x, y, board)
    (x, y) = tribute.return_clossest(4, 4, board)
    tribute.move_to(x, y, board)
    assert tribute.pos == (4, 4)

def test_tribute_vision_pos():
    board = new_board(7, 7)
    t1 = new_tribute()
    t1.pos = (3, 3)
    visible_positions = t1.tribute_vision_pos(board)
    assert len(visible_positions) == 48
    for x in range(6):
        for y in range(6):
            if x != 3 and y != 3:
                assert (x, y) in visible_positions
                assert (x, y) in visible_positions
                assert (x, y) in visible_positions
                assert (x, y) in visible_positions
                assert (x, y) in visible_positions
                assert (x, y) in visible_positions
                assert (x, y) in visible_positions

def test_tribute_vision_pos_with_tribute_in_border():
    board = new_board(7, 7)
    t1 = new_tribute()
    t1.pos = (0, 0)
    visible_positions = t1.tribute_vision_pos(board)
    assert len(visible_positions) == 15

def test_neighbors():
    board = new_board(5, 5)
    t1 = new_tribute()
    board.put_tribute(2, 2, t1)
    neighbors = t1.get_neighbors_2_distance_free(board)
    assert len(neighbors) == 16
    t2 = new_tribute()
    board.put_tribute(2, 4, t2)
    neighbors = t1.get_neighbors_2_distance_free(board)
    assert len(neighbors) == 15

def test_calculate_flee():
    board = new_board(5, 5)
    t0 = new_tribute()
    t0.set_config_parameters(50, 5, 3, 0, 0)
    board.put_tribute(0, 0, t0)
    t1 = new_tribute()
    t1.set_config_parameters(50, 5, 3, 1, 0)
    board.put_tribute(2, 2, t1)
    pos = t1.calculate_flee(t0, board)
    assert pos == (4, 4)
    t2 = new_tribute()
    t2.set_config_parameters(50, 5, 3, 1, 0)
    board.put_tribute(4, 4, t2)
    pos = t1.calculate_flee(t2, board)
    assert pos == (0, 1)