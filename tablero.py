class Tablero:
    def __init__(self, fichas, dificultad):
        if dificultad == 'facil':
            self.tablero = [fichas[i:i + 3] for i in range(0, len(fichas), 3)]
        elif dificultad == 'medio':
            self.tablero = [fichas[i:i + 5] for i in range(0, len(fichas), 5)]
        else:  
            self.tablero = [fichas[i:i + 7] for i in range(0, len(fichas), 7)]

    def mostrar_tablero(self, descubiertas=[]):
        for i, fila in enumerate(self.tablero):
            for j, ficha in enumerate(fila):
                if (i, j) in descubiertas:
                    print(ficha, end=" ")
                else:
                    print("❓", end=" ")
            print()

    def eliminar_fichas(self, coord1, coord2):
        self.tablero[coord1[0]][coord1[1]] = " "
        self.tablero[coord2[0]][coord2[1]] = " "

    def juego_terminado(self):
        return all(ficha == " " for fila in self.tablero for ficha in fila)


