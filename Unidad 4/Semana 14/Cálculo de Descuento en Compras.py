"""Cálculo de Descuento en Compras"""

"""El objetivo de esta tarea es practicar el uso de funciones en Python, incluyendo parámetros, valores 
predeterminados y retorno de valores. Deberás crear un programa que calcule el descuento en compras en función del 
monto total de la compra y mostrar el monto final a pagar."""

#1. Creación de la Función para el calculo del descuento:
"""Crea una función llamada calcular_descuento que tome dos parámetros: el monto total de la compra y un valor predeterminado
 para el porcentaje de descuento (por ejemplo, 10% por defecto).
La función debe calcular el descuento aplicando el porcentaje al monto total de la compra.
La función debe devolver el monto del descuento calculado."""

monto_total1 = 175
def calcular_descuento(valor_total, porcentaje = 10):
    descuento = valor_total * porcentaje / monto_total1
    return descuento

descuento1 = calcular_descuento(150)
print('el monto total es:' , monto_total1)
print(f' su descuento es de',descuento1)

#2. Llamada a la Función:
""""Llama a la función calcular_descuento al menos dos veces desde el programa principal.
En una llamada, proporciona el monto total de la compra y, en la otra,
proporciona tanto el monto total de la compra como el porcentaje de descuento."""

monto_total2 = 700
descuento2 = calcular_descuento(valor_total = 700, porcentaje = 35)
print('el monto total es:' , monto_total2)
print(f' el descuento es de',descuento2)

