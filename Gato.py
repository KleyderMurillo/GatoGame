import tkinter as tk
from tkinter import messagebox

# Clase Celda: Representa cada celda de la cuadrícula
class Celda:
    def __init__(self, master, fila, columna, juego):
        self.master = master
        self.fila = fila  # Fila en la que está la celda
        self.columna = columna  # Columna en la que está la celda
        self.juego = juego  # Referencia al objeto JuegoGato
        self.valor = ""  # Valor de la celda, puede ser "X", "O", o vacío
        # Crear un botón para la celda
        self.boton = tk.Button(master, text="", width=10, height=3, command=self.marcar)
        # Ubicar el botón en la cuadrícula de la ventana
        self.boton.grid(row=fila, column=columna)

    # Método para marcar la celda cuando el jugador hace clic
    def marcar(self):
        # Solo permite marcar si la celda está vacía y el juego sigue en curso
        if self.valor == "" and self.juego.jugando:
            # Asignar el valor del jugador actual a la celda
            self.valor = self.juego.jugador_actual
            # Actualizar el texto del botón con el valor (X o O)
            self.boton.config(text=self.valor)
            # Verificar si alguien ha ganado después de esta jugada
            self.juego.verificar_ganador()
            # Cambiar el turno al siguiente jugador
            self.juego.cambiar_turno()

# Clase JuegoGato: Controla la lógica del juego
class JuegoGato:
    def __init__(self, master):
        self.master = master  # Ventana principal del juego
        self.celdas = []  # Lista que contendrá las celdas del juego
        self.jugador_actual = "X"  # El jugador que inicia es "X"
        self.jugando = True  # Indicador de si el juego está en curso
        # Crear la cuadrícula de celdas
        self.crear_cuadricula()

    # Método para crear la cuadrícula 3x3 de celdas
    def crear_cuadricula(self):
        for i in range(3):
            fila = []  # Lista para almacenar las celdas de una fila
            for j in range(3):
                # Crear una celda y agregarla a la fila
                celda = Celda(self.master, i, j, self)
                fila.append(celda)
            # Agregar la fila a la lista de celdas del juego
            self.celdas.append(fila)

    # Método para cambiar el turno al siguiente jugador
    def cambiar_turno(self):
        # Cambia el jugador actual: si es "X", pasa a "O", y viceversa
        self.jugador_actual = "O" if self.jugador_actual == "X" else "X"

    # Método para verificar si alguien ha ganado
    def verificar_ganador(self):
        # Verificar las filas y columnas
        for i in range(3):
            # Verificar si todas las celdas de la fila i son iguales y no están vacías
            if self.celdas[i][0].valor == self.celdas[i][1].valor == self.celdas[i][2].valor != "":
                self.ganar()
            # Verificar si todas las celdas de la columna i son iguales y no están vacías
            if self.celdas[0][i].valor == self.celdas[1][i].valor == self.celdas[2][i].valor != "":
                self.ganar()
        # Verificar las diagonales
        if self.celdas[0][0].valor == self.celdas[1][1].valor == self.celdas[2][2].valor != "":
            self.ganar()
        if self.celdas[0][2].valor == self.celdas[1][1].valor == self.celdas[2][0].valor != "":
            self.ganar()
        # Verificar si todas las celdas están llenas y no hay ganador (empate)
        if all(celda.valor != "" for fila in self.celdas for celda in fila):
            self.empatar()

    # Método que se llama cuando un jugador gana
    def ganar(self):
        self.jugando = False  # Detiene el juego
        # Muestra un mensaje indicando que el jugador actual ha ganado
        messagebox.showinfo("Juego Terminado", f"¡{self.jugador_actual} ha ganado!")
        # Reinicia el juego
        self.reiniciar_juego()

    # Método que se llama cuando el juego termina en empate
    def empatar(self):
        self.jugando = False  # Detiene el juego
        # Muestra un mensaje indicando que el juego terminó en empate
        messagebox.showinfo("Juego Terminado", "¡Es un empate!")
        # Reinicia el juego
        self.reiniciar_juego()

    # Método para reiniciar el juego
    def reiniciar_juego(self):
        # Reinicia todas las celdas
        for fila in self.celdas:
            for celda in fila:
                celda.valor = ""  # Limpia el valor de la celda
                celda.boton.config(text="")  # Borra el texto del botón
        # El juego se reinicia con el jugador "X"
        self.jugador_actual = "X"
        self.jugando = True

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Juego del Gato")

# Crear el juego
juego = JuegoGato(ventana)

# Ejecutar la ventana
ventana.mainloop()