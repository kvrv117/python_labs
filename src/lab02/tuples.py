from testing import test

def format_record(rec: tuple[str, str, float]):
    if type(rec) != tuple:
        raise TypeError("Введен не кортеж")
    if len(rec) != 3:
        raise ValueError("Кортеж неправильной длины")
    if type(rec[0]) != str or type(rec[1]) != str or type(rec[2]) != float:
        raise TypeError("Элементы кортежа неправильного типа")
    if rec[1] == '':
        raise ValueError("Пустое имя")
    if rec[2] > 5 or rec[2] < 0:
        raise ValueError("GPA в неправильном диапазоне")

    name_parts = rec[0].strip().split()
    name_str = ''
    if len(name_parts) < 2:
        raise ValueError("Неправильно введено имя")
    if len(name_parts) == 2:
        name_str = f'{name_parts[0].capitalize()} {name_parts[1][0].capitalize()}.'
    else:
        name_str = f'{name_parts[0].capitalize()} {name_parts[1][0].capitalize()}.{name_parts[2][0].capitalize()}.'

    return f'{name_str}, гр. {rec[1]}, GPA {rec[2]:.2f}'

tests = [
    ("Иванов Иван Иванович", "BIVT-25", 4.6),
    ("Петров Пётр", "IKBO-12", 5.0),
    ("Петров Пётр Петрович", "IKBO-12", 5.0),
    ("  сидорова  анна   сергеевна ", "ABB-01", 3.999),
    (1, 2, 3),
]

test(format_record, tests)