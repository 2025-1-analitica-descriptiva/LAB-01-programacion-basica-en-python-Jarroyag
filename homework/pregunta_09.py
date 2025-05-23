"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    contador = {}
    with open("files/input/data.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter="\t")
        for row in reader:
            claves = row[4].split(",")
            for par in claves:
                clave = par.split(":")[0]
                if clave in contador:
                    contador[clave] += 1
                else:
                    contador[clave] = 1
    return dict(sorted(contador.items()))

print(pregunta_09())