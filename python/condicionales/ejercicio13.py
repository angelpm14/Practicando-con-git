#13    Desarrolle el programa que lea un número entero positivo de tres cifras y determine si las cifras son o no consecutivas (en orden ascendente o descendente). En caso contrario mostrar mensaje

import os
os.system("cls")

n = int(input("ingresar"))

n1 = int (input("ingrese el primer numero"))
n2 = int (input("ingrese el segundo numero"))
n3 = int (input("ingrese el tercer numero"))

if n1 < n2 < n3 :
    print("los numeros estan ordenados de forma creciente")
else:
    print("los numeros no estan ordenados de forma creciente")
