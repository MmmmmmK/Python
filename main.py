from typing import List, Union, Any, Tuple

def inputException(Exception):
    '''Класс обработки количества введенных данных'''
    def __init__(self):
        super.__init__(self)

rows : List[Tuple[Any]] = [(1, 'Peter', 'Johnson', 'Alexandrovich', '17.09.2000'), (2, 'Mark', 'Colinson', 'Petrovich', '17.09.2001')]
columns = ['ID', 'Name', 'Last', 'Patronymic', 'BD']


def writeTable(columns : Union[List[Any], Tuple[Any]], rows : Union[List[Union[List[Any], Tuple[Any]]], Tuple[Union[List[Any], Tuple[Any]]]]) -> str:
    """Вырисовывание таблицы"""
    answer = ''
    rows_as_str = []
    lens = list(map(len, columns))
    for row in rows:
        try:
            if len(columns) != len(row):
                raise inputException('Введено неверное количество данных! Введите имя, фамилию, отчество, год рождения:')
        except inputException as ex:
            print(ex, end=' ')
            rows[rows.index(row)] = input().split()
            rows[rows.index(row)].insert(0, rows.index(row) + 1)  # чтоб пользователь не писал лишнее
        for num, data in enumerate(row):
            if len(str(data)) > lens[num]:
                lens[num] = len(str(data))
        rows_as_str.append(tuple(map(str, rows[rows.index(row)])))
    drawRaw1 = '|{0[0]!s:>{1[0]}}|{0[1]!s:>{1[1]}}|{0[2]!s:>{1[2]}}|{0[3]!s:>{1[3]}}|{0[4]!s:>{1[4]}}|\n'.format(columns, lens)
    for value in rows_as_str:
        answer += '|'.join(value) + '|\n'
    line = '_' * (sum(lens) + len(columns) + 1) + '\n'
    return line + drawRaw1 + answer + line


print(writeTable(columns, rows))
