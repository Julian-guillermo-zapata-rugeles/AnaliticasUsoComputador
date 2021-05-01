import pandas as pd

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



menu = """
Desarrollado por Julián Guillermo Zapata Rugeles

+--------------------- analizador de datos ---------------------+\n
1 ) reporte específico (mes dia hora)
2 ) reporte por dia
2 ) reporte mensual
3 ) reporte rango horas

"""




def reporteEspecifico():
    global dataframe
    hora_buscada  =  int(input("Hora : "))
    fecha_buscada =  int(input("Dia  : "))
    mes_buscado   =  int(input("Mes  : "))
    dataframeBuscado = dataframe[(dataframe.dia == fecha_buscada)&(dataframe.hora == hora_buscada)]
    #mayorUsoCpu=dataframe[(dataframe.porcentaje_usado>60)&(dataframe.porcentaje_usado<90)]
    print(dataframeBuscado)
    print("porcentaje promedio usado  :",dataframeBuscado['porcentaje_usado'].mean())
    print("Promedio de activos en red :",dataframeBuscado['dispositivos_activos'].mean())






salir = False
names_header = ['dia','mes','año','hora','minutos','minutos_prueba','memoria_total','memoria_usada','porcentaje_usado','dispositivos_activos','ip']
dataframe = pd.read_csv ("ANALITICAS/analiticas.csv", delimiter =";" , names=names_header)


while salir == False:
    print(menu)
    entrada = str(input("eleccion : "))
