# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 17:41:15 2023

@author: Cupi2
"""

import calculo_edad as mod

def ejecutar_calcular_edad()->None:
    
    #Se solicitan las fechas al usuario
    print("Por favor ingrese la fecha actual") 
    anio_actual = int(input("Año: "))
    mes_actual = int(input("Mes: "))
    dia_actual = int(input("Día: "))

    print("\nAhora ingrese la fecha de nacimiento") 
    anio_nacimiento = int(input("Año: "))
    mes_nacimiento = int(input("Mes: "))
    dia_nacimiento = int(input("Día: "))
    
    #Se calcula la edad de la persona usando la función calcular_edad
    #y se imprime el resultado por pantalla
    resultado = mod.calcular_edad(anio_actual, mes_actual, dia_actual, anio_nacimiento, mes_nacimiento, dia_nacimiento)
    print(resultado)

def iniciar_aplicacion()->None:
    print("BIENVENIDO A LA CALCULADORA DE EDADES \n")
    ejecutar_calcular_edad()

#PROGRAMA PRINCIPAL
iniciar_aplicacion()
