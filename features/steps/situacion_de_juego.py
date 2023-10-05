from behave import given, when, then, step
from game.logic.cell import State
from game.logic.district import District
from game.logic.game_logic import GameLogic
from game.logic.tribute import Tribute
from game.logic.cell import State
from game.logic.item import Potion, Weapon
from game.logic.board import Board


@given('que el juego ya está inicializado')
def step_impl(context):
    pass


@given(u'la vida de t1 es de 30')
def step_impl(context):
    pass


@given(u'la poción cura 10 de vida')
def step_impl(context):
    pass


@given(u'la fuerza de t2 es de 5')
def step_impl(context):
    pass


@given(u't1 mueve antes que t2')
def step_impl(context):
    pass


@given(u'el estado del tablero es el siguiente')
def step_impl(context):
    pass


@when(u'se ejecute un movimiento')
def step_impl(context):
    pass


@then(u'el estado del tablero será el siguiente')
def step_impl(context):
    pass


@then(u'la vida de t1 se reducirá a 35')
def step_impl(context):
    pass


@then(u'la vida de t2 se mantiene igual')
def step_impl(context):
    pass


@given(u'que empezo la simulacion')
def step_impl(context):
    pass


@given(u'dos tributos enemigos son adyacentes')
def step_impl(context):
    pass


@given(u'estan luchando')
def step_impl(context):
    pass


@when(u'otro tributo visualize a los tributos luchando mediante su rango de vision')
def step_impl(context):
    pass


@when(u'sea adyacente a ambos')
def step_impl(context):
    pass


@then(u'le pegara al tributo que tenga mas vida')
def step_impl(context):
    pass


@given(u'dos tributos de distinto distritos son adyacentes')
def step_impl(context):
    pass


@when(u'llegue un tributo aliado de algunos de los dos tributos que estan luchando')
def step_impl(context):
    pass


@when(u'ambos tributos entran en el rango de vision del aliado')
def step_impl(context):
    pass


@then(u'el aliado atacara al tributo enemigo')
def step_impl(context):
    pass


#####################################

@given(u'que t0 pertenece al distrito 0')
def step_impl(context):
    context.game = GameLogic()
    context.game.new_game(2, 2)
    context.t0 = Tribute()
    context.d0 = District()
    context.t0.district = 0
    context.d0.number_district = 0
    context.d0.add_tribute(context.t0)
    context.game.districts.append(context.d0)


@given(u't0 tiene una vida de 50')
def step_impl(context):
    context.t0.life = 50


@given(u't0 tiene una fuerza de 10')
def step_impl(context):
    context.t0.force = 10


@given(u't1 pertenece al distrito 1')
def step_impl(context):
    context.t1 = Tribute()
    context.d1 = District()
    context.d0.number_district = 1
    context.t1 = Tribute()
    context.t1.district = 1
    context.d1.add_tribute(context.t1)
    context.game.districts.append(context.d1)


@given(u't1 tiene una vida de 50')
def step_impl(context):
    context.t1.life = 50


@given(u't1 tiene una fuerza de 10')
def step_impl(context):
    context.t1.force = 10


@given(u't0 esta en la posicion (0,0)')
def step_impl(context):
    context.game.board.put_tribute(0, 0, context.t0)


@given(u't1 esta en la posicion (0,1)')
def step_impl(context):
    context.game.board.put_tribute(0, 1, context.t1)


@when(u'se ejecute una iteracion del juego')
def step_impl(context):
    context.game.heuristic_tribute_first_attempt(context.t0)
    context.game.heuristic_tribute_first_attempt(context.t1)


@then(u'la vida de t0 es 40')
def step_impl(context):
    assert context.t0.life == 40


@then(u'la vida de t1 es 40')
def step_impl(context):
    assert context.t1.life == 40


# ------------------------------------------------------------------- Inicio del escenario

@step("que existe un t1 y un t")
@given('que existe un t1 y un t')
def step_impl(context):
    context.game = GameLogic()
    context.game.new_game(3, 3)
    context.district0 = District()
    context.district0.number_district = 0
    context.tribute1 = Tribute()
    context.tribute1.set_config_parameters(50, 5, 25, 0)
    context.district0.add_tribute(context.tribute1)
    context.neutral_tribute = Tribute()
    context.game.neutrals.append(context.neutral_tribute)
    context.district0.add_tribute(context.tribute1)
    context.old_number_of_tributes = context.district0.get_cant_tribute()
    context.game.board.put_tribute(1, 0, context.tribute1)
    context.game.board.put_tribute(1, 1, context.neutral_tribute)
    context.game.districts.append(context.district0)


@given('t1 pertenece al distrito 0')
def step_impl(context):
    assert context.tribute1.district == 0


@given('t1 tiene un valor de alianza 25')
def step_impl(context):
    assert context.tribute1.alliance == 25


@given('t es un tribruto neutro')
def step_impl(context):
    assert context.game.neutrals.__contains__(context.neutral_tribute)


@when('t acepte la alianza de t1')
def step_impl(context):
    context.game.heuristic_tribute_first_attempt(context.tribute1)


@then('el tributo t forma parte del distrito 0')
def step_impl(context):
    # context.game.alliance_neutral(context.neutral_tribute, context.district0)
    # assert context.tribute1.alliance_to(context.neutral_tribute) is True
    assert context.neutral_tribute.district == 0


@then('el distrito 0 tiene un tributo más en su cantidad total')
def step_impl(context):
    assert context.district0.get_cant_tribute() > context.old_number_of_tributes


@then('el tributo neutro pertenece al districto 0')
def step_impl(context):
    # assert context.district0.get_cant_tribute() > context.old_number_of_tributes
    # assert context.game.districts[0].tributes.__contains__(context.neutral_tribute)
    assert context.district0.tributes.__contains__(context.neutral_tribute)


@then(u'el tributo neutro no pertenece más al grupo de los neutros')
def step_impl(context):
    assert context.game.neutrals.__contains__(context.neutral_tribute) is False


# ------------------------------------------------------------------- Fin del escenario


@given('t1 tiene un valor de alianza 1')
def step_impl(context):
    pass


@when('t rechaze la alianza de t1')
def step_impl(context):
    pass


@then('el tributo t empieza a pelear con t1')
def step_impl(context):
    pass


@given(u'dos tributos')
def step_impl(context):
    pass


@when(u'se encuentran en el mapa')
def step_impl(context):
    pass


@when(u'ambos pertenecen al mismo distrito')
def step_impl(context):
    pass


@then(u'se ignoran')
def step_impl(context):
    pass


@given('t1 en la posición (0,2)')
def step_impl(context):
    context.game = GameLogic()
    context.game.new_game(4, 4)
    context.t1 = Tribute()
    context.t1.set_config_parameters(None, 7, None, 0)
    context.game.put_tribute_in_game(0, 2, context.t1)
    assert context.t1.pos == (0, 2)
    assert context.game.board.get_element(0, 2).get_state() == State.TRIBUTE


@given('t2 en la posición (1,2)')
def step_impl(context):
    context.t2 = Tribute()
    context.t2.set_config_parameters(5, None, None, 1)
    context.game.put_tribute_in_game(1, 2, context.t2)
    assert context.t2.pos == (1, 2)
    assert context.game.board.get_element(1, 2).get_state() == State.TRIBUTE


@given('ambos son de distinto distrito')
def step_impl(context):
    assert context.t1.district != context.t2.district


@given('t2 tiene 5 de vida')
def step_impl(context):
    assert context.t2.life == 5


@given('t1 tiene 7 de fuerza')
def step_impl(context):
    assert context.t1.force == 7


@when('t1 le pega a t2')
def step_impl(context):
    context.game.one_iteration()
    pass


@then('la vida de t2 se reduce en 7 puntos')
def step_impl(context):
    assert context.t2.life == -2


@then('la vida de t2 es de 0 o menos')
def step_impl(context):
    assert context.t2.life <= 0


@then('t2 muere')
def step_impl(context):
    assert context.t2.is_dead()


@given(u'que dos tributos son neutros')
def step_impl(context):
    pass


@given('un tributo t1 con 20 de vida en la posición (1,2)')
def step_impl(context):
    context.game = GameLogic()
    context.game.new_game(3, 3)
    context.t1 = Tribute()
    context.d0 = District()
    context.d0.number_district = 0
    context.game.districts.append(context.d0)
    context.t1.set_config_parameters(20, None, None, None)
    context.d0.add_tribute(context.t1)
    context.game.board.put_tribute(1, 2, context.t1)
    assert context.t1.life == 20
    assert context.t1.pos == (1, 2)
    assert context.game.board.get_element(1, 2).get_state() == State.TRIBUTE


@given('una poción p en la posición (2,2)')
def step_impl(context):
    context.p = Potion()
    context.game.board.put_item(2, 2, context.p)
    assert context.p.get_pos() == (2, 2)
    assert context.game.board.get_element(2, 2).get_state() == State.ITEM


@when('se ejecute una iteracion')
def step_impl(context):
    context.game.heuristic_tribute_first_attempt(context.t1)


@then('t1 se encuentra en (2,2)')
def step_impl(context):
    assert context.t1.pos == (2, 2)
    assert context.game.board.get_element(2, 2).get_tribute() is not None


@then('p desaparece del mapa')
def step_impl(context):
    assert context.game.board.get_element(2, 2).get_state() != State.ITEM


@then('la vida de t1 ahora es de 25')
def step_impl(context):
    assert context.t1.life == 25


@given(u'un t1 con el 100 porciento de vida')
def step_impl(context):
    pass


@given(u'el siguiente estado del tablero')
def step_impl(context):
    pass


@when(u't1 se mueve hacia la celda (2,2)')
def step_impl(context):
    pass


@then(u'el estado del tablero es el siguiente')
def step_impl(context):
    pass


@then(u'su vida se mantiene igual')
def step_impl(context):
    pass


@then(u'la poción de la celda')
def step_impl(context):
    pass




@given('que un t1 se encuentra en la posicion (2,2) del mapa')
def step_impl(context):
    context.game = GameLogic()
    context.game.new_game(4, 4)
    context.t0 = Tribute()
    context.d0 = District()
    context.t0.set_config_parameters(50, 8, 2, 0)
    context.d0.add_tribute(context.t0)
    context.game.districts.append(context.d0)
    context.game.board.put_tribute(2, 2, context.t0)
    assert not (context.game.board.get_element(2, 2).get_tribute() is None)


@given('que una espada se encuentra en la posicion (2,3) del mapa')
def step_impl(context):
    context.w0 = Weapon()
    context.game.board.put_item(2, 3, context.w0)
    assert not (context.game.board.get_element(2, 3).get_item() is None)


@given('t1 tiene una fuerza de 8')
def step_impl(context):
    assert context.t0.force == 8


@when('se ejecuta una iteracion')
def step_impl(context):
    context.game.heuristic_tribute_first_attempt(context.t0)



@then('su fuerza aumenta a 9')
def step_impl(context):
    assert context.t0.force == 9


@then('la espada desaparece del mapa')
def step_impl(context):
    assert not(context.game.board.get_element(2, 3).get_tribute() is None)


@then('la posicion de t1 es (2,3)')
def step_impl(context):
    assert context.t0.pos == (2, 3)


###############################################################################################################

@given(u'que un tributo encuentra una espada en el mapa')
def step_impl(context):
    pass


@when(u'el tributo tenga una espada')
def step_impl(context):
    pass


@when(u'se encuentre sobre la espada')
def step_impl(context):
    pass


@then(u'no la recoge')
def step_impl(context):
    pass

###############################################################################################################

# ---------------------------------------------------------------------------
# Escenario: Tributo con mayor fuerza inflige mayor daño a otro tributo con menor fuerza en combate
@given('que dos tributos son de distinto distrito en un tablero de 5 x 5')
def step_impl(context):
    context.t1 = Tribute()
    context.t2 = Tribute()
    context.game = GameLogic()
    context.game.new_game(5, 5)  # create board of 5 x 5
    context.t1.set_config_parameters(50, 9, 1, 1)  # life, force, alliance, district
    context.t2.set_config_parameters(50, 5, 1, 2)  # life, force, alliance, district
    assert context.t1.district != context.t2.district


@step('tributo t1 del distrito 1 tiene fuerza de 9 y vida de 50')
def step_impl(context):
    assert context.t1.district == 1
    assert context.t1.force == 9
    assert context.t1.life == 50


@step('tributo t2 del distrito 2 tiene fuerza de 5 y vida de 50')
def step_impl(context):
    assert context.t2.district == 2
    assert context.t2.force == 5
    assert context.t2.life == 50


@step('tributo t1 se encuentra en la posición (0, 3) del tablero')
def step_impl(context):
    context.game.board.put_tribute(0, 3, context.t1)
    assert context.t1.pos == (0, 3)
    assert context.game.board.get_element(0, 3).get_state() == State.TRIBUTE


@step('tributo t2 se encuentra en la posición (1, 2) del tablero')
def step_impl(context):
    context.game.board.put_tribute(1, 2, context.t2)
    assert context.t2.pos == (1, 2)
    assert context.game.board.get_element(1, 2).get_state() == State.TRIBUTE


@when('se ejecute un paso de simulación')
def step_impl(context):
    context.game.heuristic_tribute_first_attempt(context.t1)  # working t1
    context.game.heuristic_tribute_first_attempt(context.t2)  # working t2


@then('tributo t1 con mayor fuerza inflige mayor daño a tributo t2')
def step_impl(context):
    context.force_tribute_1 = context.t1.force
    context.force_tribute_2 = context.t2.force
    assert context.force_tribute_1 > context.force_tribute_2


@step('vida del tributo t2 se decrementa en 9')
def step_impl(context):
    assert context.t2.life == 41
    assert context.game.board.get_element(1,
                                          2).get_state() == State.TRIBUTE  # verify that t2 still in your position fighting


@step('vida del tributo t1 se decrementa en 5')
def step_impl(context):
    assert context.t1.life == 45
    assert context.game.board.get_element(0,
                                          3).get_state() == State.TRIBUTE  # verify that t1 still in your position figthing


# -----------------------------------------------------------------------------------

@given('que dos tributos son de distinto distrito')
def step_impl(context):
    pass


@when('se cruzan en el mapa')
def step_impl(context):
    pass


@then(u'el tributo con menos fuerza inflige menos daño')
def step_impl(context):
    pass
