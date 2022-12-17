#16.	El cálculo del pago mensual de un empleado de una empresa se efectúa de la siguiente manera: el sueldo básico se calcula sobre la base del número total de horas trabajadas basado en una tarifa horaria, al sueldo básico, se le aplica una bonificación del 20% obteniéndose el sueldo bruto; al sueldo bruto, se le aplica un descuento del 10% obteniéndose el sueldo neto. Desarrolle el programa que muestre el sueldo básico, bruto y neto de un trabajador.

import os
os.system("cls")

horas_trabajada = float(input("Ingrese las horas trabajadas: "))
tarifa_horaria = float(input("Ingrese la tarifa horaria: "))

sueldo_basic = tarifa_horaria * horas_trabajada
bonificacion = sueldo_basic * 0.20
sueldo_bruto = sueldo_basic + bonificacion
descuento = sueldo_bruto * 0.10
sueldo_neto = sueldo_bruto - descuento

print("Sueldo basico: ",format(sueldo_basic,".2f"))
print("Sueldo bruto: ",format(sueldo_bruto,".2f"))
print("Sueldo net: ",format(sueldo_neto,".2f"))