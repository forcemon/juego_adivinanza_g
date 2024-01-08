import random

def mostrar_menu_dificultad():
    print("Elige un nivel de dificultad:")
    print("1. Fácil (1-100, 20 intentos)")
    print("2. Medio (1-100, 10 intentos)")
    print("3. Difícil (1-100, 5 intentos)")
    eleccion = input("Selecciona 1, 2 o 3: ")
    return eleccion

def obtener_intentos_maximos(eleccion):
    if eleccion == '1':
        return 20
    elif eleccion == '2':
        return 10
    elif eleccion == '3':
        return 5
    else:
        return None

def solicitar_numero(mensaje, rango_min, rango_max):
    while True:
        entrada = input(mensaje)
        if entrada.isdigit():
            numero = int(entrada)
            if rango_min <= numero <= rango_max:
                return numero
            else:
                print(f"Por favor, ingresa un número entre {rango_min} y {rango_max}.")
        else:
            print("Entrada inválida. Por favor, ingresa un número.")

def jugar_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    eleccion = mostrar_menu_dificultad()
    intentos_maximos = obtener_intentos_maximos(eleccion)
    
    while intentos_maximos is None:
        print("Por favor, selecciona una dificultad válida.")
        eleccion = mostrar_menu_dificultad()
        intentos_maximos = obtener_intentos_maximos(eleccion)

    print("Bienvenido al Juego de Adivinanzas")
    print(f"Estoy pensando en un número entre 1 y 100. Tienes {intentos_maximos} intentos para adivinar.")

    while intentos < intentos_maximos:
        adivinanza = solicitar_numero("Adivina el número: ", 1, 100)
        intentos += 1

        if adivinanza < numero_secreto:
            print("Demasiado bajo.")
        elif adivinanza > numero_secreto:
            print("Demasiado alto.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            return

        print(f"Intentos restantes: {intentos_maximos - intentos}")

    print(f"Lo siento, te has quedado sin intentos. El número era {numero_secreto}.")

if __name__ == "__main__":
    jugar_adivinanza()