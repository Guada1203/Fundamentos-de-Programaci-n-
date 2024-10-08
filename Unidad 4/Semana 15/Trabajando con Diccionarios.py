#Utilizar diccionarios en Python para representar informacion estructurada y realizar operaciones comunes.

"""1. creamos un diccionario"""

informacion_personal = {"nombre" : "Alyla" , "edad" : 17 , "ciudad" : "ambato" , "profesion" : "estudiante" , }

"""2. acceder y modificar valores"""

#modificacion de ciudad

informacion_personal["ciudad"] = "MACAS"

informacion_personal["estudiante"] = ("profesion")

#clave valor nueva de la profesion

informacion_personal["profesion"] = "Estudiante de bachillerato"

for clave,valor in informacion_personal.items():
 print(clave, " : " ,valor)

 """3 verificar existencia de claves"""

informacion_personal["telefono"] = "09985767241"

""" 4. eliminar una clave """

del(informacion_personal["edad"])

print(informacion_personal)

print("**********fin tarea********")