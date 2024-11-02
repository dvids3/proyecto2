
from players import Player
from fichas import Ficha
from tablero import Tablero

class Juego:
    def __init__(self):
        self.jugadores = []
        self.turno = 0
        self.tablero = None
        self.dificultad = None

    def registrar_jugadores(self, nombre, contraseña):
        self.jugadores.append(Player(nombre, contraseña))

    def seleccionar_tematica(self, tematica):
        fichas = Ficha(tematica)
        self.tablero = Tablero(fichas.fichas, self.dificultad)

    def establecer_dificultad(self, dificultad):
        self.dificultad = dificultad

    def jugar_turno(self, coord1, coord2):
        jugador = self.jugadores[self.turno % len(self.jugadores)]
        if self.tablero.tablero[coord1[0]][coord1[1]] == self.tablero.tablero[coord2[0]][coord2[1]]:
            jugador.incrementar_puntos(10)
            jugador.incrementar_aciertos()
            self.tablero.eliminar_fichas(coord1, coord2)
            return True
        else:
            jugador.incrementar_puntos(-5)
            return False

    def juego_terminado(self):
        return self.tablero.juego_terminado()

    def obtener_resultados(self):
        return sorted(self.jugadores, key=lambda x: x.puntos, reverse=True)

    def siguiente_turno(self):
        self.turno += 1


