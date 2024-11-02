

class Player:
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña
        self.puntos = 0
        self.aciertos = 0

    def incrementar_puntos(self, puntos):
        self.puntos += puntos

    def incrementar_aciertos(self):
        self.aciertos += 1
