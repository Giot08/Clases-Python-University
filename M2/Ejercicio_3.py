#Ejercicio 3 - Modulo 2 / Programacion Basica (Python) IPP
#Estudiante: Jose Miguel Torres Medina - RUT: 25877201-6

"""
Enunciado:

Un año bisiesto es un año con 366 días en vez de 365. Cada 4 años, febrero tiene un día más. Esto se
hace porque un año oficialmente no tiene 365 días, sino 365,25 días. Añadiendo un día cada 4 años, se
soluciona este problema.
Cualquier año divisible por 4 es un año bisiesto, como 2016, 2020, 2024, 2028.
Nota: La regla anterior no se aplica a los años de siglo.
Siglos como 1900 y 2000 solo tienen un día bisiesto si son divisibles por 400.
1900 es divisible entre 4 y también entre 100, pero no entre 400, por lo que no es un año bisiesto.
Esto significa que los siglos son solo un año bisiesto si son divisibles por 400.
Entonces 1900 no lo es, 2000 lo es, 2100, 2200, 2300 no lo es, pero 2400 es otro año bisiesto.
Cree un programa, donde:

1. Dado el año de nacimiento de una persona
2. El año de muerte
3. Ingresar un cero en caso de estar vivo aún
4. El sistema debe reemplazar el cero por el año actual
5. se determine la cantidad de años bisiestos que le ha tocado vivir.

"""

#Desde aqui empieza la solución del ejercicio
print('Bienvenido, vamos a calcular los años biciestos que hay entre dos fechas.')
# Primero creamos variables con los requerimientos
nac = int(input("ingresa el año de nacimiento o de inicio \n"))
mue = int(input("ingresa el año de Muerte o de termino si aun no sucede ingresa 0\n"))

# Hacemos validacion de que nacimiento debe ser mayor a 0
if (nac < 0):
    while (nac < 0):
        print('Por favor ingresa una fecha valida')
        nac = int(input("ingresa el año de nacimiento o de inicio \n"))

# Devolvemos una nueva variable para muertes, en caso de que siga vivo el usuario usara 0 para señalarlo
if (mue == 0):
    mue = 2022

# Por ultimo hacemos una Validacion de que el año de nacimiento sea menor que el año de muerte para evitar complicaciones
if(nac > mue):
    while (nac >  mue):
        nac = int(input("ingresa el año de nacimiento o de inicio, que sea menor al año de muerte \n"))
        mue = int(input("ingresa el año de Muerte o de termino si aun no sucede ingresa 0\n"))
        if (mue == 0):
            mue = 2022
        

# Agregamos contador donde aumentaremos cada vez que el bucle encuentre un año biciesto
cont = 0

# Creamos el bucle con el rango entre Nacimiento (nac) y muerte (mue)
for i in range (nac, mue):
    # Creamos dos variables nuevas "mil" que nos dara un numero respecto a la cantidad de unidades del año, ejemplo si es 1956 nos dara 4 si es 803 nos dara 3 y asi sucesivamente.
    # Mientras que Millenium transformara el año en un String.
    mil = len(str(i))
    millenium = str(i)
    # Por ultimo lo que hacemos es que itere sobre los años que posean 4 unidades, luego con nuestra variable "millenium" seleccionamos las dos ultimas posiciones, por ejemplo 19[9][8] donde los datos dentro de los [] serian las posiciones 2 y 3 respectivamente y las asignamos a la variable mil_a de forma conjunta
    if (mil == 4):
        mil_a = millenium[2] + millenium[3]
    #Aca obtenemos los siglos Biciestos
    if (mil == 4):
        #por ultimo hacemos que los años con terminacion en "00" se les realice un porcentual sobre 400, de esta forma obtener los siglos que sean biciestos.
        if(mil_a == "00" ):
            a = i % 400
            if(a == 0):
                # Una vez encontrado el siglo Biciesto aumenta el contador en 1
                cont +=1
        else:
            #para el resto de años que no sean siglos les realizamos el porcentual con el numero 4
            a = i % 4
            if(a == 0):
                # y los que obtengamos sobrante 0 aumentara el contador
                cont +=1
    else:
        # Por ultimo utilizamos los años menores a 1000 los cuales pueden ser divididos por 4 igualmente.
        a = i % 4
        if(a == 0):
            cont +=1
# y de esta forma obtenemos el resultado final exigido.
print(f"La cantidad de años biciestos entre {nac} y {mue} es de {cont}")
