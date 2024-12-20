import pytest

from game.logic.game_logic import GameLogic, GameMode
from game.logic.district import DISTRICT_DEFAULT
from main import init_simulation
from .utils import new_tribute, new_weapon, new_potion, new_district, state_free, \
    state_tribute, new_weapon_sword, new_weapon_spear, new_weapon_bow, new_potion_poision, \
    new_potion_force, new_potion_life

@pytest.fixture
def game():
    game = GameLogic()
    game.new_game(5, 5)
    t1 = new_tribute()
    t2 = new_tribute()
    t3 = new_tribute()
    w1 = new_weapon()
    p1 = new_potion()
    game.board.put_tribute(2, 2, t1)
    game.board.put_tribute(1, 1, t2)
    game.board.put_tribute(3, 3, t3)
    game.board.put_item(4, 4, w1)
    game.board.put_item(4, 3, p1)
    return game

@pytest.fixture
def game2x2():
    game2x2 = GameLogic()
    game2x2.new_game(2, 2)
    district0 = new_district()
    district1 = new_district()
    t0 = new_tribute()
    t1 = new_tribute()
    district0.number_district = 0
    district1.number_district = 1
    game2x2.districts.append(district0)
    game2x2.districts.append(district1)
    t0.set_config_parameters(50, 20, 1, 0, 0)
    t1.set_config_parameters(50, 20, 1, 1, 0)
    game2x2.board.put_tribute(0, 0, t0)
    game2x2.board.put_tribute(0, 1, t1)
    district0.add_tribute(t0)
    district1.add_tribute(t1)
    return game2x2

def test_from_string_and_to_string():
    game = GameLogic()
    board_str = 't3|t2\n' \
                't4|t1\n' \
                'n4|n1'
    game.from_string(board_str)
    assert board_str == game.to_string()
    assert len(game.districts[1].tributes) == 1
    assert len(game.districts[2].tributes) == 1
    assert len(game.districts[3].tributes) == 1
    assert len(game.districts[4].tributes) == 1
    assert len(game.neutrals) == 2
    t1 = game.board.get_element(1, 1).get_tribute()
    game.remove_tribute(t1)
    assert len(game.districts[1].tributes) == 0

def test_put_neutral(game2x2):
    game2x2.put_neutral(1, 0)
    game2x2.put_neutral(1, 1)
    neutral = game2x2.board.get_element(1, 0).get_tribute()
    neutral1 = game2x2.board.get_element(1, 1).get_tribute()
    assert neutral.name == 'n0'
    assert neutral1.name == 'n1'
    assert neutral.life == 50
    assert neutral.force == 5
    assert neutral.pos == (1, 0)
    assert neutral.district is None
    assert neutral.cowardice == 0
    assert len(game2x2.neutrals) == 2

def test_remove_tribute1():
    game = GameLogic()
    game.new_game(3, 3)
    t0 = new_tribute()
    t1 = new_tribute()
    t2 = new_tribute()
    t0.set_config_parameters(50, 5, 3, 0, 0)
    t1.set_config_parameters(51, 5, 3, 0, 0)
    t2.set_config_parameters(52, 5, 3, 0, 0)
    game.put_tribute(0, 0, t0)
    game.put_tribute(0, 1, t1)
    game.put_tribute(1, 0, t2)
    game.remove_tribute(t1)
    free = game.board.get_element(0, 1).get_state()
    assert free == state_free()

def test_tribute_vision_cells_with_a_cells():
    game = GameLogic()
    game.new_game(3, 3)
    tribute1 = new_tribute()
    game.board.put_tribute(1, 1, tribute1)
    tribute_vision_cells = tribute1.tribute_vision_cells(game.board)
    assert len(tribute_vision_cells) == 8
    assert game.board.get_element(0, 0) in tribute_vision_cells
    assert game.board.get_element(0, 1) in tribute_vision_cells
    assert game.board.get_element(0, 2) in tribute_vision_cells
    assert game.board.get_element(1, 0) in tribute_vision_cells
    assert game.board.get_element(1, 2) in tribute_vision_cells
    assert game.board.get_element(2, 0) in tribute_vision_cells
    assert game.board.get_element(2, 1) in tribute_vision_cells
    assert game.board.get_element(2, 2) in tribute_vision_cells

def test_get_adjacents_cells_complex():
    game = GameLogic()
    game.new_game(8, 8)
    x, y = 0, 0
    game.board.put_tribute(1, 0, new_tribute())
    game.board.put_tribute(0, 1, new_tribute())
    game.board.put_tribute(1, 1, new_tribute())
    adjacent_cells = game.board.get_adjacents_cells(x, y)
    assert len(adjacent_cells) == 3
    assert game.board.get_element(0, 1) in adjacent_cells
    assert game.board.get_element(1, 0) in adjacent_cells
    assert game.board.get_element(1, 1) in adjacent_cells
    # Modifica el cuarto assert
    assert len([cell for cell in adjacent_cells if cell.get_pos() == (7, 7)]) == 0
    with pytest.raises(ValueError):
        game.board.get_adjacents_cells(-1, 1)

def test_get_tribute_closenes_complex():
    game = GameLogic()
    game.new_game(3, 3)
    t1 = new_tribute()
    t2 = new_tribute()
    neutro = new_tribute()
    w = new_weapon()
    p = new_potion()
    t1.set_config_parameters(50, 5, 1, 1, 2)
    t2.set_config_parameters(50, 5, 1, 2, 3)
    game.board.put_tribute(1, 1, t1)
    game.board.put_tribute(0, 1, t2)
    game.board.put_item(2, 1, w)
    game.board.put_item(1, 0, p)
    game.board.put_tribute(1, 2, neutro)
    assert game.tribute_vision_closeness(t1).pos == (2, 1)
    game.board.remove_item(w)
    assert game.tribute_vision_closeness(t1).pos == (1, 0)
    game.board.remove_item(p)
    assert game.tribute_vision_closeness(t1).pos == (1, 2)
    game.board.remove_tribute(neutro)
    assert game.tribute_vision_closeness(t1).pos == (0, 1)
    game.board.remove_tribute(t2)
    result = game.tribute_vision_closeness(t1)
    assert result is False
    t2.district = 1
    game.board.put_tribute(2, 2, t2)
    assert game.tribute_vision_closeness(t1) is False
    w1 = new_weapon()
    game.board.put_item(2, 1, w1)
    assert game.tribute_vision_closeness(t1).pos == (2, 1)

def test_fight_2_tributes_and_one_died():
    game = GameLogic()
    game.new_game(2, 2)
    t1 = new_tribute()
    t2 = new_tribute()
    t1.set_config_parameters(40, 20, 1, 0, 1)
    t2.set_config_parameters(40, 20, 1, 1, 2)
    game.put_tribute(0, 0, t1)
    game.put_tribute(0, 1, t2)
    game.fight(t1, t2)
    assert t2.life == 20
    game.fight(t2, t1)
    assert t1.life == 20
    assert t2 in game.districts[1].tributes
    game.fight(t1, t2)
    assert t2.is_dead()
    assert game.board.get_element(0, 1).get_state() == state_free()
    assert not (t2 in game.districts[1].tributes)

def test_heuristic_tribute_weapons_items():
    game = GameLogic()
    game.new_game(7, 7)
    t0 = new_tribute()
    t0.set_config_parameters(50, 5, 3, 0, 0)
    game.put_tribute(3, 3, t0)
    sw = new_weapon_sword()
    game.put_item(2, 2, sw)
    game.heuristic_tribute(t0)
    assert t0.weapon
    t0.weapon = False
    t0.force = 5
    sp = new_weapon_spear()
    game.put_item(3, 3, sp)
    game.heuristic_tribute(t0)
    assert t0.weapon
    assert t0.range == 2
    assert t0.force == 8
    t0.weapon = False
    t0.range = 1
    t0.force = 5
    bow = new_weapon_bow()
    game.put_item(2, 2, bow)
    game.heuristic_tribute(t0)
    assert t0.weapon
    assert t0.range == 3
    assert t0.force == 6
    po = new_potion_poision()
    game.put_item(3, 3, po)
    game.heuristic_tribute(t0)
    pl = new_potion_life()
    assert t0.life == 45
    game.put_item(3, 4, pl)
    game.heuristic_tribute(t0)
    assert t0.life == 50
    pf = new_potion_force()
    game.put_item(3, 5, pf)
    game.heuristic_tribute(t0)
    assert t0.force == 11

def test_figth_weapons():
    game = GameLogic()
    game.new_game(7, 7)
    t0 = new_tribute()
    t0.set_config_parameters(50, 5, 3, 0, 0)
    game.put_tribute(2, 2, t0)
    t1 = new_tribute()
    t1.set_config_parameters(50, 5, 3, 1, 0)
    game.put_tribute(6, 6, t1)
    bow = new_weapon_bow()
    game.put_item(3, 3, bow)
    game.heuristic_tribute(t0)
    assert t0.weapon
    game.heuristic_tribute(t0)
    assert t1.life == 44
    t0.force = 5
    t0.weapon = False
    t0.range = 1
    sp = new_weapon_spear()
    game.put_item(4, 4, sp)
    game.heuristic_tribute(t0)
    assert t0.weapon
    assert t0.range == 2
    game.heuristic_tribute(t0)
    assert t1.life == 36
    t0.force = 5
    t0.weapon = False
    t0.range = 1
    sword = new_weapon_sword()
    game.put_item(5, 5, sword)
    game.heuristic_tribute(t0)
    assert t0.weapon
    assert t0.range == 1
    game.heuristic_tribute(t0)
    assert t1.life == 26

def test_heuristic_tribute_complex():
    game = GameLogic()
    game.new_game(7, 7)
    tribute = new_tribute()
    tribute.set_config_parameters(50, 5, 3, 0, 0)
    game.put_tribute(3, 3, tribute)
    weapon = new_weapon()
    game.board.put_item(4, 3, weapon)
    game.heuristic_tribute(tribute)
    assert tribute.pos == (4, 3)
    assert tribute.force == 10
    tribute1 = new_tribute()
    tribute1.set_config_parameters(50, 5, 5, 1, 0)
    game.put_tribute(4, 2, tribute1)
    game.heuristic_tribute(tribute)
    game.heuristic_tribute(tribute1)
    assert tribute.life == 45
    assert tribute1.life == 40
    game.heuristic_tribute(tribute)
    game.heuristic_tribute(tribute)
    game.heuristic_tribute(tribute)
    game.heuristic_tribute(tribute)
    game.heuristic_tribute(tribute)
    assert tribute.pos != (4, 3)
    game.put_neutral(4, 3)
    tribute.alliance = 25
    game.heuristic_tribute(tribute)
    assert len(game.districts[0].tributes) == 2
    neutral = game.board.get_element(4, 3).get_tribute()
    game.remove_tribute(neutral)
    game.put_neutral(4, 3)
    tribute.alliance = -25
    game.heuristic_tribute(tribute)
    assert len(game.districts[0].tributes) == 1
    assert tribute.enemy is not None

def test_heuristic_tribute_complex2():
    game = GameLogic()
    game.new_game(5, 4)
    tribute0 = new_tribute()
    tribute0.set_config_parameters(50, 5, 25, 0, 0)
    game.board.put_tribute(1, 1, tribute0)
    d0 = new_district()
    d0.number_district = 0
    d0.add_tribute(tribute0)
    game.districts.append(d0)
    t1 = new_tribute()
    t1.set_config_parameters(10, 5, 1, 1, 0)
    game.board.put_tribute(1, 3, t1)
    d1 = new_district()
    d1.number_district = 1
    d1.add_tribute(t1)
    game.districts.append(d1)
    neutro = new_tribute()
    game.board.put_tribute(4, 3, neutro)
    neutro.life = 20
    neutro.force = 10
    game.neutrals.append(neutro)
    w = new_weapon()
    p = new_potion()
    game.board.put_item(2, 3, w)
    game.board.put_item(4, 2, p)
    game.heuristic_tribute(tribute0)
    game.heuristic_tribute(tribute0)
    assert tribute0.pos == w.pos
    assert tribute0.force == 10
    game.heuristic_tribute(tribute0)
    t1.attack_to(tribute0)
    game.heuristic_tribute(tribute0)
    assert tribute0.life == 45
    assert t1.is_dead()
    assert game.board.get_element(1, 3).get_state() == state_free()
    game.heuristic_tribute(tribute0)
    game.heuristic_tribute(tribute0)
    assert tribute0.life == 50
    assert tribute0.pos == p.pos
    game.heuristic_tribute(tribute0)
    assert neutro in game.districts[0].tributes

def test_end_game():
    district1 = new_district()
    district2 = new_district()
    district1.set_config(50, 5, 3, 1, 2, 3)
    district2.set_config(50, 5, 3, 2, 2, 3)
    game = GameLogic()
    game.districts.append(district1)
    assert game.winner_district() == district1.get_number_district()
    game.districts.append(district2)
    assert game.game_ended() is False
    game2 = GameLogic()
    with pytest.raises(ValueError):
        game2.game_ended()
    #assert neutro.district == tribute.district

def test_alliance_neutral_tribute():
    district = new_district()
    district.set_config(50, 6, 4, 0, 1, 2)
    game = GameLogic()
    game.new_game(2, 2)
    game.put_neutral(0, 0)
    neutral = game.neutrals[0]
    game.alliance_neutral(neutral, district)
    assert neutral.district is district.get_number_district()
    assert 1 + 1 == district.get_cant_tribute()
    assert district.tributes.__contains__(neutral)

def test_heuristic_of_game_simple_one(game2x2):
    game2x2.mode = GameMode.SIMULATION
    game2x2.heuristic_of_game()
    assert len(game2x2.districts[0].tributes) == 1
    assert len(game2x2.districts[1].tributes) == 0

def test_heuristic_of_game_simple_two(game2x2):
    w1 = new_weapon()
    game2x2.put_item(1, 0, w1)
    game2x2.mode = GameMode.SIMULATION
    t1 = game2x2.board.get_element(0, 0).get_tribute()
    t2 = game2x2.board.get_element(0, 1).get_tribute()
    game2x2.heuristic_of_game()
    assert t2.is_dead()
    assert t1.force == 25
    assert t1.is_alive()
    assert len(game2x2.districts[0].tributes) == 1
    assert len(game2x2.districts[1].tributes) == 0

def test_heuristic_of_game_simple_three(game2x2):
    p1 = new_potion()
    game2x2.put_item(1, 0, p1)
    game2x2.mode = GameMode.SIMULATION
    t1 = game2x2.board.get_element(0, 0).get_tribute()
    t2 = game2x2.board.get_element(0, 1).get_tribute()
    game2x2.heuristic_of_game()
    assert t2.is_alive()
    assert t1.is_dead()
    assert len(game2x2.districts[0].tributes) == 0
    assert len(game2x2.districts[1].tributes) == 1

def test_heuristic_of_game_simple_four(game2x2):
    neutro = new_tribute()
    neutro.life = 25
    t1 = game2x2.board.get_element(0, 0).get_tribute()
    t2 = game2x2.board.get_element(0, 1).get_tribute()
    t1.alliance = 25
    game2x2.board.put_tribute(1, 0, neutro)
    game2x2.mode = GameMode.SIMULATION
    game2x2.neutrals.append(neutro)
    game2x2.heuristic_of_game()
    assert t1.is_alive()
    assert neutro.life == 25
    assert t2.is_dead()
    assert len(game2x2.districts[0].tributes) == 2
    assert len(game2x2.districts[1].tributes) == 0

def test_heuristic_of_game_simple_five():
    game = GameLogic()
    game.new_game(8, 8)
    game.mode = GameMode.SIMULATION
    t0 = new_tribute()
    t1 = new_tribute()
    t0.set_config_parameters(50, 10, -25, 0, 0)
    t1.set_config_parameters(40, 20, 1, 1, 0)
    game.put_tribute(0, 0, t0)
    game.put_tribute(7, 7, t1)
    game.put_neutral(0, 1)
    game.heuristic_of_game()
    assert len(game.neutrals) == 0
    assert len(game.districts[0].tributes) == 0
    assert len(game.districts[1].tributes) == 1

def test_applies_effects_complex():
    t1 = new_tribute()
    t1.district = 0
    potion = new_potion()
    game = GameLogic()
    game.new_game(2, 2)
    game.put_tribute(0, 0, t1)
    game.put_item(0, 1, potion)
    t1.life = 45
    game.heuristic_tribute(t1)
    assert t1.life == 50
    game.put_item(0, 0, potion)
    game.heuristic_tribute(t1)
    assert t1.life == 50
    game.put_item(0, 1, new_weapon())
    game.heuristic_tribute(t1)
    assert t1.force == 10

#Test for init_simulation in main.py
def test_init_simulation_inputs_one(monkeypatch):
    game = GameLogic()
    user_inputs = iter(['1', '5', '4', '4', '2', '1', 'n'])
    def mock_input(prompt):
        return next(user_inputs)
    monkeypatch.setattr('builtins.input', mock_input)
    init_simulation(15, 15, game)
    my_district = game.districts[0]
    for i in range(len(my_district.tributes)):
        tribute_my_district = my_district.tributes[i]
        assert tribute_my_district.district == 0

#Test for init_simulation in main.py
def test_init_simulation_inputs_two(monkeypatch):
    game = GameLogic()
    user_inputs = iter(['3', '2', '5', '5', '2', '3', 'n'])
    def mock_input(prompt):
        return next(user_inputs)
    monkeypatch.setattr('builtins.input', mock_input)
    init_simulation(15, 15, game)
    my_district = game.districts[0]
    for i in range(len(my_district.tributes)):
        tribute_my_district = my_district.tributes[i]
        assert tribute_my_district.district == 0

def test_put_tribute():
    game = GameLogic()
    game.new_game(2, 2)
    t0 = new_tribute()
    t0.set_config_parameters(50, 10, 4, 0, 0)
    game.put_tribute(0, 0, t0)
    assert t0.name == 't0'
    assert t0.pos == (0, 0)
    assert game.board.get_element(0, 0).get_tribute() == t0
    t1 = new_tribute()
    t1.set_config_parameters(50, 10, 4, 1, 0)
    game.put_tribute(1, 1, t1)
    assert t1.name == 't1'
    assert t1.pos == (1, 1)
    assert game.board.get_element(1, 1).get_tribute() == t1
    assert len(game.districts) == 2
    s1 = new_tribute()
    s1.set_config_parameters(50, 10, 4, 1, 0)
    game.put_tribute(1, 0, s1)
    assert s1.name == 'a1'
    assert s1.pos == (1, 0)
    assert game.board.get_element(1, 0).get_tribute() == s1
    assert len(game.districts[1].tributes) == 2

def test_neutral_heuristic():
    game = GameLogic()
    game.new_game(3, 3)
    t0 = new_tribute()
    t1 = new_tribute()
    t0.set_config_parameters(60, 5, -25, 0, 0)
    t1.set_config_parameters(60, 5, -25, 1, 0)
    game.put_tribute(0, 0, t0)
    game.put_tribute(0, 2, t1)
    game.put_neutral(0, 1)
    game.heuristic_tribute(t0)
    game.heuristic_tribute(t1)
    neutral = game.board.get_element(0, 1).get_tribute()
    game.neutral_heuristic(neutral)
    assert t1.life == 55
    assert t0.life == 60
    game.remove_tribute(t0)
    game.remove_tribute(t1)
    neutral.enemy = None
    game.neutral_heuristic(neutral)
    assert neutral.pos != (0, 1)

def test_order_attack():
    game = GameLogic()
    game.new_game(2, 2)
    t0 = new_tribute()
    t0.set_config_parameters(50, 5, 3, 0, 0)
    game.put_tribute(0, 0, t0)
    t1 = new_tribute()
    t1.set_config_parameters(50, 5, 3, 1, 0)
    game.put_tribute(0, 1, t1)
    t2 = new_tribute()
    t2.set_config_parameters(50, 5, 3, 2, 0)
    game.put_tribute(1, 1, t2)
    game.order_attack()
    assert game.order == [0, 1, 2]
    game.all_iteration()
    assert game.order == [1, 2, 0]
    game.all_iteration()
    assert game.order == [2, 0, 1]
    game.all_iteration()

def test_get_away():
    game = GameLogic()
    game.new_game(5, 5)
    t0 = new_tribute()
    t0.set_config_parameters(50, 5, 3, 0, 0)
    game.put_tribute(0, 0, t0)
    t1 = new_tribute()
    t1.set_config_parameters(50, 5, 3, 1, 0)
    game.put_tribute(0, 1, t1)
    #first iteration, can escape down
    game.heuristic_tribute(t0)
    assert t1.life == 45
    game.get_away(t1, t0)
    assert t1.pos == (2, 3)
    #second, can escape left
    game.remove_tribute(t0)
    game.remove_tribute(t1)
    game.put_tribute(4, 3, t1)
    game.put_tribute(4, 4, t0)
    game.get_away(t1, t0)
    assert t1.pos == (4, 1)
    #third, can escape up left
    game.remove_tribute(t0)
    game.remove_tribute(t1)
    game.put_tribute(4, 3, t0)
    game.put_tribute(4, 4, t1)
    game.get_away(t1, t0)
    assert t1.pos == (2, 2)

def test_heuristic_get_away():
    game = GameLogic()
    game.new_game(6, 6)
    t0 = new_tribute()
    t0.set_config_parameters(50, 5, 3, 0, 0)
    game.put_tribute(0, 0, t0)
    t1 = new_tribute()
    t1.set_config_parameters(50, 5, 3, 1, 1)
    game.put_tribute(0, 1, t1)
    #first iteration, can escape down
    game.one_iteration()
    assert t1.pos == (2, 3)
    assert t1.life == 45
    assert t1.cowardice == 0.5
    game.one_iteration()
    assert t1.pos == (4, 5)
    assert t0.pos == (1, 1)
    assert t1.cowardice == 0

def test_distribute_neutral_tributes():
    game = GameLogic()
    game.new_game(4, 4)
    number_neutrals = 10
    game.distribute_neutral_tributes(number_neutrals)
    neutrals_count = 0
    for row in game.board.board:
        for cell in row:
            if cell.state == state_tribute():
                neutrals_count += 1
    assert neutrals_count == number_neutrals
    assert len(game.neutrals) == number_neutrals

def test_get_tribute_by_name():
    game = GameLogic()
    game.new_game(6, 6)
    t0 = new_tribute()
    t0.set_config_parameters(50, 5, 3, 0, 0)
    game.put_tribute(0, 0, t0)
    assert game.districts[0].tributes[0] == game.get_tribute_by_name('t0')

def test_configure_random_districts():
    game = GameLogic()
    game.configure_random_districts()
    assert len(game.districts) == 5
    for i in range(5):
        district = game.districts[i]
        for j in range(4):
            tribute = district.tributes[j]
            assert tribute.life == 50
            assert tribute.cowardice == 0
            assert tribute.force + tribute.alliance <= 15
        assert district.cant_tributes == 4
        assert district.number_district != 0

def test_one_iteration_front_with_winner_district():
    game = GameLogic()
    game.new_game(3, 3)
    t0 = new_tribute()
    t0.set_config_parameters(10, 5, 3, 0, 0)
    game.put_tribute(1, 1, t0)
    t1 = new_tribute()
    t1.set_config_parameters(50, 10, 3, 1, 0)
    game.put_tribute(2, 2, t1)
    game.winner_district()
    assert game.winner is None
    game.one_iteration_front()
    assert t0.life == 0
    assert t1.life == 45
    game.winner_district()
    assert game.winner == 1

def test_set_parameters_invalid_inputs_catch_except():
    game = GameLogic()
    with pytest.raises(ValueError):
        game.set_parameters("invalidLife", 5, 3, 4, 0)
    with pytest.raises(ValueError):
        game.set_parameters(50, 'invalidForce', 3, 4, 0)
    with pytest.raises(ValueError):
        game.set_parameters(50, 5, '', 4, 0)
    with pytest.raises(ValueError):
        game.set_parameters(50, 5, 3, "invalidTributes", 0)
    with pytest.raises(ValueError):
        game.set_parameters(50, 5, 3, 4, 'a')

def test_set_parameters_invalid_inputs_out_of_range():
    game = GameLogic()
    with pytest.raises(ValueError):
        game.set_parameters(1000, 5, 3, 4, 0)
    with pytest.raises(ValueError):
        game.set_parameters(50, -1, 3, 4, 0)
    with pytest.raises(ValueError):
        game.set_parameters(50, 5, 0, 4, 0)
    with pytest.raises(ValueError):
        game.set_parameters(50, 5, 3, 10, 0)
    with pytest.raises(ValueError):
        game.set_parameters(50, 5, 3, 4, 20)

def test_set_parameters_invalid_inputs_points():
    game = GameLogic()
    with pytest.raises(ValueError):
        game.set_parameters(100, 25, 10, 6, 5)
    with pytest.raises(ValueError):
        game.set_parameters(50, 10, 4, 5, 2)
    with pytest.raises(ValueError):
        game.set_parameters(100, 6, 3, 4, 0)
    with pytest.raises(ValueError):
        game.set_parameters(59, 8, 3, 6, 0)
    with pytest.raises(ValueError):
        game.set_parameters(90, 8, 3, 4, 0)

def test_set_parameters_valid_inputs():
    game = GameLogic()
    game.set_parameters(50, 25, 3, 4, 0)
    own_district = game.districts[0]
    for i in range(own_district.cant_tributes):
        tribute = own_district.tributes[i]
        assert tribute.life == 50
        assert tribute.force == 25
        assert tribute.alliance == 3
        assert tribute.cowardice == 0
        assert tribute.district == DISTRICT_DEFAULT

def test_district_lifes():
    game = GameLogic()
    game.set_parameters(70, 5, 6, 4, 3)
    game.configure_random_districts()
    list_district_life = game.district_lifes()
    assert list_district_life == [280, 200, 200, 200, 200, 200]