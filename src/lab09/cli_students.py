import sys
import argparse
from src.lab08.models import format_student
from src.lab09.group import add_student, list_students, find_students, remove_student, update_student, stats

def main():
    path = "data/lab09/students.csv"

    parser = argparse.ArgumentParser(description="CLI утилита для управления базой данных студентов на CSV.")
    
    subparsers = parser.add_subparsers(dest="command", required=True, help="Доступные команды")
    
    parser_add = subparsers.add_parser("add", help="Добавить нового студента")
    parser_add.add_argument("--fio", required=True, help="ФИО студента")
    parser_add.add_argument("--birthdate", required=True, help="Дата рождения (ГГГГ-ММ-ДД)")
    parser_add.add_argument("--group", required=True, help="Учебная группа")
    parser_add.add_argument("--gpa", required=True, type=float, help="Средний балл (GPA)")
    
    parser_list = subparsers.add_parser("list", help="Вывести список студентов")
    parser_list.add_argument("--sort", choices=["fio", "gpa"], help="Сортировка по полю")
    
    parser_find = subparsers.add_parser("find", help="Поиск студента по ФИО")
    parser_find.add_argument("--q", required=True, help="Подстрока для поиска в ФИО")
    
    parser_remove = subparsers.add_parser("remove", help="Удалить студента по ФИО")
    parser_remove.add_argument("--fio", required=True, help="Точное ФИО студента для удаления")
    
    parser_update = subparsers.add_parser("update", help="Обновить данные существующего студента")
    parser_update.add_argument("--fio", required=True, help="ФИО студента, которого нужно обновить")
    parser_update.add_argument("--birthdate", help="Новая дата рождения")
    parser_update.add_argument("--group", help="Новая учебная группа")
    parser_update.add_argument("--gpa", type=float, help="Новый средний балл (GPA)")
    
    subparsers.add_parser("stats", help="Показать расширенную аналитику и статистику по базе данных")

    args = parser.parse_args()

    try:
        if args.command == "add":
            new_student = {
                "fio": args.fio,
                "birthdate": args.birthdate,
                "group": args.group,
                "gpa": args.gpa
            }
            add_student(path, new_student)
            print("Успешно: Студент добавлен.")
            
        elif args.command == "list":
            students = list_students(path, sort_by=args.sort)
            if not students:
                print("База данных пуста.")
            for s in students:
                print(format_student(s))
                
        elif args.command == "find":
            students = find_students(path, args.q)
            if not students:
                print("Студенты не найдены.")
            for s in students:
                print(format_student(s))
                
        elif args.command == "remove":
            deleted = remove_student(path, args.fio)
            print(f"Успешно: Удалено записей: {deleted}")
            
        elif args.command == "update":
            update_fields = {}
            if args.birthdate is not None:
                update_fields["birthdate"] = args.birthdate
            if args.group is not None:
                update_fields["group"] = args.group
            if args.gpa is not None:
                update_fields["gpa"] = args.gpa
                
            if not update_fields:
                raise ValueError("Предупреждение: Не переданы поля для обновления.")
                
            found = update_student(path, args.fio, **update_fields)
            if found:
                print("Успешно: Данные студента обновлены.")
            else:
                raise ValueError(f"Ошибка: Студент с ФИО '{args.fio}' не найден.")
                
        elif args.command == "stats":
            data = stats(path)
            print(f"Общее количество студентов: {data['count']}")
            print(f"GPA (Мин / Макс / Средний): {data['min_gpa']} / {data['max_gpa']} / {data['avg_gpa']}")
            print("Распределение по группам:")
            for grp, cnt in data['groups'].items():
                print(f"  - {grp}: {cnt} чел.")
            print("Топ-5 студентов по успеваемости:")
            for i, s in enumerate(data['top_5_students'], 1):
                print(f"  {i}. {s['fio']} — GPA: {s['gpa']}")

    except (ValueError, KeyError, TypeError) as err:
        print(f"Ошибка выполнения команды: {err}", file=sys.stderr)


if __name__ == "__main__":
    main()
