# src/lab09/__init__.py

from src.lab09.group import (
    ensure_storage,
    load_students,
    save_students,
    add_student,
    list_students,
    find_students,
    remove_student,
    update_student,
    stats,
)

__all__ = [
    "ensure_storage",
    "load_students",
    "save_students",
    "add_student",
    "list_students",
    "find_students",
    "remove_student",
    "update_student",
    "stats",
]
