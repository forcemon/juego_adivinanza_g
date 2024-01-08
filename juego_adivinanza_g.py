import tkinter as tk
import random

# Función para iniciar el juego
def iniciar_juego(dificultad):
    global numero_secreto, intentos, intentos_maximos
    numero_secreto = random.randint(1, 100)
    intentos = 0
    intentos_maximos = dificultad
    etiqueta_intentos['text'] = f'Intentos: {intentos}/{intentos_maximos}'
    boton_adivinar.config(state=tk.NORMAL)
    entrada_numero.config(state=tk.NORMAL)
    mensaje['text'] = "He pensado en un número del 1 al 100. ¡Intenta adivinarlo!"

# Función para verificar la adivinanza del usuario
def verificar_adivinanza():
    global intentos
    intentos += 1
    adivinanza = int(entrada_numero.get())
    etiqueta_intentos['text'] = f'Intentos: {intentos}/{intentos_maximos}'

    if adivinanza < numero_secreto:
        mensaje['text'] = "Demasiado bajo. Intenta de nuevo."
    elif adivinanza > numero_secreto:
        mensaje['text'] = "Demasiado alto. Intenta de nuevo."
    else:
        mensaje['text'] = f"¡Felicidades! Adivinaste el número en {intentos} intentos."
        boton_adivinar.config(state=tk.DISABLED)
        entrada_numero.config(state=tk.DISABLED)

    if intentos >= intentos_maximos and adivinanza != numero_secreto:
        mensaje['text'] = f"Fin del juego. El número era: {numero_secreto}"
        boton_adivinar.config(state=tk.DISABLED)
        entrada_numero.config(state=tk.DISABLED)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Juego de Adivinanzas")

# Variables globales
numero_secreto = 0
intentos = 0
intentos_maximos = 0

# Elementos de la interfaz gráfica
mensaje = tk.Label(ventana, text="Elige una dificultad para empezar el juego.")
mensaje.pack()

etiqueta_intentos = tk.Label(ventana, text="Intentos: 0/0")
etiqueta_intentos.pack()

entrada_numero = tk.Entry(ventana, state=tk.DISABLED)
entrada_numero.pack()

boton_adivinar = tk.Button(ventana, text="Adivinar", command=verificar_adivinanza, state=tk.DISABLED)
boton_adivinar.pack()

boton_facil = tk.Button(ventana, text="Fácil (20 intentos)", command=lambda: iniciar_juego(20))
boton_facil.pack()

boton_medio = tk.Button(ventana, text="Medio (10 intentos)", command=lambda: iniciar_juego(10))
boton_medio.pack()

boton_dificil = tk.Button(ventana, text="Difícil (5 intentos)", command=lambda: iniciar_juego(5))
boton_dificil.pack()

# Iniciar el bucle de eventos
ventana.mainloop()