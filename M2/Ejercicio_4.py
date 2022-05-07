#Ejercicio 4 - Modulo 2 / Programacion Basica (Python) IPP
#Estudiante: Jose Miguel Torres Medina - RUT: 25877201-6

"""
Enunciado:

Escoje 2 palabras del mismo largo en que dos letras iguales no coincidan
en la misma posición. Por ejemplo, si escojo las palabras morena y pelito,
toda m que aparezca en mi frase será reemplazada por una p, las letras o
se reemplazan por la e, las r por l, las e por i, las n por t y las a por
o. Quedando una frase de la siguiente manera

    morena
    pelito
    ingrese la frase a codificar: este es un gran dia
    tu nueva frase es: Esti is ut glot dio

Considera:
1. Escoje las 2 palabras de acuerdo a lo solicitado
2. solicita la frase al usuario
3. reemplaza los valores
4. imprime la nueva frase

"""

#Desde aqui empieza la solución del ejercicio

# Se decidio usar las palabras
# si Cambiamos Word1 por morena y word2 por pelito nos da el resultado del ejemplo.
word1 = 'contra'
word2 = 'fuerte'
# El input a ingresar
frase = str(input("Ingrese la frase a la cual va a transformar sus caracteres \n"))

# Variable para la nueva frase
nueva_frase = frase

# variable para saber el numero de veces q recorrera nuestro while
c = len(frase)
# variable que indica cuando empezar y en que posicion del caracter empezar
a = 0

while a <= c:
    #el punto de ruptura del while
    if (a == c):
        break
    # Decidi usar el mismo metodo de codigo, donde hace una consulta
    # al recorrido, de si  es igual al caracter de "word1" entonces remplace ese
    # caracter con el de "word2" que ocupe una misma posicion.
    if (word1[0] == frase[a]):
        nueva_frase = nueva_frase.replace(frase[a], word2[0])

    elif (word1[1] == frase[a]):
        nueva_frase = nueva_frase.replace(frase[a], word2[1])    

    elif (word1[2] == frase[a]):
        nueva_frase = nueva_frase.replace(frase[a], word2[2])    

    elif (word1[3] == frase[a]):
        nueva_frase = nueva_frase.replace(frase[a], word2[3])

    elif (word1[4] == frase[a]):
        nueva_frase = nueva_frase.replace(frase[a], word2[4])

    elif (word1[5] == frase[a]):
        nueva_frase = nueva_frase.replace(frase[a], word2[5])
    # Aumentamos el nro de iteraciones evitando el bucle infinito
    a += 1

# Por ultimo salida del resultado
print(f'Su frase era: {frase} \ny su nueva Frase es: {nueva_frase}')