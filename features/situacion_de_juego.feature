# language: es
  Característica: Sitauacion de juego

    Escenario: Dos tributos luchan y uno de ellos encuentra un item
      Dado que el juego ya está inicializado
      Y la vida de t1 es de 30
      Y la poción cura 10 de vida
      Y la fuerza de t2 es de 5
      Y t1 mueve antes que t2
      Y el estado del tablero es el siguiente
        |0 |1 |2 |3 |
        |  |  |  |  |
        |  |  |  |t2|
        |  |t1|p |  |
        |  |  |  |  |
      Cuando se ejecute una iteracion
      Entonces el estado del tablero será el siguiente
        |0 |1 |2 |3 |
        |  |  |  |  |
        |  |  |  |t2|
        |  |  |t1|  |
        |  |  |  |  |
      Y la vida de t1 se reducirá a 35
      Y la vida de t2 se mantiene igual

    Escenario: Dos tributos luchan y llega otro tributo
      Dado que empezo la simulacion
      Y dos tributos enemigos son adyacentes
      Y estan luchando
      Cuando otro tributo visualize a los tributos luchando mediante su rango de vision
      Y sea adyacente a ambos
      Entonces le pegara al tributo que tenga mas vida

    Escenario: Dos tributos luchan y llega un aliado
      Dado que empezo la simulacion
      Y dos tributos de distinto distritos son adyacentes
      Y estan luchando
      Cuando  llegue un tributo aliado de algunos de los dos tributos que estan luchando
      Y ambos tributos entran en el rango de vision del aliado
      Entonces el aliado atacara al tributo enemigo

    Escenario: Enfrentamiento entre tributos
      Dado que t1 es del distrito 0
      Y t2 es del distrito 1
      Y t1 tiene la misma fuerza t2
      Y t1 tiene la misma vida t2
      Y el estado del tablero es el siguiente
        |0 |1 |2 |3 |
        |t1|t2|  |  |
        |  |  |  |  |
        |  |  |  |  |
        |  |  |  |  |
      Cuando se ejecute una iteracion
      Entonces la vida de t1 es distinta de 40
      Y la vida de t2 es distinta de 50

    Escenario: Un tributo se alia con un tributo neutro
      Dado que un tributo pertenece a un distrito y otro es neutro
      Cuando se encuentran en el mapa
      Y el tributo perteneciente al distrito es capaz de aliarse
      Entonces el tributo neutro se convierte en un miembro del tributo que se encontro
      Y adquiere las caracteristicas del distrito al cual corresponde

    Escenario: Un tributo no logra aliarse con un tributo neutro
      Dado un tributo que pertenece a un distrito y otro neutro
      Cuando ambos tributos se encuentran en el mapa
      Y el tributo del distrito NO es capaz de aliarse
      Entonces el tributo del distrito lucha con el tributo neutro

    Escenario: Dos tributos del mismo distrito se encuentran en el mapa
      Dado dos tributos
      Cuando se encuentran en el mapa
      Y ambos pertenecen al mismo distrito
      Entonces se ignoran

    Escenario: Muerte de un tributo en batalla
      Dado t1 en la posición (0,2)
      Y t2 en la posición (1,2)
      Y ambos son de distinto distrito
      Y t1 mueve antes que t2
      Y t2 tiene 5 de vida
      Y t1 tiene 7 de fuerza
      Cuando t1 le pega a t2
      Entonces la vida de t2 se reduce en 7 puntos
      Y la vida de t2 es de 0 o menos
      Y t2 muere

    Escenario: Dos tributos neutros se encuentran en el mapa
      Dado que dos tributos son neutros
      Cuando se encuentran en el mapa
      Entonces se ignoran

    Escenario: Tributo encuentra un item de curacion y lo utiliza
      Dado que un tributo encuentra un item de curacion en el mapa
      Y no tenga la vida al maximo
      Cuando el tributo se encuentra sobre el item
      Entonces su vida incrementa
      Y el item desaparece del mapa

    Escenario: Tributo encuentra un item de curación y no lo utiliza
      Dado un t1 con el 100 porciento de vida
      Y el siguiente estado del tablero
        |0 |1 |2 |3 |
        |  |  |  |  |
        |  |  |  |  |
        |  |t1|p |  |
        |  |  |  |  |
      Cuando t1 se mueve hacia la celda (2,2)
      Entonces el estado del tablero es el siguiente
        |0 |1 |2 |3 |
        |  |  |  |  |
        |  |  |  |  |
        |  |  |t1|  |
        |  |  |  |  |
      Y su vida se mantiene igual
      Y la poción de la celda

    Escenario: Tributo encuentra una espada y la recoge
      Dado que un tributo encuentra una espada en el mapa
      Cuando el tributo no tenga una espada
      Y se escuentre sobre la espada
      Entonces su daño se incrementa
      Y la espada desaparece del mapa

    Escenario: Tributo encuentra una espada y no la recoge
      Dado que un tributo encuentra una espada en el mapa
      Cuando el tributo tenga una espada
      Y se encuentre sobre la espada
      Entonces no la recoge

    Escenario: Tributo con más fuerza inflige más daño a su enemigo
	    Dado que dos tributos son de distinto distrito
	    Cuando se cruzan en el mapa
	    Entonces el tributo con más fuerza inflige más daño

    Escenario: Tributo con menos fuerza inflige menos daño a su enemigo
	    Dado que dos tributos son de distinto distrito
	    Cuando se cruzan en el mapa
	    Entonces el tributo con menos fuerza inflige menos daño
