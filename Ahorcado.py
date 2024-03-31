import random

# Lista de palabras para que el programa escoja al azar
biblioteca_palabras = ["python", "programacion", "hola", "inteligencia", "analisis", "aprendizaje", "platzi", "celular", "internet", "casa", "nombre", "mesa"]

# Seleccionar una palabra al azar de la biblioteca
palabra_secreta = random.choice(biblioteca_palabras)

# Lista para almacenar las letras adivinadas por el jugador
letras_adivinadas = []

# Número de intentos permitidos
intentos = 6

print("¡Bienvenido al juego de ahorcado!")

# Mostrar cuántas letras tiene la palabra seleccionada
print("La palabra que vas a adivinar tiene un total de => ", len(palabra_secreta), "letras.")

while True:
    # Mostrar el tablero con las letras adivinadas y los espacios vacíos
    tablero = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    print(tablero)

    # Pedir al jugador que ingrese una letra
    letra = input("Ingresa una letra: ").lower()

    # Verificar si la letra ingresada es válida
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, ingresa una letra válida.")
        continue

    # Verificar si la letra ya ha sido adivinada anteriormente
    if letra in letras_adivinadas:
        print("Ya has intentado esta letra. Intenta con otra.")
        continue

    # Agregar la letra adivinada a la lista
    letras_adivinadas.append(letra)

    # Verificar si el jugador ha adivinado todas las letras
    if all(letra in letras_adivinadas for letra in palabra_secreta):
        print("¡Felicidades! Has adivinado la palabra correctamente.")
        break

    # Verificar si la letra no está en la palabra secreta
    if letra not in palabra_secreta:
        intentos -= 1
        print(f"¡Incorrecto! Te quedan {intentos} intentos.")

        # Si el jugador se queda sin intentos, termina el juego
        if intentos == 0:
            print("¡Oh no! Te has quedado sin intentos. La palabra era:", palabra_secreta)
            break
