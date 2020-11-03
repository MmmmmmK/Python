from typing import List, Union, Any, Tuple

line = '_' * 14 + '\n'
columns: List[str] = []
rows : List[Tuple[Any]] = [(1, 'Peter', 'Johnson', 'Alexandrovich', '17.09.2000'), (2, 'Mark', 'Colinson', 'Petrovich', '17.09.2001')]


def writeTable(columns: Union[List[Any], Tuple[Any]], rows : Union[List[Union[List[Any], Tuple[Any]]], Tuple[Union[List[Any], Tuple[Any]]]]) -> str:
    """Вырисовывание таблицы"""
    drawRaw1 = ('|{columns[0]!s:>4}|{columns[1]!s:>15}|{columns[2]!s:>15}|{columns[3]!s:>15}|{columns[4]!s:>15}'.format(columns=['ID', 'Name', 'Last', 'Patronymic', 'BD']))
    answer = ''
    for sequence, value in enumerate(rows):
        answer += '|{value[sequence][0]:>4d}|{value[sequence][1]:>15s}|{value[sequence][2]:>15s}|{value[sequence][3]:>15s}|{value[sequence][4]:>15s}|\n'.format(value)
    return line + drawRaw1 + answer + line


print(writeTable(columns, rows))
