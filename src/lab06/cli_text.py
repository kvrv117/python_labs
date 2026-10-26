import argparse
import sys
from pathlib import Path
from src.lab03.text_stats import print_stats
from src.lab03.text import tokenize, normalize

def cat(input_path : str, n : bool) -> None:
    p = Path(input_path)
    lines = []

    try:
        with open(p, 'r', encoding='utf-8') as file:
            lines = file.readlines();
    except FileNotFoundError:
        print(f"Ошибка: файл не найден: {p}", file=sys.stderr)
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Ошибка: не удалось прочитать файл {p} в кодировке UTF-8", file=sys.stderr)
        sys.exit(1)

    for i in range(len(lines)):
        if n:
            print(f'{i + 1}.{lines[i]}', end='')
        else:
            print(lines[i], end='')

def stats(input_path : str, top : int) -> None:
    p = Path(input_path)

    try:
        with open(p, 'r', encoding='utf-8') as file:
            print_stats(tokenize(normalize(file.read())), n=top)
    except FileNotFoundError:
            print(f"Ошибка: файл не найден: {p}", file=sys.stderr)
            sys.exit(1)
    except UnicodeDecodeError:
        print(f"Ошибка: не удалось прочитать файл {p} в кодировке UTF-8", file=sys.stderr)
        sys.exit(1)

def main() -> None:
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()
    
    if args.command == "cat":
        cat(args.input, args.n)
    elif args.command == "stats":
        if args.top <= 0:
            parser.error("--top должен быть положительным числом")
        stats(args.input, args.top)

if __name__ == "__main__":
    main()