from typing import List, Union, Any, Tuple

def inputException(Exception):
    '''Класс обработки количества введенных данных'''
    def __init__(self, waiting, fact):
        Exception.__init__(self)
        self.waiting = waiting
        self.fact = fact

rows : List[Tuple[Any]] = [(1, 'Peter', 'Johnson', 'Alexandrovich', '17.09.2000'), (2, 'Mark', 'Colinson', 'Petrovich', '17.09.2001')]
columns = ['ID', 'Name', 'Last', 'Patronymic', 'BD']


def writeTable(columns : Union[List[Any], Tuple[Any]], rows : Union[List[Union[List[Any], Tuple[Any]]], Tuple[Union[List[Any], Tuple[Any]]]]) -> str:
    """Вырисовывание таблицы"""
    answer = ''
    rows_as_str = []
    lens = list(map(len, columns))
    for row in rows:
        rows_as_str.append(tuple(map(str, row)))
        try:
            if len(columns) != len(row):
                raise inputException(len(columns), len(row))
        except inputException as ex:
            print('Вы ввели {0}, а нужно {1}! Введите имя, фамилию, отчество, год рождения:'.format(ex.fact, ex.waiting), end=' ')
            rows[rows.index(row)] = input().split()
            rows[rows.index(row)].insert(0, rows.index(row) + 1)  # чтоб пользователь не писал лишнее
        for num, data in enumerate(row):
            if len(str(data)) > lens[num]:
                lens[num] = len(str(data))
    drawRaw1 = '|{0[0]!s:>{1[0]}}|{0[1]!s:>{1[1]}}|{0[2]!s:>{1[2]}}|{0[3]!s:>{1[3]}}|{0[4]!s:>{1[4]}}|\n'.format(columns, lens)
    for value in rows_as_str:
        answer += '|{0}|{1}|{2}|{3}|{4}|\n'.format(*value)
    line = '_' + (lambda lens: lens[0] + lens[1] + lens[2] + lens[3] + lens[4] + 6) + '\n'
    return line + drawRaw1 + answer + line


print(writeTable(columns, rows))
