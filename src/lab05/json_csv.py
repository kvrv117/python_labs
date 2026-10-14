import csv
import json
from pathlib import Path
from src.lab04.io_txt_csv import ensure_parent_dir, write_csv


def check_ext(path: str | Path, expected: str) -> Path:
    """Проверяет расширение файла и возвращает Path."""
    result = Path(path)
    if result.suffix.lower() != expected:
        raise ValueError(f"Ожидался файл с расширением {expected}: {result}")
    return result


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    source = check_ext(json_path, ".json")
    target = check_ext(csv_path, ".csv")
    ensure_parent_dir(target)

    with source.open("r", encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError as exc:
            raise ValueError("Пустой JSON или некорректный JSON")

    if type(data) != list or not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    if any(type(item) != dict for item in data):
        raise ValueError("JSON должен содержать список словарей")

    fieldnames = []
    seen = set()
    for item in data:
        for key in item:
            if type(key) != str:
                raise ValueError("Ключи JSON-объектов должны быть строками")
            if key not in seen:
                seen.add(key)
                fieldnames.append(key)

    if not fieldnames:
        raise ValueError("В JSON отсутствуют поля для CSV")

    with target.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, extrasaction="raise")
        writer.writeheader()
        for item in data:
            writer.writerow({key: item.get(key, "") for key in fieldnames})



def csv_to_json(csv_path: str, json_path: str) -> None:
    """Преобразует CSV в JSON — список словарей со строковыми значениями."""
    source = check_ext(csv_path, ".csv")
    target = check_ext(json_path, ".json")
    ensure_parent_dir(json_path)

    with source.open("r", newline="", encoding="utf-8") as file:
        sample = file.read(1024)
        file.seek(0)

        if not sample.strip():
            raise ValueError("CSV пустой")
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=",;")
        except csv.Error:
            dialect = csv.excel
        
        reader = csv.DictReader(file, dialect=dialect)
        if not reader.fieldnames:
            raise ValueError("CSV должен содержать заголовок")
        rows = list(reader)

    with target.open("w", newline="", encoding="utf-8") as file:
        json.dump(rows, file, ensure_ascii=False, indent=2)

def main():
    json_to_csv("data/lab05/samples/people.json", "data/lab05/out/people_from_json.csv")

if __name__ == "__main__":
    main()