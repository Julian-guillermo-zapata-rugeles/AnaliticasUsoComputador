import pandas as pd
import matplotlib.pyplot as plt
import os
import math
import time
"""
Autor = Julián Guillermo Zapata Rugeles
Año   = 2021

Objetivo :
    generar imagenes de forma rapida

"""


def reporteDia():
    os.system("clear")
    global dataframe
    file_save = time.localtime()[0:3]
    dia_buscado = file_save[2]
    mes_buscado = file_save[1]
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


    ruta = os.popen("pwd").read().replace("\n","").replace(" ","")
    folder = "mkdir "+ruta+"/REPORTES/ 2>/dev/null"
    os.system(folder)
    file_name = ruta+"/REPORTES/"+str(file_save[0])+"-"+str(file_save[1])+"-"+str(file_save[2])+".png"
    plt.savefig(file_name)
    #new_data_frame['']



salir = False
names_header = ['dia','mes','año','hora','minutos','minutos_prueba','memoria_total','memoria_usada','porcentaje_usado','dispositivos_activos','ip']
dataframe = pd.read_csv ("ANALITICAS/analiticas.csv", delimiter =";" , names=names_header)

reporteDia()
