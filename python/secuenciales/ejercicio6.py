#6.	Desarrolle el programa que calcule el área total y el volumen de un cilindro. Considere las siguientes formulas: Área = 2πr(r+h) y Volumen = πr2h. Siendo r el radio y h la altura.

import os
os.system("cls")

rad = float(input("Ingrese el radio del cilindro: "))
altu = float(input("Ingrese la altura del cilindro: "))

areatt = 2 * 3.1416 * rad * (rad + altu)
volumen = 3.1416 * rad * 2 * altu

print("El area total del cilindro es: ", format(areatt,".2f"))
print("El volumen del cilindro es: ", format(volumen,".2f"))