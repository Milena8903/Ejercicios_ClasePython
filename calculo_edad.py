# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 17:41:15 2023

@author: Cupi2
"""

def fecha_a_dias(anio: int, mes: int, dia: int)->int:
    """ Convierte una fecha a días, ingresada como año, mes y día. Se
    supone que todos los meses tienen 30 días.
    Parámetros:
        anio (int) Año de la fecha. Número entero positivo.
        mes (int) Mes de la fecha. Número entero positivo.
        dia (int) Día de la fecha. Número entero positivo.
    Retorno:
        int: La fecha ingresada convertida a días.
    """
    #TODO: implemente la función de acuerdo a su documentación
    anio = anio * 360
    mes = mes * 30
    cantidad_dias = anio + mes + dia
    return cantidad_dias


def diferencia_fechas (anio_fecha2: int, mes_fecha2: int, dia_fecha2: int,
                       anio_fecha1: int, mes_fecha1: int, dia_fecha1: int)->int:
    """ Calcula la diferencia en días entre dos fechas cualesquiera fecha1 y 
    fecha2 (expresadas en año, mes y día). Se supone que la fecha2 siempre 
    es superior a la fecha1. 
    Parámetros:
        anio_fecha2 (int) Año de la fecha2. Número entero positivo.
        mes_fecha2 (int) Mes de la fecha2. Número entero positivo.
        dia_fecha2 (int) Día de la fecha2. Número entero positivo.
        anio_fecha1 (int) Año de la fecha1. Número entero positivo.
        mes_fecha1 (int) Mes de la fecha1. Número entero positivo.
        dia_fecha1 (int) Día de la fecha1. Número entero positivo.
    Retorno:
        int: Diferencia en días entre las dos fechas.
    """
    #TODO: implemente la función de acuerdo a su documentación
    anio_fecha1 = anio_fecha1 * 360
    mes_fecha1 = mes_fecha1 * 30
    fecha1 = anio_fecha1 + mes_fecha1 + dia_fecha1
    
    anio_fecha2 = anio_fecha2 * 360
    mes_fecha2 = mes_fecha2 * 30
    fecha2 = anio_fecha2 + mes_fecha2 + dia_fecha2
    
    diferencia = fecha2 - fecha1
    return diferencia

def calcular_edad (anio_actual: int, mes_actual: int, dia_actual: int,
                   anio_nacimiento: int, mes_nacimiento: int, 
                   dia_nacimiento: int)->str:
    """ Calcula la edad de un persona dada su fecha de nacimiento y la fecha
    actual. 
    Parámetros:
        anio_actual (int) Año actual. Número entero positivo.
        mes_actual (int) Mes actual. Número entero positivo.
        dia_actual (int) Día actual. Número entero positivo.
        anio_nacimiento (int) Año de nacimiento. Número entero positivo.
        mes_nacimiento (int) Mes de nacimiento. Número entero positivo.
        dia_nacimiento (int) Día de nacimiento. Número entero positivo.
    Retorno:
        str: Mensaje informando la edad de la persona. El mensaje debe tener
        el siguiente formato: "La persona tiene X años, Y meses y Z días"
    """
    #TODO: implemente la función de acuerdo a su documentación
    anio_actual = anio_actual * 360
    mes_actual = mes_actual * 30
    fecha1 = anio_actual + mes_actual + dia_actual
    
    anio_nacimiento = anio_nacimiento * 360
    mes_nacimiento = mes_nacimiento * 30
    fecha2 = anio_nacimiento + mes_nacimiento + dia_nacimiento
    
    diferencia = fecha1 - fecha2
    
    anio = diferencia // 360
    anio2 = diferencia % 360
    mes = anio2 // 30
    dia = mes % 30
    
    respuesta = "La persona tiene " + str(anio) + " años " + \
                 str(mes) + " meses " + str(dia) + " días."
    
    return(respuesta)
