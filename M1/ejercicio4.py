# Programa que devuelva el digito verificador ingresando unicamente los 8 digitos primeros del rut.
# // Realizado por Jose Torres 25.877.201-6
#
# Considero que para realizar esta tarea bajo las condiciones que son utilizar solo el contenido
# comprendido en el documento teórico del M1 quedaria un codigo muy largo, pues no mencionan
# mas alla del print, las variables y los inputs por mencionar algunos, entonces para realizar
# el ejercicio tendria que ser con 8 inputs para poder realizar las asignaciones digito a digito.
# debido a esto se utilizara un único input y trabajando con la posicion comprendida dentro del 
# mismo con un serie de [ ]

print("Bienvenido, por favor ingresa tu Rut sin el digito verificador ni los puntos, ej.: 10123123")
rut_input = input("ingresa tu Rut \n")
calc = (int(rut_input[7]) * 2) + (int(rut_input[6]) * 3) + (int(rut_input[5]) * 4) + (int(rut_input[4]) * 5) + (int(rut_input[3]) * 6) + (int(rut_input[2]) * 7) + (int(rut_input[1]) * 2) + (int(rut_input[0]) * 3)
calc = int(calc % 11)
print("su digito verificador es: " + str(calc) + " por lo tanto su rut completo seria: " + str(rut_input) + "-" + str(calc))
# Recordemos que el resultado puede dar 10 u 11, pero segun la tarea no son relevantes para este ejercicio, por lo tanto lo dejamos asi.