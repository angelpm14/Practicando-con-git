#5.	Desarrolle el programa que dada la capacidad de un disco duro en gigabytes, lo convierta a megabytes, kilobytes y bytes. 1 KB = 1024 bytes, 1 MB = 1024 KB, 1 GB = 1024 MB.

import os 
os.system("cls")

gigabytes = int(input("Ingrese capacidad de disco en GB: "))

megaby = gigabytes * 1024
kiloby = megaby * 1024
cby = kiloby * 1024

print("La capacidad del disco duro es : ",gigabytes,"GB")
print("En megabytes es: ",megaby,"MB")
print("En kilobytes es: ",kiloby,"KB")
print("En bytes es: ",cby,"B")