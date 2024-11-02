import tkinter as tk
from tkinter import messagebox
from juego import Juego

class Interfaz:
    def __init__(self):
        self.juego = Juego()
        self.root = tk.Tk()
        self.root.title("Juego de Memoria")

        self.frame_registro = tk.Frame(self.root)
        self.frame_registro.pack()

        tk.Label(self.frame_registro, text="Nombre:").grid(row=0, column=0)
        self.entry_nombre = tk.Entry(self.frame_registro)
        self.entry_nombre.grid(row=0, column=1)

        tk.Label(self.frame_registro, text="Contraseña:").grid(row=1, column=0)
        self.entry_contraseña = tk.Entry(self.frame_registro, show="*")
        self.entry_contraseña.grid(row=1, column=1)

        self.boton_registrar = tk.Button(self.frame_registro, text="Registrar Jugador", command=self.registrar_jugador)
        self.boton_registrar.grid(row=2, columnspan=2)

        self.boton_iniciar_juego = tk.Button(self.frame_registro, text="Iniciar Juego", command=self.iniciar_juego)
        self.boton_iniciar_juego.grid(row=3, columnspan=2)

        self.frame_juego = tk.Frame(self.root)

    def iniciar(self):
        self.root.mainloop()

    def registrar_jugador(self):
        nombre = self.entry_nombre.get()
        contraseña = self.entry_contraseña.get()
        if nombre and contraseña:
            self.juego.registrar_jugadores(nombre, contraseña)
            messagebox.showinfo("Registro", f"Jugador {nombre} registrado con éxito!")
            self.entry_nombre.delete(0, tk.END)
            self.entry_contraseña.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def iniciar_juego(self):
        if len(self.juego.jugadores) < 2:
            messagebox.showwarning("Advertencia", "Se necesitan al menos 2 jugadores para iniciar el juego.")
            return

        self.frame_registro.pack_forget()
        self.mostrar_dificultad()

    def mostrar_dificultad(self):
        self.frame_dificultad = tk.Frame(self.root)
        self.frame_dificultad.pack()

        tk.Label(self.frame_dificultad, text="Seleccione la dificultad:").pack()

        dificultades = ['facil', 'medio', 'dificil']
        for dificultad in dificultades:
            boton = tk.Button(self.frame_dificultad, text=dificultad.capitalize(), command=lambda d=dificultad: self.seleccionar_dificultad(d))
            boton.pack()

    def seleccionar_dificultad(self, dificultad):
        self.juego.establecer_dificultad(dificultad)
        self.frame_dificultad.pack_forget()
        self.mostrar_tematica()

    def mostrar_tematica(self):
        self.frame_tematica = tk.Frame(self.root)
        self.frame_tematica.pack()

        tk.Label(self.frame_tematica, text="Seleccione la temática:").pack()

        self.tematicas = ['animales', 'frutas', 'emojis', 'objetos']
        for tematica in self.tematicas:
            boton = tk.Button(self.frame_tematica, text=tematica.capitalize(), command=lambda t=tematica: self.seleccionar_tematica(t))
            boton.pack()

    def seleccionar_tematica(self, tematica):
        self.juego.seleccionar_tematica(tematica)
        self.frame_tematica.pack_forget()
        self.iniciar_tablero()

    def iniciar_tablero(self):
        self.frame_juego.pack()
        self.tablero_label = tk.Label(self.frame_juego, text="Tablero de Juego")
        self.tablero_label.pack()

        self.tablero_frame = tk.Frame(self.frame_juego)
        self.tablero_frame.pack()

        self.mostrar_tablero()

        self.coord1 = None
        self.coord2 = None

        self.turno_label = tk.Label(self.frame_juego, text=f"Turno de: {self.juego.jugadores[self.juego.turno % len(self.juego.jugadores)].nombre}")
        self.turno_label.pack()

        # Contadores de puntos y aciertos
        self.puntos_label = tk.Label(self.frame_juego, text=f"Puntos: {self.juego.jugadores[self.juego.turno % len(self.juego.jugadores)].puntos}")
        self.puntos_label.pack()

        self.aciertos_label = tk.Label(self.frame_juego, text=f"Aciertos: {self.juego.jugadores[self.juego.turno % len(self.juego.jugadores)].aciertos}")
        self.aciertos_label.pack()

    def mostrar_tablero(self):
        for widget in self.tablero_frame.winfo_children():
            widget.destroy()

        for i, fila in enumerate(self.juego.tablero.tablero):
            for j, ficha in enumerate(fila):
                boton = tk.Button(self.tablero_frame, text="❓", width=4, height=2,
                                  command=lambda x=i, y=j: self.seleccionar_ficha(x, y))
                boton.grid(row=i, column=j)

    def seleccionar_ficha(self, x, y):
        if self.coord1 is None:
            self.coord1 = (x, y)
            self.mostrar_ficha(x, y)
        elif self.coord2 is None:
            self.coord2 = (x, y)
            self.mostrar_ficha(x, y)
            self.verificar_fichas()

    def mostrar_ficha(self, x, y):
        ficha = self.juego.tablero.tablero[x][y]
        for boton in self.tablero_frame.winfo_children():
            if boton.grid_info()['row'] == x and boton.grid_info()['column'] == y:
                boton.config(text=ficha)

    def verificar_fichas(self):
        if self.juego.jugar_turno(self.coord1, self.coord2):
            messagebox.showinfo("Éxito", "¡Par encontrado!")
        else:
            messagebox.showinfo("Error", "No coinciden. Intenta de nuevo.")

        
        jugador_actual = self.juego.jugadores[self.juego.turno % len(self.juego.jugadores)]
        self.puntos_label.config(text=f"Puntos: {jugador_actual.puntos}")
        self.aciertos_label.config(text=f"Aciertos: {jugador_actual.aciertos}")

        self.coord1 = None
        self.coord2 = None
        self.juego.siguiente_turno()

        if self.juego.juego_terminado():
            self.mostrar_resultados()
        else:
            self.turno_label.config(text=f"Turno de: {self.juego.jugadores[self.juego.turno % len(self.juego.jugadores)].nombre}")
            self.mostrar_tablero()

    def mostrar_resultados(self):
        resultados = self.juego.obtener_resultados()
        resultado_text = "Resultados finales:\n"
        for jugador in resultados:
            resultado_text += f"{jugador.nombre}: {jugador.puntos} puntos, Aciertos: {jugador.aciertos}\n"

        messagebox.showinfo("Resultados", resultado_text)
        self.root.quit()





