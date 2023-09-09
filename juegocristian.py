import random

intentos = 0
numero_secreto = random.randint(1, 100)

while True:
    adivina_el_numero = input("Ingresa un número del 1 al 100: ")

    if adivina_el_numero.lower() == "salir":
        # El usuario ha decidido salir del juego
        print("Has salido del juego.")
        break

    try:
        numero_adivinado = int(adivina_el_numero)

        if 1 <= numero_adivinado <= 100:
            intentos += 1

            if numero_adivinado == numero_secreto:
                print(f"¡Felicidades! Adivinaste el número secreto {numero_secreto} en {intentos} intentos.")
                break
            elif numero_adivinado > numero_secreto:
                print("El número secreto es más bajo. ¡Intenta de nuevo!")
            else:
                print("El número secreto es más alto. ¡Intenta de nuevo!")
        else:
            print("Por favor, ingresa un número válido del 1 al 100.")
    except ValueError:
        print("Por favor, ingresa un número válido del 1 al 100 o escribe 'salir' para salir del juego.")
