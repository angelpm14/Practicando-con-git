#9.	Una tienda ofrece un porcentaje de descuento sobre el importe de la compra de los cuatro tipos de productos cuyos códigos, precios unitarios y descuentos se muestran en las siguientes tablas. Desarrolle el programa que determine el importe de la compra, el descuento y el total a pagar por la compra de cierta cantidad de unidades de un mismo tipo de producto.

import os
os.system("cls")

codigo =float (input ("Escribe el monto o valor del codigo:"))
unidades_adqui = float(input ("Ingrese el monto o valor de unidades adquiridas:"))


importe_descuento=0
precio_unit=0
if codigo==101:
    precio_unit=17
if codigo==102:
    precio_unit=25
if codigo==103:
    precio_unit=16 
if codigo==104:
    precio_unit=27  


importe_compra = precio_unit * unidades_adqui
if unidades_adqui >= 1 and unidades_adqui <= 10:
    importe_descuento = importe_compra * 0.05
if unidades_adqui>=11 and unidades_adqui <= 20:
    importe_descuento=importe_compra * 0.08
if unidades_adqui >= 21 and unidades_adqui <= 30:
    importe_descuento = importe_compra * 0.1
if unidades_adqui >= 31:
    importe_descuento = importe_compra * 0.13



importe_a_pagar=importe_compra - importe_descuento
print ("Valor de importe a pagar: " + repr (importe_a_pagar))
print ("Valor de importe de la compra: " + repr (importe_compra))
print ("Valor de importe del descuento: " + repr (importe_descuento))
print ("Valor de precio unitario: " + repr (precio_unit))