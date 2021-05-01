import pandas as pd
import matplotlib.pyplot as plt
import os
import math

"""
Autor = Julián Guillermo Zapata Rugeles
Año   = 2021

Objetivo :
    Este script tiene como Objetivo generar las estadisticas necesarias para en análisis de uso
    los reportes se generarán a partir de las analíticas que genera el script recolector
    el recolector está diseñado en entornos tipo LINUX donde los comandos de salida
    grep y awk están disponibles
    las adaptaciones para entornos windows es posible pero es necesario reemplazar los comandos equivalentes
    en el recolector. si conoce la estructura y powershell manipule la salida estandar para alimentar el algoritmo
    de recolección.
"""



def reporteEspecifico():
    global dataframe
    hora_buscada  =  int(input("Hora : "))
    dia_buscado =    int(input("Dia  : "))
    mes_buscado   =  int(input("Mes  : "))
    dataframeBuscado = dataframe[(dataframe.dia == dia_buscado)&(dataframe.hora == hora_buscada)]
    #mayorUsoCpu=dataframe[(dataframe.porcentaje_usado>60)&(dataframe.porcentaje_usado<90)]
    os.system("clear");
    print("+------------------------- resultados -------------------------+")
    print(dataframeBuscado.info())
    print("+------------------------- analiticas -------------------------+\n")
    print("promedio RAM usada             : ",dataframeBuscado['porcentaje_usado'].mean(),"%")
    print("Promedio de activos en red     : ",math.ceil(dataframeBuscado['dispositivos_activos'].mean()))
    print("Desviacion standard conectados : ",dataframeBuscado['dispositivos_activos'].std())
    print("Maximo dispositivo detectados  : ",dataframeBuscado['dispositivos_activos'].max())
    print("Minimo dispositivo detectados  : ",dataframeBuscado['dispositivos_activos'].min())
    print("Minutos activos en la hora     : ",dataframeBuscado['minutos_prueba'].sum() )
    print("Porcentaje actividad           : ",(dataframeBuscado['minutos_prueba'].sum()*100)/60,"%")

    titulo = "conexiones por minuto dia {} mes {} Desde {} hasta {}" .format(dia_buscado,mes_buscado,hora_buscada,hora_buscada+1)
    eje_x = dataframeBuscado['minutos']
    eje_y = dataframeBuscado['dispositivos_activos']

    c=dataframeBuscado['dispositivos_activos'].mean()
    plt.title(titulo)
    plt.axhline(y=c, color='r', linestyle='-')
    plt.plot(eje_x, eje_y, color='#a12424' ,linestyle='dashed')
    plt.show()





def reporteDia():
    os.system("clear")
    global dataframe
    dia_buscado = int(input("Ingrese el dia : "))
    mes_buscado = int(input("Ingrese el mes : "))
    dataframeBuscado = dataframe[(dataframe.mes == mes_buscado)&(dataframe.dia == dia_buscado)]
    #print(dataframe)
    print("+------------------------- resultados -------------------------+")
    print(dataframeBuscado.info())
    print("+------------------------- analiticas -------------------------+\n")
    print("promedio RAM usada             : ",dataframeBuscado['porcentaje_usado'].mean(),"%")
    print("Promedio de activos en red     : ",math.ceil(dataframeBuscado['dispositivos_activos'].mean()))
    print("Desviacion standard conectados : ",dataframeBuscado['dispositivos_activos'].std())
    print("Maximo dispositivo detectados  : ",dataframeBuscado['dispositivos_activos'].max())
    print("Minimo dispositivo detectados  : ",dataframeBuscado['dispositivos_activos'].min())
    print("Minutos activos en la dia      : ",dataframeBuscado['minutos_prueba'].sum() )
    print("equivalente  (horas x dia)     : ",dataframeBuscado['minutos_prueba'].sum()/60,"horas")
    #print("Porcentaje actividad           : ",(dataframeBuscado['minutos_prueba'].sum()*100)/60,"%")














salir = False
names_header = ['dia','mes','año','hora','minutos','minutos_prueba','memoria_total','memoria_usada','porcentaje_usado','dispositivos_activos','ip']
dataframe = pd.read_csv ("ANALITICAS/analiticas.csv", delimiter =";" , names=names_header)


menu = """
Desarrollado por Julián Guillermo Zapata Rugeles

+--------------------- analizador de datos ---------------------+\n
1 ) reporte específico (mes dia hora)
2 ) reporte por dia
2 ) reporte mensual
3 ) reporte rango horas

"""

while salir == False:
    print(menu)
    entrada = str(input("eleccion : "))
    if entrada=="1":
        reporteEspecifico()
    elif entrada=="2":
        reporteDia()
