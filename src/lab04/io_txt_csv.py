from pathlib import Path
import csv


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Читает текстовый файл целиком и возвращает его содержимое одной строкой.

    По умолчанию используется кодировка UTF-8.
    Для другой кодировки можно передать её явно, например:
    read_text("data/input.txt", encoding="cp1251").

    Если файл не существует, возникает FileNotFoundError.
    Если кодировка не подходит, возникает UnicodeDecodeError.
    """
    p = Path(path)
    return p.read_text(encoding=encoding)


def ensure_parent_dir(path: str | Path):
    """
    Создаёт родительские директории для указанного пути,
    если они ещё не существуют.
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None):
    """
    Записывает строки в CSV-файл.

    Если передан header, он записывается первой строкой.
    Все строки должны иметь одинаковую длину, иначе возникает ValueError.
    """
    if rows:
        expected_length = len(rows[0])

        for row in rows:
            if len(row) != expected_length:
                raise ValueError("Все строки CSV должны иметь одинаковую длину.")

        if header is not None and len(header) != expected_length:
            raise ValueError("Длина заголовка не совпадает с длиной строк.")

    elif header is not None:
        expected_length = len(header)
    else:
        expected_length = None

    p = Path(path)
    ensure_parent_dir(path)

    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if header is not None:
            writer.writerow(header)

        for row in rows:
            writer.writerow(row)

if __name__ == 'main':
    txt = read_text('data\\lab04\\input.txt')
    print(repr(txt))
    write_csv([("word","count"),("test",3)], "data/lab04/check.csv")