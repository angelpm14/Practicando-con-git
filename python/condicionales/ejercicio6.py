#6.	Desarrolle el programa que determine la edad menor y mayor de tres edades ingresadas.

import os
os.system("cls")

edad=input("Escribir el numero de edades:")
edad_int=int(edad)
if edad_int>=18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de esda")