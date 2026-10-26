import argparse
import sys
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

def main() -> None:
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    j2c_parser = subparsers.add_parser("json2csv", help="Преобразует .json в .csv")
    j2c_parser.add_argument("--in", dest="input", required=True, help="Входной .json файл")
    j2c_parser.add_argument("--out", dest="output", required=True, help="Выходной .csv файл")

    c2j_parser = subparsers.add_parser("csv2json", help="Преобразует .csv в .json")
    c2j_parser.add_argument("--in", dest="input", required=True, help="Входной .csv файл")
    c2j_parser.add_argument("--out", dest="output", required=True, help="Выходной .json файл")

    c2x_parser = subparsers.add_parser("csv2xlsx", help="Преобразует .csv в .xlsx")
    c2x_parser.add_argument("--in", dest="input", required=True, help="Входной .csv файл")
    c2x_parser.add_argument("--out", dest="output", required=True, help="Выходной .xlsx файл")

    args = parser.parse_args()
    
    if args.command == "json2csv":
        json_to_csv(args.input, args.output)
    elif args.command == "csv2json":
        csv_to_json(args.input, args.output)
    elif args.command == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)

if __name__ == "__main__":
    main()