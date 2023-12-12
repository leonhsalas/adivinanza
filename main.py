import random

azar = random.randint(1,100)
mon = 0
while mon <= 2:
    numero = int(input("Elige un numero del 1 al 100 "))
    if numero < 1 or numero > 100:
        print("Pon un numero del 1 al 100 por favor")
    else:
        if numero == azar:
            print("Ganaste")
            break
        elif numero > azar:
            print("El valor de ingreso es menor que el numero a adivinar")
            mon = mon + 1
        elif numero < azar:
            print("El valor de ingreso es mayor que el numero a adivinar")
            mon = mon + 1

if mon == 3:
    print(f"Perdiste, el numero era {azar}")