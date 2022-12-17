#4.	El promedio final de un curso se obtiene en base al promedio simple de tres prácticas calificadas. Para ayudar a los alumnos, el profesor del curso ha prometido incrementar en dos puntos la nota de la tercera práctica calificada, si es que esta no es menor que 10. Desarrolle el programa que determine el promedio final de un alumno conociendo sus tres notas. 

import os
os.system("cls")

nota_a = float(input("Ingrese su primera nota: "))
nota_b = float(input("Ingrese su segunda nota: "))
nota_c = float(input("Ingrese su tercera nota: "))

if nota_c < 10:
    nota_c +=2

promedio = float((nota_a + nota_b + nota_c)/3)

print(promedio)