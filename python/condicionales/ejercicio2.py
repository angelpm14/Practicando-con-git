#2.	Una tienda vende un producto a un precio unitario igual a S/. 20. Como oferta la tienda ofrece un porcentaje de descuento sobre el importe de la compra. Adicionalmente la tienda regala caramelos en base al número de unidades adquiridas del producto. Desarrolle el programa que determine el importe de la compra, el descuento, total a pagar y el número de caramelos del obsequio que se da al cliente por la compra realizada.

import os
os.system("cls")

unidades = float(input("cantidad de productos: "))

if unidades >= 1 and unidades <= 50:
    print("5 caramelos de regalo")

elif unidades >= 51 and unidades <= 100:
    print("se regalan 10 caramelos")

else: 
    print("Se regalan 15 caramelos")
importe = unidades * 20

print("El descuento seria...")
if importe > 700:
    descuento = importe * 0.16
    importe_pagar = importe - descuento  
    print("descuento",format(importe_pagar,".2f"))

elif importe < 700 and importe > 501:
    descuento = importe * 0.14
    importe_pagar = importe - descuento  
    print("descuento",format(importe_pagar,".2f"))

else :
    descuento = importe * 0.12
    importe_pagar = importe - descuento  
    print(f"descuento",format(importe_pagar,".2f"))