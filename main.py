from typing import List, Union, Any, Tuple

line = '_' * 14
rows = []
columns: Tuple[str] = tuple(input('Введите элементы-заголовки: ').split())
rows : List[Tuple[Any]] = tuple(input('Введите элементы-данные строк: ').split())


def write_table(columns: Union[List[Any], Tuple[Any]], rows : Union[List[Union[List[Any], Tuple[Any]]], Tuple[Union[List[Any], Tuple[Any]]]], valuesOfTable : str) -> str:
    """Вырисовывание таблицы"""
    for sequence in range(rows):
        answer += ('|{:> 4d}|{:>7s}|\n'.format(sequence + 1, valuesOfTable))
    return line + answer + line


print(writeTable(columns, rows))
