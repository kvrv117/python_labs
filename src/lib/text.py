import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """
    Нормализация строки.
    При casefold = True использует s.casefold() иначе s.lower()
    При yo2e = True заменяет Ё на Е
    """
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")

    text = re.sub(r"\s+", " ", text).strip()

    return text


def tokenize(text: str) -> list[str]:
    """
    Разбивает строку на слова.
    """

    return re.findall(r"\w+(?:-\w+)*", text, flags=re.UNICODE)


def count_freq(tokens: list[str]) -> dict[str, int]:
    """
    Считает частоты каждого токена
    """

    freq  = {}

    for token in tokens:
        freq[token] = freq.get(token, 0) + 1

    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """
    Возвращает топ-n самых встречающихся слов в алфавитном порядке
    """

    if n <= 0:
        return []

    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))[:n]