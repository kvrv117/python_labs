import csv
from pathlib import Path

from src.lab04.io_txt_csv import ensure_parent_dir
from openpyxl import Workbook


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """Конвертирует CSV в XLSX, задавая ширину столбцов по содержимому."""
    source = Path(csv_path)
    target = Path(xlsx_path)
    ensure_parent_dir(target)

    if source.suffix.lower() != ".csv":
        raise ValueError(f"Ожидался CSV-файл: {source}")
    if target.suffix.lower() != ".xlsx":
        raise ValueError(f"Ожидался XLSX-файл: {target}")

    with source.open("r", newline="", encoding="utf-8") as file:
        sample = file.read(1024)
        file.seek(0)
        if not sample.strip():
            raise ValueError("CSV пустой")
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=",;")
        except csv.Error:
            dialect = csv.excel
        rows = list(csv.reader(file, dialect=dialect))

    if not rows or not rows[0] or not any(cell.strip() for cell in rows[0]):
        raise ValueError("CSV должен содержать заголовок")

    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Sheet1"

    for row in rows:
        worksheet.append(row)

    for column in worksheet.columns:
        max_length = max((len(str(cell.value)) if cell.value is not None else 0) for cell in column)
        worksheet.column_dimensions[column[0].column_letter].width = max(8, max_length)

    workbook.save(target)

def main():
    csv_to_xlsx("data/lab05/samples/cities.csv", "data/lab05/out/cities.xlsx")

if __name__ == "__main__":
    main()