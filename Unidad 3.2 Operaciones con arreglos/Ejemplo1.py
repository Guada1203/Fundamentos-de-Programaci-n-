#Matriz de 3 x
matriz = [
    [2, 6, 12],
    [4, 8, 1 ],
    [5, 3, 9 ]
]

print(matriz)
#funcion para buscar los valores especificos

def buscar_valor(matriz,encontrar_valor):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == encontrar_valor:
                return i,j

encontrar_valor = 9
"""print(buscar_valor(matriz,encontrar_valor))"""

if encontrar_valor == encontrar_valor:
    print("Valor encontrado en la posicion", buscar_valor(matriz,encontrar_valor))
else:
    print("Valor invalido")