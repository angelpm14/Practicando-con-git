#12.	Dado un número que expresa el tiempo en segundos, desarrolle el programa que exprese dicho tiempo como la cantidad de días, horas, minutos y segundos contenidos en ese número.

import os
os.system("cls")

num_seg = int(input("Ingrese un numero expresado en segundos: "))

dias = ((num_seg // 60)// 60)// 24
hora = ((num_seg // 60)// 60)% 24
minutos =(num_seg // 60)% 60
segundos = num_seg % 60

print("Dias: ",dias)
print("Horas: ",hora)
print("Minutos: ",minutos)
print("Segundos: ",segundos)
