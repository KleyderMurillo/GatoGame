import tkinter as tk
from tkinter import messagebox

# clase Celda: representa cada celda de la cuadricula
class Celda:
    def __init__(self, master, fila, columna, juego):
        self.master = master
        self.fila = fila  # fila en la que esta la celda
        self.columna = columna  # columna en la que esta la celda
        self.juego = juego  # referencia al objeto JuegoGato
        self.valor = ""  # valor de la celda, puede ser "X", "O", o vacio
        # crear un boton para la celda
        self.boton = tk.Button(master, text="", width=10, height=3, command=self.marcar)
        # ubicar el boton en la cuadricula de la ventana
        self.boton.grid(row=fila, column=columna)

    # metodo para marcar la celda cuando el jugador hace clic
    def marcar(self):
        # solo permite marcar si la celda esta vacia y el juego sigue en curso
        if self.valor == "" and self.juego.jugando:
            # asignar el valor del jugador actual a la celda
            self.valor = self.juego.jugador_actual
            # actualizar el texto del boton con el valor (X o O)
            self.boton.config(text=self.valor)
            # verificar si alguien ha ganado despues de esta jugada
            self.juego.verificar_ganador()
            # cambiar el turno al siguiente jugador
            self.juego.cambiar_turno()

# clase JuegoGato: Controla la logica del juego
class JuegoGato:
    def __init__(self, master):
        self.master = master  # ventana principal del juego
        self.celdas = []  # lista que contendrá las celdas del juego
        self.jugador_actual = "X"  # el jugador que inicia es "X"
        self.jugando = True  # indicador de si el juego está en curso
        # crear la cuadricula de celdas
        self.crear_cuadricula()

    # metodo para crear la cuadricula 3x3 de celdas
    def crear_cuadricula(self):
        for i in range(3):
            fila = []  # lista para almacenar las celdas de una fila
            for j in range(3):
                # se crear una celda y se agrega a la fila
                celda = Celda(self.master, i, j, self)
                fila.append(celda)
            # se agrega la fila a la lista de celdas del juego
            self.celdas.append(fila)

    # metodo para cambiar el turno al siguiente jugador
    def cambiar_turno(self):
        # cambia el jugador actual: si es "X", pasa a "O", y viceversa
        self.jugador_actual = "O" if self.jugador_actual == "X" else "X"

    # metodo para verificar si alguien ha ganado
    def verificar_ganador(self):
        # verifica las filas y columnas
        for i in range(3):
            # verifica si todas las celdas de la fila i son iguales y no estan vacias
            if self.celdas[i][0].valor == self.celdas[i][1].valor == self.celdas[i][2].valor != "":
                self.ganar()
            # verifica si todas las celdas de la columna i son iguales y no estan vacias
            if self.celdas[0][i].valor == self.celdas[1][i].valor == self.celdas[2][i].valor != "":
                self.ganar()
        # verifica las diagonales
        if self.celdas[0][0].valor == self.celdas[1][1].valor == self.celdas[2][2].valor != "":
            self.ganar()
        if self.celdas[0][2].valor == self.celdas[1][1].valor == self.celdas[2][0].valor != "":
            self.ganar()
        # verifica si todas las celdas estan llenas y no hay ganador (empate)
        if all(celda.valor != "" for fila in self.celdas for celda in fila):
            self.empatar()

    # metodo que se llama cuando un jugador gana
    def ganar(self):
        self.jugando = False  # detiene el juego
        # muestra un mensaje indicando que el jugador actual ha ganado
        messagebox.showinfo("El juego a terminado", f"¡{self.jugador_actual} es el vencedor")
        # reinicia el juego
        self.reiniciar_juego()

    # metodo que se llama cuando el juego termina en empate
    def empatar(self):
        self.jugando = False  # se detiene el juego
        # muestra un mensaje indicando que el juego termino en empate
        messagebox.showinfo("El juego a terminado", "Es un empate")
        # reinicia el juego
        self.reiniciar_juego()

    # metodo para reiniciar el juego
    def reiniciar_juego(self):
        # reinicia todas las celdas
        for fila in self.celdas:
            for celda in fila:
                celda.valor = ""  # limpia el valor de la celda
                celda.boton.config(text="")  # borra el texto del boton
        # el juego se reinicia con el jugador "X"
        self.jugador_actual = "X"
        self.jugando = True

# crear la ventana principal
ventana = tk.Tk()
ventana.title("Juego del Gato")

# crear el juego
juego = JuegoGato(ventana)

# ejecutar la ventana
ventana.mainloop()