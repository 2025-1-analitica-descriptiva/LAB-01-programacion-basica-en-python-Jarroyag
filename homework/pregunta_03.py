"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    with open("files/input/data.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter="\t")
        contador = {}
        for row in reader:
            letra = row[0]
            valor = int(row[1])
            if letra in contador:
                contador[letra] += valor
            else:
                contador[letra] = valor
    return sorted(contador.items())
print(pregunta_03())