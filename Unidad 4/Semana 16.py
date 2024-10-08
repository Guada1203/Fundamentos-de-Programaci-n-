print("/////////Tarea: Trabajo con Archivos de Texto en Python////////")

#1.Escritura de Archivo de Texto:

#nombre del archivo
file_name = "my_notes.txt"

#modo de apertura: "w" para la escritura (write)

#abrimos el archivos que creamos.
archivo = open(file_name, "w")

file = open ("my_notes.txt", "w")

file.write("Estudio en la UEA.\n " )

file.write("Tengo 21 años. \n ")

file.write("vivo en Shell provincia Pastaza. \n ")

file.close()

#ahora haremos las lineas personales del archivo read y readline
file = open ("my_notes.txt", "r")
archivo_escritura.write("linea 1 : Me gusta jugar en el celular")
archivo_escritura.write("linea 2 : mi hija se llama Camila")
archivo_escritura.write("linea 3 : me gusta viajar")

print( file.readlines() )
file.close()

