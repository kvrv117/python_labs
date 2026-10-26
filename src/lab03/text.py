import testing
from text_utils import *

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