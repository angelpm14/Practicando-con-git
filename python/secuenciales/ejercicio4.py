#4.	En países de habla inglesa, es común dar la estatura de una persona como la suma de una cantidad de pies, más una cantidad de pulgadas, por ejemplo 3’ 2”. Desarrolle el programa que determine la estatura en metros dada su estatura en el formato inglés.

import os
os.system("cls")

pies = float(input("Ingrese valor de pies: "))
pulgadas = float(input("Ingrese valor de pulgadas: "))

estat = (((pies * 12)+ pulgadas)* 2.54)

print("La estatura en metros es: ", format(estat, ".2f"), "m")