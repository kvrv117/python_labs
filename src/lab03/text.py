import testing
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

def main() -> None:
    print('===NORMALIZE===')
    norm_tests = [
        "ПрИвЕт\nМИр\t",
        "ёжик, Ёлка",
        "Hello\r\nWorld",
        "  двойные   пробелы  "
    ]

    testing.test(normalize, norm_tests, True)
    print()

    print('===TOKENIZE===')
    token_tests = [
        "привет, мир!",
        "hello,world!!!",
        "по-настоящему круто",
        "2025 год",
        "emoji 😀 не слово"
    ]

    testing.test(tokenize, token_tests)
    print()

    print('===FREQ TOPN===')
    freq_tests = [
        ["a", "b", "a", "c", "b", "a"],
        ["bb", "aa", "bb", "aa", "cc"]
    ]

    for t in freq_tests:
        freq = count_freq(t)
        topn = top_n(freq, n = 2)
        start = f'{t} -> '
        print(start + f'freq = {freq}')
        topn = f'top_n = {topn}'
        print(f'{topn: >{len(start) + len(topn)}}')

if __name__ == "__main__":
    main()