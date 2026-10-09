import argparse
from collections import Counter
from pathlib import Path

from text_utils import normalize, tokenize
from src.lab04.io_txt_csv import read_text, write_csv
from src.lab03.text_stats import print_stats


def frequencies_from_text(text: str) -> dict[str, int]:
    """
    Нормализует текст, разбивает его на токены
    и возвращает частоты слов.
    """
    tokens = tokenize(normalize(text))
    return dict(Counter(tokens))


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    """
    Возвращает пары (слово, количество),
    отсортированные по количеству по убыванию,
    а при равенстве — по слову по возрастанию.
    """
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))


def make_total_report(input_files: list[str], output_file: str, encoding: str) -> None:
    """
    Создаёт общий CSV-отчёт по всем входным файлам.
    """
    total_freq: Counter[str] = Counter()

    for path in input_files:
        text = read_text(path, encoding)
        total_freq.update(tokenize(normalize(text)))

    rows = sorted_word_counts(dict(total_freq))

    write_csv(rows, output_file, header=("word", "count"))


def make_per_file_report(input_files: list[str], output_file: str, encoding: str) -> None:
    """
    Создаёт CSV-отчёт с частотами слов отдельно для каждого файла.
    """
    rows = []

    for path in input_files:
        text = read_text(path, encoding)
        freq = frequencies_from_text(text)
        name = Path(path).name

        for word, count in sorted_word_counts(freq):
            rows.append((name, word, count))

    rows.sort(key=lambda row: (row[0], -row[2], row[1]))

    write_csv(rows, output_file, header=("file", "word", "count"))


def print_summary(text: str) -> None:
    """
    Печатает краткую статистику текста в консоль.
    """
    tokens = tokenize(normalize(text))
    print_stats(tokens)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Генерация отчёта по частотности слов."
    )

    parser.add_argument(
        "--in",
        dest="input_files",
        nargs="+",
        default=["data/lab04/input.txt"],
        help="Пути к входным TXT-файлам."
    )

    parser.add_argument(
        "--out",
        default="data/lab04/report.csv",
        help="Путь к общему CSV-отчёту."
    )

    parser.add_argument(
        "--encoding",
        default="utf-8",
        help="Кодировка входных файлов. По умолчанию UTF-8."
    )

    parser.add_argument(
        "--per-file",
        default=None,
        help="Путь к отчёту по каждому файлу отдельно."
    )

    parser.add_argument(
        "--total",
        default=None,
        help="Путь к сводному отчёту."
    )

    args = parser.parse_args()

    if args.per_file is not None or args.total is not None:
        per_file_path = args.per_file or "data/lab04/report_per_file.csv"
        total_path = args.total or "data/lab04/report_total.csv"

        make_per_file_report(args.input_files, per_file_path, args.encoding)

        make_total_report(args.input_files, total_path, args.encoding)

        print(f"Отчёт по файлам сохранён: {per_file_path}")
        print(f"Сводный отчёт сохранён: {total_path}")

        return

    # Базовый режим — один файл
    if len(args.input_files) != 1:
        parser.error(
            "Для нескольких файлов используйте --per-file и/или --total."
        )

    input_path = args.input_files[0]

    text = read_text(input_path, args.encoding)
    freq = frequencies_from_text(text)

    rows = sorted_word_counts(freq)

    write_csv(rows, args.out, header=("word", "count"))

    print_summary(text)
    print(f"Отчёт сохранён: {args.out}")


if __name__ == "__main__":
    main()