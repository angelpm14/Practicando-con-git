#3.	Una persona ha recorrido tres tramos de una carretera. La longitud del primer tramo está dada en kilómetros, el segundo tramo en pies y el tercer tramo en millas. Desarrolle el programa que determine la longitud total recorrida en metros y en yardas. Considere los siguientes factores de conversión: 1 metro = 3.2808 pies, 1 milla = 1609 metros.

import os 
os.system("cls")

kilometros = float(input("Ingrese el primer tramo en kilometros: "))
pies = float(input("Ingrese el segundo tramo en pies: "))
millas = float(input("Ingrese el tercer tramo en millas: "))

tramo_1 = kilometros*1000
tramo_2 = pies / 3.2808
tramo_3 = millas * 1609

total_metros = tramo_1 + tramo_2 + tramo_3
total_yardas = (total_metros *3.2808) / 3
print("Total en metros: ",format(total_metros,".2f"),"m")
print("Total en yardas: ",format(total_yardas,".2f"),"yd")