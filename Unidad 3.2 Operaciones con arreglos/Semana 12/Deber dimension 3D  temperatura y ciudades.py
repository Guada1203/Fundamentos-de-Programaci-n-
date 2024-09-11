"""Crear una matriz 3D que represente los datos de temperaturas diarias en varias ciudades. En una dimensión, puedes tener diferentes ciudades, en otra dimensión, días de la semana (Lunes, Martes, Miércoles, etc.), y en la tercera dimensión, semanas.
Dentro de cada celda de la matriz, puedes almacenar las temperaturas diarias para una ciudad en un día específico de una semana determinada.
Utilizar bucles anidados para calcular el promedio de temperaturas para una ciudad por cada una de las semanas.
Mostrar el promedio de temperaturas para cada ciudad y semana en la pantalla."""

# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)

""" Matriz en 3D"""
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"dias": "Lunes", "temp": 32},
            {"dias": "Martes", "temp": 45},
            {"dias": "Miércoles", "temp": 24},
            {"dias": "Jueves", "temp": 35},
            {"dias": "Viernes", "temp": 42},
            {"dias": "Sábado", "temp": 29},
            {"dias": "Domingo", "temp": 18}
        ],
        [   # Semana 2
            {"dias": "Lunes", "temp": 45},
            {"dias": "Martes", "temp": 53},
            {"dias": "Miércoles", "temp": 38},
            {"dias": "Jueves", "temp": 50},
            {"dias": "Viernes", "temp": 35},
            {"dias": "Sábado", "temp": 40},
            {"dias": "Domingo", "temp": 55}
        ],
        [   # Semana 3
            {"dias": "Lunes", "temp": 60},
            {"dias": "Martes", "temp": 65},
            {"dias": "Miércoles", "temp": 57},
            {"dias": "Jueves", "temp": 72},
            {"dias": "Viernes", "temp": 66},
            {"dias": "Sábado", "temp": 75},
            {"dias": "Domingo", "temp": 59}
        ],
        [   # Semana 4
            {"dias": "Lunes", "temp": 43},
            {"dias": "Martes", "temp": 38},
            {"dias": "Miércoles", "temp": 40},
            {"dias": "Jueves", "temp": 39},
            {"dias": "Viernes", "temp": 44},
            {"dias": "Sábado", "temp": 32},
            {"dias": "Domingo", "temp": 28}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"dias": "Lunes", "temp": 25},
            {"dias": "Martes", "temp": 43},
            {"dias": "Miércoles", "temp": 58},
            {"dias": "Jueves", "temp": 50},
            {"dias": "Viernes", "temp": 35},
            {"dias": "Sábado", "temp": 28},
            {"dias": "Domingo", "temp": 43}
        ],
        [   # Semana 2
            {"dias": "Lunes", "temp": 53},
            {"dias": "Martes", "temp": 76},
            {"dias": "Miércoles", "temp": 70},
            {"dias": "Jueves", "temp": 74},
            {"dias": "Viernes", "temp": 72},
            {"dias": "Sábado", "temp": 47},
            {"dias": "Domingo", "temp": 51}
        ],
        [   # Semana 3
            {"dias": "Lunes", "temp": 53},
            {"dias": "Martes", "temp": 46},
            {"dias": "Miércoles", "temp": 79},
            {"dias": "Jueves", "temp": 70},
            {"dias": "Viernes", "temp": 52},
            {"dias": "Sábado", "temp": 76},
            {"dias": "Domingo", "temp": 80}
        ],
        [   # Semana 4
            {"dias": "Lunes", "temp": 24},
            {"dias": "Martes", "temp": 32},
            {"dias": "Miércoles", "temp": 36},
            {"dias": "Jueves", "temp": 44},
            {"dias": "Viernes", "temp": 52},
            {"dias": "Sábado", "temp": 48},
            {"dias": "Domingo", "temp": 60}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"dias": "Lunes", "temp": 40},
            {"dias": "Martes", "temp": 54},
            {"dias": "Miércoles", "temp": 34},
            {"dias": "Jueves", "temp": 45},
            {"dias": "Viernes", "temp": 58},
            {"dias": "Sábado", "temp": 65},
            {"dias": "Domingo", "temp": 22}
        ],
        [   # Semana 2
            {"dias": "Lunes", "temp": 89},
            {"dias": "Martes", "temp": 91},
            {"dias": "Miércoles", "temp": 93},
            {"dias": "Jueves", "temp": 90},
            {"dias": "Viernes", "temp": 87},
            {"dias": "Sábado", "temp": 84},
            {"dias": "Domingo", "temp": 81}
        ],
        [   # Semana 3
            {"dias": "Lunes", "temp": 91},
            {"dias": "Martes", "temp": 90},
            {"dias": "Miércoles", "temp": 73},
            {"dias": "Jueves", "temp": 75},
            {"dias": "Viernes", "temp": 63},
            {"dias": "Sábado", "temp": 58},
            {"dias": "Domingo", "temp": 47}
        ],
        [   # Semana 4
            {"dias": "Lunes", "temp": 50},
            {"dias": "Martes", "temp": 40},
            {"dias": "Miércoles", "temp": 30},
            {"dias": "Jueves", "temp": 20},
            {"dias": "Viernes", "temp": 35},
            {"dias": "Sábado", "temp": 43},
            {"dias": "Domingo", "temp": 60}
        ]
    ]
]

#calcular el promedio de las temperaturas de cada ciudad y semana

for ciudad in temperaturas:
    for semana in ciudad:
        suma = 0
        for dias in semana:
            suma += dias["temp"]
            print("el promedio es: ",suma)

while True:

    print("selecciona una ciudad:")
    print("1. Ciudad 1")
    print("2. Ciudad 2")
    print("3. Ciudad 3")
    print("4. salir")

    opcion = input("ingrese la opcion buscada:")
    if opcion == "3":
        ciudad = temperaturas [0]
        print(ciudad)
    else:
        print("la opcion es invalida")
    continue
