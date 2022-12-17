#11.	Desarrolle el programa que determine el signo de un número entre positivo, negativo y cero.

import os
os.system("cls")
'''11.	Desarrolle el programa que determine el signo de un número entre positivo, negativo y cero.'''
print("")
n= int(input("ingresa un numero: "))

if n > 0:
    print("el numero es positivo")
elif n < 0:
    print("el numero es negativo")
else: 
    print("el numero es neutro")
