#Ejercicio 1 - Modulo 2 / Programacion Basica (Python) IPP
#Estudiante: Jose Miguel Torres Medina - RUT: 25877201-6

"""
Enunciado:

Debes crear un programa que dibuje una matriz, 
según las siguientes consideraciones:
1. Solicitud de filas
2. Solicitud de columnas
3. Se logre dibujar filas indicadas
4. Se logre dibujar columnas solicitadas.
"""

# Desde aqui empiza la solución al ejecicio
print('Bienvenido usuario, por favor seguir las instrucciones para el correcto uso de la aplicación, En esta app Dibujaremos una matriz a conveniencia')
# NOTA limitamos los valores entre 1 y 10 para evitar corrupciones del programa.

"""
Las variables de "matriz" son unicamente para usar como dibujo a imprimir,
no tienen otra funcion que repetirse las veces que el usuario desee.
"""
matriz_top = "+---+"
matriz_body = "|   |"
matriz_bot = "+---+"

# Usamos las variables de columnas y filas (col y row, en ingles)
col = int(input("Por favor ingrese el numero de Columnas, debe ser un numero entre 1 y 10\n"))
row = int(input("Por favor ingrese el numero de FILAS, debe ser unnumero entre 1 y 10\n"))

# Añadimos unas condiciones while para comprobar y evitar que se rompa el programa
while (col <= 0 or row <= 0 or col > 10 or row > 10):
    print(f"Error, has ingresado {col} y {row}, por favor ingresa numeros superiores a 0 y menores a 10 en ambas sentencias")
    col = int(input("Por favor ingrese nuevamente el numero de COLUMNAS, debe ser un numero entre 1 y 10\n"))
    row = int(input("Por favor ingrese nuevamente el numero de FILAS, debe ser un numero entre 1 y 10\n"))

# y por ultimo finalizamos con un bucle que imprimirá el resultado
for i in range(row):
    i = col
    print(matriz_top * i)
    print(matriz_body * i)
    print(matriz_bot * i)
