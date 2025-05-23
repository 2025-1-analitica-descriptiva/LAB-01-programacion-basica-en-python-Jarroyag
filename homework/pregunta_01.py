"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv



def pregunta_01():
    """
    
    Retorne la suma de la segunda columna.


    Rta/
    214

    """
   
    
    with open("files/input/data.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter="\t")
        contador = 0
        for row in reader:
             contador += int(row[1])
             print(row[1])
    return contador
           
       
    

print(pregunta_01())


    
 
  
  