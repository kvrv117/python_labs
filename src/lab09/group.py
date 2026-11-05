import csv
import collections
from pathlib import Path
from src.lab08.models import STUDENT_FIELDS, student_from_dict, validate_student
from src.lab08.models import update_student as mdls_update

HEADER = STUDENT_FIELDS


def ensure_storage(path):
    """Если файла нет, создает его с одной строкой-заголовком. Создает каталоги."""
    path = Path(path)
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, mode="w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(HEADER)


def load_students(path) -> list[dict]:
    """Читает все записи из CSV. Отсутствие заголовка или лишние колонки - ValueError."""
    ensure_storage(path)
    students = []
    
    with open(path, mode="r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        
        if reader.fieldnames is None or set(reader.fieldnames) != set(HEADER):
            raise ValueError("Некорректная структура заголовков CSV-файла.")
            
        for row in reader:
            try:
                student = student_from_dict(row)
                validate_student(student)
                students.append(student)
            except (KeyError, ValueError, TypeError) as e:
                raise ValueError(f"Ошибка валидации данных в строке CSV: {e}")
                
    return students


def save_students(path, students):
    """Перезаписывает файл целиком корректными данными."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=HEADER)
        writer.writeheader()
        for student in students:
            writer.writerow(student)


def add_student(path, student: dict):
    """Валидирует запись и дописывает в конец. Запрет дубликатов"""
    
    validate_student(student)
        
    students = load_students(path)
    
    if any(s["fio"].lower() == student["fio"].lower() for s in students):
        raise ValueError(f"Студент с ФИО '{student['fio']}' уже существует в базе данных.")
        
    students.append(student)
    save_students(path, students)


def list_students(path, sort_by=None) -> list[dict]:
    students = load_students(path)
    if sort_by is None:
        return students
        
    if sort_by not in ("fio", "gpa"):
        raise ValueError("Недопустимый параметр сортировки. Используйте 'fio' или 'gpa'.")
        
    return sorted(students, key=lambda x: x[sort_by])


def find_students(path, substr: str) -> list[dict]:
    """Поиск по подстроке в ФИО без учета регистра."""
    students = load_students(path)
    substr_lower = substr.lower()
    return [s for s in students if substr_lower in s["fio"].lower()]


def remove_student(path, fio: str) -> int:
    """Удаляет ВСЕ записи с таким fio, возвращает количество удаленных."""
    students = load_students(path)
    initial_count = len(students)
    
    students = [s for s in students if s["fio"].lower() != fio.lower()]
    
    removed_count = initial_count - len(students)
    if removed_count > 0:
        save_students(path, students)
        
    return removed_count


def update_student(path, fio: str, **fields) -> bool:
    """Обновляет поля ПЕРВОЙ записи с таким fio. Результат валидируется."""
    students = load_students(path)
    
    for key in fields:
        if key not in HEADER:
            raise KeyError(f"Неизвестное поле для обновления: {key}")
            
    for i, student in enumerate(students):
        if student["fio"].lower() == fio.lower():
            updated = mdls_update(student, fields=fields)
            students[i] = updated
            save_students(path, students)
            return True
            
    return False


def stats(path) -> dict:
    """Собирает расширенную аналитику по студентам."""
    students = load_students(path)
    if not students:
        return { "count": 0, "min_gpa": 0.0, "max_gpa": 0.0, "avg_gpa": 0.0, "groups": {}, "top_5_students": [] }
        
    gpas = [s["gpa"] for s in students]
    groups_counts = collections.Counter([s["group"] for s in students])
    
    sorted_by_gpa = sorted(students, key=lambda x: x["gpa"], reverse=True)
    top_5 = [{"fio": s["fio"], "gpa": s["gpa"]} for s in sorted_by_gpa[:5]]
    
    return {
        "count": len(students),
        "min_gpa": min(gpas),
        "max_gpa": max(gpas),
        "avg_gpa": round(sum(gpas) / len(students), 2),
        "groups": dict(groups_counts),
        "top_5_students": top_5
    }