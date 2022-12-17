#10.	Un curso se evalúa sobre la base de 5 notas de las cuales se elimina las notas de mayor y menor puntaje. Desarrolle el programa que muestre las notas eliminadas y el promedio aprobatorio.

import os
os.system("cls")

print("             --Digite sus 4 notas--")
n_1 = int(input("Digite su nota 1: "))
n_2 = int(input("Digite su nota 2: "))
n_3 = int(input("Digite su nota 3: "))
n_4 = int(input("Digite su nota 4: "))

nota_mala = 0

if n_1 < n_2 and n_1 < n_3 and n_1 < n_4:
    nota_mala = n_1
    prom = (n_1 * n_2 * n_3 * n_4 - nota_mala)/ 3
    print(f"La nota baja es {nota_mala}")
    print(f"Su promedio fue {prom} y la nota mas baja es {nota_mala}")

elif n_2 < n_1 and n_2 < n_3 and n_2 < n_4:
    nota_mala = n_2
    prom = (n_1 * n_2 * n_3 * n_4 - nota_mala)/ 3
    print(f"La nota baja es {nota_mala}")
    print(f"Su promedio fue {prom} y la nota mas baja es {nota_mala}")

elif n_3 < n_1 and n_3 < n_2 and n_3 < n_4:
    nota_mala = n_3
    prom = (n_1 * n_2 * n_3 * n_4 - nota_mala)/ 3
    print(f"La nota baja es {nota_mala}")
    print(f"Su promedio fue {prom} y la nota mas baja es {nota_mala}")

elif n_4 < n_1 and n_4 < n_2 and n_4 < n_3:
    nota_mala = n_4
    prom = (n_1 * n_2 * n_3 * n_4 - nota_mala)/ 3
    print(f"La nota baja es {nota_mala}")
    print(f"Su promedio fue {prom} y la nota mas baja es {nota_mala}")