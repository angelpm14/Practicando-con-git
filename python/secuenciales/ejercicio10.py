#10.    Dado un número natural de cuatro cifras, desarrolle el programa que permite obtener el número al revés. Ejemplo 1234   4321.

import os
os.system("cls")

numero = int(input("Ingrese un numero: "))

c1 = numero // 1000
c2 = (numero % 1000) // 100
c3 = (((numero % 1000)% 100)// 10)
c4 = numero % 10

print("El numero al reves es: ", (c4 * 1000) + (c3 * 100) + (c2 * 10) + c1)
