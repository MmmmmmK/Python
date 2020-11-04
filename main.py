from typing import List, Union, Any, Tuple

line = '_' * 64 + '\n'
rows : List[Tuple[Any]] = [(1, 'Peter', 'Johnson', 'Alexandrovich', '17.09.2000'), (2, 'Mark', 'Colinson', 'Petrovich', '17.09.2001')]
columns = ['ID', 'Name', 'Last', 'Patronymic', 'BD']

def writeTable(columns : Union[List[Any], Tuple[Any]], rows : Union[List[Union[List[Any], Tuple[Any]]], Tuple[Union[List[Any], Tuple[Any]]]]) -> str:
    """Вырисовывание таблицы"""
    drawRaw1 = '|{0[0]!s:>4}|{0[1]!s:>15}|{0[2]!s:>15}|{0[3]!s:>15}|{0[4]!s:>15}|\n'.format(columns)
    answer = ''
    for sequence, value in enumerate(rows):
        answer += '|{1[{0}][0]:>4d}|{1[{0}][1]:>15s}|{1[{0}][2]:>15s}|{1[{0}][3]:>15s}|{1[{0}][4]:>15s}|\n'.format(sequence, value)
    return line + drawRaw1 + answer + line


print(writeTable(columns, rows))
