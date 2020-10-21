# class Exception(Exception):
#     def __init__(self):
from typing import List, Union

data: List[str] = ['Tom', 'Peter', 'Vasyl', 'Kola']
line = '_' * 14

def write_table(columns: Union[List[Any], Tuple[Any]], rows:Union[List[Union[List[Any], Tuple[Any]]], Tuple[Union[List[Any], Tuple[Any]]]]) -> None:
    """Вырисовывание таблицы"""
    print(line)
    for sequence, names in enumerate(valuesOfTable):
        print('|{:> 4d}|{:>7s}|'.format(sequence, names))
    print(line)

writeTable(data)
