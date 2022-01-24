"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.

"""

import re


def read_file():
    data = open(".\data.csv", "r").readlines()
    data = [line.replace("\n", "") for line in data]
    #data = [line.replace("\t", ",") for line in data]
    data = [line.split("\t") for line in data]
    #data = [line.split(",") for line in data]
    return data

def pregunta_01():
    data = read_file()
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    sum=0
    [sum:= sum + int(line[1]) for line in data]
    return sum


def pregunta_02():
    data = read_file()
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    #Obtengo la columina 1
    column_1 = [line[0] for line in data]
    #Cuento por cada elemento unico la cantidad
    diccionario = dict((x,column_1.count(x)) for x in set(column_1))
    #Ordeno diccionario
    diccionario = dict(sorted(diccionario.items(), key=lambda item: item[0]))
    #Convierto a tuplas
    lista = [(k,v) for k,v in diccionario.items()]
    return lista


def pregunta_03():
    data = read_file()
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    #Obtengo la columina 1
    column_1 = [line[0] for line in data]
    diccionario = dict((x,0) for x in set(column_1))
    #sumar en diccionario los valores de la columna 2
    [diccionario.update({line[0]:diccionario.get(line[0],0) + int(line[1])}) for line in data]
    #Ordeno diccionario
    diccionario = dict(sorted(diccionario.items(), key=lambda item: item[0]))
    #Convierto a tuplas
    lista = [(k,v) for k,v in diccionario.items()]
    return lista


def pregunta_04():
    data = read_file()
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    #Obtengo la columina 3, dividimos por signo '-', obtenemos meses
    column_3 = [line[2].split('-')[1] for line in data]
    diccionario = dict((x,column_3.count(x)) for x in set(column_3))
    #Ordeno diccionario
    diccionario = dict(sorted(diccionario.items(), key=lambda item: item[0]))
    #Convierto a tuplas
    lista = [(k,v) for k,v in diccionario.items()]
    return lista


def pregunta_05():
    data = read_file()
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    #Obtengo la columina 1
    column_1 = [line[0] for line in data]
    set_unicos = sorted(set(column_1))
    lista_tupla = []
    for unico in set_unicos:
        temp_lista = [line[1] for line in data if line[0] == unico]
        lista_tupla.append((unico,int(max(temp_lista)),int(min(temp_lista))))
    return lista_tupla


def pregunta_06():
    data = read_file()
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    data = [line[4] for line in data]
    data = [line.split(',') for line in data]
    data = [line for line in data]
    return data


def pregunta_07():
    data = read_file()
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    #Obtengo la columina 2
    column_2 = [line[1] for line in data]
    diccionario = dict((int(x),[]) for x in set(column_2))
    #sumar en diccionario los valores de la columna 2
    [diccionario.update({int(line[1]):diccionario.get(int(line[1]),0) + [line[0]]}) for line in data]
    #Ordeno diccionario
    diccionario = dict(sorted(diccionario.items(), key=lambda item: item[0]))
    #Convierto a tuplas
    lista = [(k,v) for k,v in diccionario.items()]
    return lista


def pregunta_08():
    data = read_file()
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    #Obtengo la columina 2
    column_2 = [line[1] for line in data]
    diccionario = dict((int(x),set()) for x in set(column_2))
    #sumar en diccionario los valores de la columna 2
    [diccionario.update({int(line[1]):diccionario.get(int(line[1]),0).union(set(line[0]))}) for line in data]
    #Ordeno diccionario
    diccionario = dict(sorted(diccionario.items(), key=lambda item: item[0])) #diccionario.update({key:sorted(diccionario.get(key,0))})
    [diccionario.update({key:sorted(diccionario.get(key,0))}) for key in diccionario]
    #Convierto a tuplas
    lista = [(k,v) for k,v in diccionario.items()]
    return lista


def pregunta_09():
    data = read_file()
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    data = [line[4] for line in data]
    data = [re.findall(r"\w{3}",line) for line in data]
    data = [x for line in data for x in line]
    #Cuento por cada elemento unico la cantidad
    diccionario = dict((x,data.count(x)) for x in set(data))
    #Ordeno diccionario
    diccionario = dict(sorted(diccionario.items(), key=lambda item: item[0]))
    return diccionario


def pregunta_10():
    data = read_file()
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    data = [line[:3]+[line[3].split(',')]+[line[4].split(',')] for line in data]
    data = [(line[0],len(line[3]),len(line[4]))for line in data]
    return data


def pregunta_11():
    data = read_file()
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    data_aux = [line[1:2]+[line[3].split(',')] for line in data]
    data_aux_2 = [x for line in data_aux for x in line[1]]
    #Cuento por cada elemento unico la cantidad
    diccionario = dict((x,0) for x in set(data_aux_2))
    [diccionario.update({key:diccionario.get(key,0)+int(line[0])}) for line in data_aux for key in line[1]]
    #Ordeno diccionario
    diccionario = dict(sorted(diccionario.items(), key=lambda item: item[0]))
    return diccionario


def pregunta_12():
    data = read_file()
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    #Obtengo la columina 1
    column_1 = [line[0] for line in data]
    diccionario = dict((x,0) for x in set(column_1))
    data_aux = [[line[0]]+[line[4]] for line in data]
    data_aux = [[line[0]]+[re.findall(r"\d+",line[1])] for line in data_aux]
    data_aux = [[line[0]]+ [int(x)] for line in data_aux for x in line[1]]
    [diccionario.update({line[0]:diccionario.get(line[0],0)+int(line[1])}) for line in data_aux]

    return diccionario
