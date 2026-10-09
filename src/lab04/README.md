# ЛР4 — Файлы: TXT/CSV и отчёты по текстовой статистике

## Задание А

### Мини-тесты

``` python
txt = read_text('data\\lab04\\input.txt')
print(repr(txt))
write_csv([("word","count"),("test",3)], "data/lab04/check.csv")
```
Консоль:
![](../../images/lab04/img01.png)
Содержимое check.csv:
```
word,count
test,3
```

## Тест-кейсы

### A. Один файл (база)

Вход (data/lab04/input.txt):
```
Привет, мир! Привет!!!
```

Консоль:
![](../../images/lab04/img02.png)

Отчёт (data/lab04/report.csv):
```
word,count
привет,2
мир,1
```

### B. Пустой файл

Вход: пустой файл blank_input.txt

Консоль:
![](../../images/lab04/img03.png)

Отчёт (только заголовок):
```
word,count
```

### C. Кодировка cp1251

Вход (data/lab04/cp1251_input.txt в кодировке cp1251):
```
Привет
```

Консоль:
![](../../images/lab04/img04.png)

Отчёт (data/lab04/report.csv):
```
word,count
привет,1
```

### D★. Несколько файлов (пер‑файл и сводный)

Вход:
a.txt
```
Привет мир
```
b.txt
```
Привет, привет!
```

Консоль:
![](../../images/lab04/img05.png)

Пер-файл отчёт (data/lab04/report_per_file.csv):
```
file,word,count
a.txt,мир,1
a.txt,привет,1
b.txt,привет,2
```

Сводный отчёт (data/lab04/report_total.csv):
```
word,count
привет,3
мир,1
```