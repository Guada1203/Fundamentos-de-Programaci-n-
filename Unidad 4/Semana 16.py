print("/////////Tarea: Trabajo con Archivos de Texto en Python////////")

#Abrimos archivos en Python
file_name = "mis_notas_personales.txt"

#modo de apertura: "w" para la escritura (write)
#abrimos el archivo que creamos

archivo = open(file_name, "w")
print(file_name)

#metodo write(): una linea a la vex
archivo.write('Linea 1: Tengo 21 años. \n')
archivo.write('Linea 2: Estudio en la UEA. \n')
archivo.write('Linea 3: Vivo en Shell provincia de Pastaza. \n')

#metodo writelines(): escribe una lista de lineas
lineas = ["Linea 3: Cumplo años en diciembre \n", "Linea 2: Mi ma es... \n"]
mis_notas_personales.writelineas(lineas)

#modo apertura: "r" para la lectura (read)
archivo_lectura = open(file_name, "r")
#metodo readline()
#leemos y mostramos el contenido
contenido = archivo_lectura.read()
print("contenido del archivo despues de escribir")
print(contenido)

#cerramos el archivo de lectura
archivo_lectura.close()










