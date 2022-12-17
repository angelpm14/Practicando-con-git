#9.	Desarrolle el programa que lea un número entero y determine la suma de sus cifras. Asumir que el número es positivo y de 4 cifras.

import os
os.system("cls")

numero = int(input("Ingrese un numero de 4 cifras: "))

c_1 = int(numero / 1000)
c_2 = int((numero % 100)/100)
c_3 = int(((numero % 1000)% 100)/ 10)
c_4 = numero % 10

print("La suma de los digitos es: ", c_1 + c_2 + c_3 + c_4)