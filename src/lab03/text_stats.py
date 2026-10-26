import sys
from text_utils import *

def print_stats(tokens: list[str], is_table: bool = True) -> None:
    freq = count_freq(tokens)
    top = top_n(freq, 5)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")

    if not top:
        return

    word_width = max(len(word) for word, _ in top)

    if is_table:
        print(f"{'слово':<{word_width}} | частота")
        print("-" * (word_width + 10))

        for word, count in top:
            print(f"{word:<{word_width}} | {count}")
    else:
        for word, count in top:
                    print(f"{word}:{count}")


def main():
    sys.stdin.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')
    text = sys.stdin.read()

    normalized = normalize(text)
    tokens = tokenize(normalized)

    print_stats(tokens, True)


if __name__ == "__main__":
    main()