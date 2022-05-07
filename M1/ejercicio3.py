# Programa que calcula el promedio las notas según el porcenjate valido del tipo de evaluación
# // Realizado por Jose Torres 25.877.201-6
print("\nPor favor ingresa a continuación tus notas en el orden que se solicita \n le recordamos que Laboratorio y Las Tareas tienen en total 15% c/u de la nota final \n mientras que las evaluaciones Solemne tienen un 35% cada una, dando el total de 100%")
lab1 = float(input("Por favor ingresa tú nota obtenida en el Laboratorio #1 \n"))
lab2 = float(input("Por favor ingresa tú nota obtenida en el Laboratorio #2 \n"))
lab3 = float(input("Por favor ingresa tú nota obtenida en el Laboratorio #3 \n"))
hw1 = float(input("Por favor ingresa tú nota obtenida en la Tarea #1 \n"))
hw2 = float(input("Por favor ingresa tú nota obtenida en la Tarea #2 \n"))
hw3 = float(input("Por favor ingresa tú nota obtenida en la Tarea #3 \n"))
exam1 = float(input("Por favor ingresa tú nota obtenida en la evaluación Solemne #1 \n"))
exam2 = float(input("Por favor ingresa tú nota obtenida en la evaluación Solemne #2 \n"))
#
labs_promedio = (lab1 + lab2 + lab3) / 3
labs_final = labs_promedio * 0.15
#
hw_promedio = (hw1 + hw2 + hw3) / 3
hw_final = hw_promedio * 0.153

#
exam1_promedio = exam1 * 0.35
exam2_promedio = exam2 * 0.35
#
nota = labs_final + hw_final + exam1_promedio + exam2_promedio
print("Tú media de nota en los Laboratorios fué de: "+ str(labs_promedio) + " que equivalen a " + str(labs_final) + " de la nota final")
print("Tú media de nota en las Tareas fué de: "+ str(hw_promedio) + " que equivalen a " + str(hw_final) + " de la nota final")
print("Tú nota en la evaluación solemne 1 fué de: "+ str(exam1) + " que equivalen a " + str(exam1_promedio) + " de la nota final")
print("Tú nota en la evaluación solemne 2 fué de: "+ str(exam2) + " que equivalen a " + str(exam2_promedio) + " de la nota final")
#
print("Por lo tanto tu nota final del curso fué de: " + str(nota))