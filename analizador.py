import pandas as pd
import matplotlib.pyplot as plt
import os
import math
import time
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

    dataframeHoras = dataframe['hora'].unique() # obtendré los horas disponibles durante el día
    tmp_list_prom = []
    tmp_list_hour = []
    for hour_avalibles in dataframeHoras:
        #print(type(hour_avalibles))
        tmp_data = dataframeBuscado[dataframeBuscado.hora == hour_avalibles]
        promedio_dispositivos = tmp_data['dispositivos_activos'].mean()
        tmp_list_prom.append(promedio_dispositivos)
        tmp_list_hour.append(hour_avalibles)

    new_data_frame = pd.DataFrame()
    new_data_frame['hora']=tmp_list_hour
    new_data_frame['promedio']=tmp_list_prom

    #print(new_data_frame)
    eje_x = new_data_frame['hora']
    eje_y = new_data_frame['promedio']

    #eje_x2 = dataframeBuscado['minutos']
    #eje_y2 = dataframeBuscado['dispositivos_activos']


    c=new_data_frame['promedio'].mean()
    plt.title("( Proyecto ARCU Julian Guillermo Zapata Rugeles) Analiticas del  dia {}  --> mes {}".format(dia_buscado,mes_buscado))
    plt.axhline(y=c, color='r', linestyle='-')
    plt.plot(eje_x, eje_y, color='#a12424' ,linestyle='dashed')
    #plt.plot(eje_x2, eje_y2, color='#4bb27b' ,linestyle='dashed')

    file_save = time.localtime()[0:3]
    os.system("mkdir REPORTES/ 2>/dev/null")
    file_name = "REPORTES/"+str(file_save[0])+"-"+str(file_save[1])+"-"+str(file_save[2])+".png"
    plt.savefig(file_name)
    plt.show()
    #new_data_frame['']












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
