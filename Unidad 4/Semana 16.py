from idlelib.debugobj import myrepr

print("/////////Tarea: Trabajo con Archivos de Texto en Python////////")

# Abrimos el archivo en modo escritura
with open("my_notes.txt", "w") as file:

#1.Escritura de Archivo de Texto:

#nombre del archivo
 file_name = "my_notes.txt"
print(file_name)

#modo de apertura: "w" para la escritura (write)
file.write("Linea 1 : Estoy aprendiendo en Python \n")
file.write("Linea 2 : Me gusta aprender cosas nuevas \n")
file.write("Linea 3 : Me gusta dormir mucho \n")

#metodo del writelines () : escribimos la lista de lineas
lineas = ("linea 3 : todos los dias aprendo \n", "linea 4 : fin ejemplos \n ")

file.writelines(lineas)
file.write.close()

#abrimos el archivos que creamos.
archivo = open(file_name, "w")

file = open ("my_notes.txt", "w")

file.write("Estudio en la UEA.\n " )

file.write("Tengo 21 años. \n ")

file.write("vivo en Shell provincia Pastaza. \n ")

file.close()

#ahora haremos las lineas personales del archivo read y readline
file = open ("my_notes.txt", "r")
my_notes.write("linea 1 : Me gusta jugar en el celular")
my_notes.write("linea 2 : mi hija se llama Camila")
my_notes.write("linea 3 : me gusta viajar")

print( file.readlines() )
file.close()

