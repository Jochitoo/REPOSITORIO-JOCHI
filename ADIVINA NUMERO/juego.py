import random
secreto = random.randint(1, 100)
while True: 
    adivina = int(input("Adivina el número entre 1 y 100: "))
    if adivina < secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    elif adivina > secreto:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print("¡Felicidades! Has adivinado el número.")
        break



