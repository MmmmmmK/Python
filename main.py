from typing import List, Union, Any, Tuple

data: List[str] = ['Tom', 'Peter', 'Vasyl', 'Kola']
line = '_' * 14
rows = int(input('Введите количество элементов: '))


def write_table(rows : Union[List[Union[List[Any], Tuple[Any]]], Tuple[Union[List[Any], Tuple[Any]]]], valuesOfTable : str) -> str:
    """Вырисовывание таблицы"""
    answer = ' '
    for sequence in range(rows):
        answer += ('|{:> 4d}|{:>7s}|\n'.format(sequence + 1, valuesOfTable))
    return line + answer + line


print(writeTable(rows, data))
