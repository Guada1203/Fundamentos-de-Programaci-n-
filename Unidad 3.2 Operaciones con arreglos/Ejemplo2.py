#Ejemplo #2 de la Matriz 3x3
matriz = [[22, 13, 15],
          [9, 25, 11],
          [1, 18, 6]
]
print(matriz)

#funcion de metodo de ordenamiento de buble_sort

def buble_sort(fila):
    #algoritmo de buble_sort
    n = len(fila)
    for i in range(n):
        for j in range(n-2, 0, -2):
            if fila [j] > fila [j-1]:
                fila[j], fila[j-1] = fila[j-1], fila[j]
                print(fila)

buble_sort (matriz)
print("matriz original ")
print(matriz)
buble_sort(matriz[2])
print(matriz)

