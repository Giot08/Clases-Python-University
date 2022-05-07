#Ejercicio 2 - Modulo 2 / Programacion Basica (Python) IPP
#Estudiante: Jose Miguel Torres Medina - RUT: 25877201-6

"""
Enunciado:

Crea programa en Python que solicite al usuario:
1. Ingresar un número entero cualquiera del 1 al 9.
2. Luego solicitar que ingrese números secuenciales 
partiendo por 1, pero saltándose aquellos que sean 
múltiplos del valor ingresado al comienzo.
3. En caso de ingresar un valor erróneo, enviar un 
mensaje indicando el error y el número que correspondía ingresar.

"""

# Desde aqui empieza la solución del ejercicio

print('Bienvenido, vamos a jugar al numero secuencial')
num = int(input('Para jugar ingresa un numero del 1 al 9 \n'))

# Comprobamos que el numero ingresado sea entre 1 y el 9
while (num < 1 or num > 9):
    print(f"El numero {num} no es valido, por favor ingresa un numero valido")
    num = int(input('vuelve a ingresar un numero del 1 al 9 \n'))

# Aqui empieza el juego como tal.
print(f'A partir de aqui ingresa numeros que NO sean multiplos de {num} desde el 1')

# Con este IF hacemos nuevamente una validacion
if (num > 1 and num <= 9):
    # Definimos las variables donde num2 siempre sera el numero que ingrese como 
    # respuesta y num3 un calculo donde nos de un resto del numero con el cual 
    # elegimos jugar "num" y el numero ingresado en secuancia "num2"
    num2 = int(input(f'Ingresa un numero secuencial que no sea multiplo de {num} Recuerda que hay que empezar por el 1 \n'))
    num3 = num2 % num

    # Nos aseguramos que el primer numero de inicio del juego sea 1 y el valor de 
    # "num3" sea diferente de 0, para corroborar asi que no es un numero multiplo
    if(num3 != 0 and num2 == 1):

        # Creamos el While donde realizara la aplicacion constante de irnos pidiendo
        # un valor para nuestro juego
        while (num3 != 0):
            num2_b = num2
            num2_c = num2 + 1
            # Decidi hacer un poco mas complejo el codigo,
            # agregando 3 variaciones de num2 las cuales llamo "num2_b", "num2_c y num2_d"
            # Las que explicare mejor donde las uso y porque.

            # Aqui usamos el input donde ira ingresando en secuencia los numeros.
            num2 = int(input(f'Ingresa un numero secuencial que no sea multiplo de {num} \n'))
            
            # Aca utilizo una formula asignada a la variable "num2_d" donde es el producto del "num2"
            # recien ingresado por el usuario MENOS "num2_c" cuyo valor es el resultado de la suma
            # del num2 anterior al ingresado + 1
            num2_d = num2 - num2_c
            if(num2_d >= 2):
                print(f'Has perdido has ingresado un numero MAYOR al correspondiente')
                break
            # Gracias a esto me permite limitar al jugador a no ingresar numeros superiores al que
            # al que corresponde en ese momento, es decir, que no podra saltarse los numeros y
            # debera ingresarlos en secuencia

            # Aca uso el num2_b el cual posee el valor del "num2" ingresado anterior al actual
            # con este hago una comparacion del "num2" recien ingresado con el anterior a este
            # por lo tanto el jugador pierde si el valor es igual o menor, limitandolo que no
            # pueda volver a los numeros anteriores.
            elif(num2 <= num2_b):
                print(f'Has perdido has ingresado un numero menor o igual al anterior {num2}')
                break
            # Por ultimo el juego no exigia una victoria y decidi añadirla.
            elif(num2 >= 9 and num2_d <= 1):
                print('Felicidades has ganado!')
                break
            else:
                num3 = num2 % num
        if(num3 == 0):
            # Aqui la forma principal de perder ya ingresando un numero multiplo del inicial
            print(f'Has perdido, has Ingresado {num2} y correspondia {num2 + 1}')
    else:            
        # Un comprobante que te recuerda que has ingresado incorrectamente un dato.
        print('Has Ingresado mal, vuelve a intentarlo!')
    







