import os
import time
import dispositivos
import speed
"""



Autor = Julián Guillermo Zapata Rugeles
Año   = 2021

    Obtener analíticas de uso de la computadora para análisis de tiempo
    se recoletará la siguiente información para la generación de un dataset sencillo de
    actividad contra días

    el dataset se organizará en una archivo de tipo csv delimitado por ;
    su organización será la siguiente :

    #################################################################
    #                                                               #
    #        ESTA SERÁ LA SALIDA QUE PRODUCIRÁ EL ALGORITMO         #
    #                                                               #
    #################################################################


    [ DIA ; MES ; AÑO ; HORA ; MINUTOS ; MINUTOS POR PRUEBA; MEMORIA DISPONIBLE;
      MEMORIA USADA; PORCENTAJE; CONECTADOS RED; IP'S ;VEL BAJADA ; VEL SUBIDA ]




"""



class RecolectorInformacion():
    """recolector de informacion"""

    def __init__(self):
        self.__ruta_uso = os.popen("pwd").read().replace("\n","").replace(" ","")+"/"
        self.__save_folder = "ANALITICAS/"
        self.__file_name = "analiticas.csv"




    def generarRegistro(self , minutos ):
        struct_time = time.localtime()
        date = str(struct_time[2])+";"+str(struct_time[1])+";"+str(struct_time[0])
        hour = str(struct_time[3])+";"+str(struct_time[4])
        #print(struct_time)
        total_memory = os.popen("free | grep \"Mem\" | awk '{ print $2}'").read().replace("\n","").replace(" ","")
        used_memory = os.popen("free | grep \"Mem\" | awk '{ print $3}'").read().replace("\n","").replace(" ","")
        memory_porcent = "0"
        try:
            memory_porcent = str(int((float(used_memory)*100) / float(total_memory)))
        except Exception as e:
            memory_porcent = "0"

        print("\n-------- reporte general --------\n")
        print("Fecha         : ",date)
        print("Hora          : ",hour)
        print("Minutos       : ",minutos)
        print("Memoria total : ",total_memory)
        print("Memoria usada : ",used_memory)
        print("Nivel memoria : ",memory_porcent,"%")
        print("\n--------------------------------\n")
        conectados = dispositivos.BusquedaPorRango(20,50)
        velocidad = speed.obtenerVelocidad()
        salida = str(date) + ";" + str(hour) + ";" + str(minutos) +";"+ str(total_memory) + ";" + str(used_memory) +";"+str(memory_porcent)+";"+conectados+";"+velocidad
        file = self.__ruta_uso+ self.__save_folder + self.__file_name
        archivo_salida = open(file,"a")
        archivo_salida.write(salida)
        archivo_salida.write("\n")
        archivo_salida.close()


    def obtenerRuta(self):
        return self.__ruta_uso;


    def obtenerDirectorioSalida(self):
        return  "mkdir " + self.__ruta_uso + self.__save_folder + " 2>/dev/null"



    def crearDirectorioAlmacen(self):
        # creación del directorio de salida y almacen
        new_dir = "mkdir " + self.__ruta_uso + self.__save_folder + " 2>/dev/null"
        os.system(new_dir)
        #print(new_dir)




manager  = RecolectorInformacion()
manager.crearDirectorioAlmacen()
manager.generarRegistro(1)
