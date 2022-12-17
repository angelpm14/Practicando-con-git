#20.	Desarrolle el programa que lea tres números a, b, c y determine si los números fueron ingresados en orden ascendente, descendente o en desorden.
import os
os.system("cls")

n = int(input(" INGRESE SU NUMERO DE 3 DIGITOS: "))

a = int(input("El primer digito es: "))
b = int(input("El segundo digito es: "))
c = int(input("El tercer digito es: "))


if a < b < c :
    print("El numero esta ordenado en ascendentemente")

elif a > b > c :
    print("El numero esta ordenado en descendentemente")

else :
    print("El numero esta desordenado")
