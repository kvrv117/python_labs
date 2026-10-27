import json
import os
from src.lab08.models import student_to_dict, student_from_dict


def students_to_json(students: list[dict], path: str) -> None:
    """Сохраняет список валидных записей студентов в JSON файл."""

    data_to_save = [student_to_dict(s) for s in students]
    
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data_to_save, f, ensure_ascii=False, indent=2)


def students_from_json(path: str) -> list[dict]:
    """
    Читает JSON-массив студентов из файла, политика ошибок - skip
    """

    if not os.path.exists(path):
        raise FileNotFoundError(f"Файл не найден по пути: {path}")

    with open(path, "r", encoding="utf-8") as f:
        try:
            raw_data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Некорректный формат JSON файла: {e}")

    if not isinstance(raw_data, list):
        raise ValueError("JSON корень должен быть массивом (list).")

    valid_students = []
    skipped_count = 0
    skip_reasons = []

    for index, item in enumerate(raw_data):
        try:
            student = student_from_dict(item)
            valid_students.append(student)
        except Exception as e:
            skipped_count += 1
            skip_reasons.append(f"Запись #{index} пропущена. Причина: {e}")

    if skipped_count > 0:
        print(f"\n[Внимание] При чтении файла {path} было пропущено битых записей: {skipped_count}")
        for reason in skip_reasons:
            print(f" - {reason}")
            
    return valid_students
