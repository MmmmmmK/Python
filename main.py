# class Exception(Exception):
#     def __init__(self):
from typing import List, Union

data: List[str] = ['Tom', 'Peter', 'Vasyl', 'Kola']

def writeTable(valuesOfTable: List) -> None:
    """Вырисовывание таблицы"""
    print('_____________')
    for sequence, names in enumerate(valuesOfTable):
        print('|{:> 4d}|{:>7s}|'.format(sequence, names))
    print('______________')

writeTable(data)
