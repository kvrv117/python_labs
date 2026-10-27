from datetime import date

STUDENT_FIELDS = ("fio", "birthdate", "group", "gpa")


def make_student(fio: str, birthdate: str, group: str, gpa: float) -> dict:
    """Собирает запись студента, предварительно проверив каждое поле."""
    if not isinstance(fio, str) or not isinstance(group, str):
        raise ValueError("Поля 'fio' и 'group' должны быть строками.")
    
    fio_clean = fio.strip()
    group_clean = group.strip()

    if not fio_clean:
        raise ValueError("ФИО не может быть пустой строкой.")
    if not group_clean:
        raise ValueError("Группа не может быть пустой строкой.")

    if not isinstance(birthdate, str):
        raise ValueError("Поле 'birthdate' должно быть строкой в формате YYYY-MM-DD.")
    try:
        b_date = date.fromisoformat(birthdate)
    except ValueError:
        raise ValueError(f"Некорректный формат или значение даты: '{birthdate}'. Ожидается YYYY-MM-DD.")
    
    if b_date > date.today():
        raise ValueError(f"Дата рождения не может быть в будущем: '{birthdate}'.")

    if not isinstance(gpa, (int, float)):
        raise ValueError("GPA должен быть числом (int или float).")
    
    gpa_float = float(gpa)
    if not (0.0 <= gpa_float <= 5.0):
        raise ValueError(f"Средний балл (gpa) должен быть в диапазоне от 0 до 5. Получено: {gpa_float}.")

    return {
        "fio": fio_clean,
        "birthdate": birthdate,
        "group": group_clean,
        "gpa": gpa_float
    }


def validate_student(rec: dict) -> None:
    """Проверяет готовый словарь на соответствие структуре и валидность данных."""
    if not isinstance(rec, dict):
        raise ValueError("Запись должна быть словарем.")
    
    if set(rec.keys()) != set(STUDENT_FIELDS):
        raise ValueError(f"Неверный набор ключей. Ожидается: {STUDENT_FIELDS}, получено: {tuple(rec.keys())}.")

    make_student(rec["fio"], rec["birthdate"], rec["group"], rec["gpa"])


def student_age(rec: dict, today: date = None) -> int:
    """Возвращает количество полных лет студента на дату today."""
    validate_student(rec)
    b_date = date.fromisoformat(rec["birthdate"])
    today = today or date.today()
    
    age = today.year - b_date.year
    if (today.month, today.day) < (b_date.month, b_date.day):
        age -= 1
    return age


def format_student(rec: dict) -> str:
    """Возвращает красивую строку с данными студента и инициалами."""
    validate_student(rec)
    
    parts = rec["fio"].split()
    if len(parts) >= 3:
        fio_formatted = f"{parts[0]} {parts[1][0]}.{parts[2][0]}."
    elif len(parts) == 2:
        fio_formatted = f"{parts[0]} {parts[1][0]}."
    else:
        fio_formatted = rec["fio"]

    age = student_age(rec)
    
    if 11 <= age % 100 <= 19:
        age_word = "лет"
    elif age % 10 == 1:
        age_word = "год"
    elif age % 10 in (2, 3, 4):
        age_word = "года"
    else:
        age_word = "лет"

    return f"{fio_formatted} ({rec['group']}), {age} {age_word}, GPA {rec['gpa']:.2f}"


def student_to_dict(rec: dict) -> dict:
    """Возвращает чистую глубокую копию записи для сериализации."""
    validate_student(rec)
    return {
        "fio": rec["fio"],
        "birthdate": rec["birthdate"],
        "group": rec["group"],
        "gpa": rec["gpa"]
    }


def student_from_dict(d: dict) -> dict:
    """Десериализует словарь, извлекая только нужные ключи и валидируя их."""
    if not isinstance(d, dict):
        raise ValueError("Входные данные для десериализации должны быть словарем.")
    
    try:
        rec = make_student(fio=d.get("fio"), birthdate=d.get("birthdate"), group=d.get("group"), gpa=d.get("gpa"))
        validate_student(rec)
        return rec
    except Exception as e:
        raise ValueError(f"Ошибка валидации полей: {e}")


def update_student(rec: dict, **fields) -> dict:
    """Возвращает новую запись с изменёнными полями без мутации старой."""
    validate_student(rec)

    new_data = student_to_dict(rec)
    
    for key, val in fields.items():
        if key not in STUDENT_FIELDS:
            raise KeyError(f"Попытка обновить несуществующее поле '{key}'.")
        new_data[key] = val

    validate_student(new_data)
    return new_data
