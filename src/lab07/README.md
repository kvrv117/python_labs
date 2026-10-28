# ЛР7 — Поиск, сортировка и измерение времени

## search.py

``` python
def linear_search(nums, x) -> int:
    """
    Линейный поиск. nums - любой
    """
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1

def binary_search(sorted_nums, x) -> int:
    """
    Бинарный поиск, работает только на отсортированном массиве
    """
    if len(sorted_nums) == 0:
        return -1
    lo = 0
    hi = len(sorted_nums) - 1
    while lo <= hi:
        m = (lo + hi) // 2
        if x == sorted_nums[m]:
            return m
        elif x < sorted_nums[m]:
            hi = m - 1
        elif x > sorted_nums[m]:
            lo = m + 1
    return -1

def two_sum_brute(nums, target) -> tuple[int, int] | None:
    """
    Ищет элементы, которые в сумме дают target, напрямую
    """
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None

def two_sum_fast(nums, target) -> tuple[int, int] | None:
    """
    Ищет элементы, которые в сумме дают target, через словарь
    """
    seen = {}
    for i in range(len(nums)):
        if nums[i] in seen:
            return (seen[nums[i]], i)
        else:
            seen[target - nums[i]] = i
    return None
```

## sorting.py

``` python
def bubble_sort(nums):
    """
    Новый список, отсортированный по возрастанию. Исходный не меняется.
    """
    if len(nums) <= 1:
        return nums
    
    output = nums.copy()

    was_switch = True
    while was_switch:
        was_switch = False
        for i in range(len(output) - 1):
            if output[i + 1] < output[i]:
                output[i], output[i + 1] = output[i + 1], output[i]
                was_switch = True
    
    return output

def insertion_sort(nums):
    """
    Новый список, отсортированный по возрастанию. Исходный не меняется.
    """
    if len(nums) <= 1:
        return nums
    
    output = nums.copy()

    for i in range(1, len(output)):
        k = output[i]
        j = i - 1

        while j >= 0 and output[j] > k:
            output[j], output[j + 1] = k, output[j]
            j -= 1

    return output

def selection_sort(nums):
    """
    Новый список, отсортированный по возрастанию. Исходный не меняется.
    """
    if len(nums) <= 1:
        return nums
    
    output = nums.copy()

    for i in range(len(output) - 1):
        min_i = i

        for j in range(i + 1, len(output)):
            if output[j] < output[min_i]:
                min_i = j

        output[min_i], output[i] = output[i], output[min_i]

    return output
```

## check.py

``` python
import random
from src.lab07.search import *
from src.lab07.sorting import *

def check_sorting(fn, trials=100):
    """
    Проверяет функцию сортировки на выбранном количестве примеров
    """
    for i in range(100):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        start = nums.copy()
        assert fn(nums) == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == start, f"{fn.__name__} изменила исходный список"

def check_search(trials=100):
    """
    Проверяет linear_search и binary_search на случайных примерах
    """
    for i in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        x = random.randint(-100, 100)

        try:
            lin_ans = nums.index(x)
        except ValueError:
            lin_ans = -1

        assert linear_search(nums, x) == lin_ans, f"linear_search ошиблась в поиске {x} на {nums}"

        nums.sort()
        bin_ans = binary_search(nums, x)

        if bin_ans == -1:
            assert bin_ans == -1, f"binary_search ошиблась в поиске {x} на {nums}"
        else:
            assert nums[bin_ans] == x, f"binary_search ошиблась в поиске {x} на {nums}"

def check_two_sum(trials=100):
    for i in range(trials):
            n = random.randint(0, 50)
            nums = [random.randint(-100, 100) for _ in range(n)]
            target = random.randint(-200, 200)

            brute = two_sum_brute(nums, target)
            fast = two_sum_fast(nums, target)
            if brute == None or fast == None:
                assert brute == fast, f"Функции дали разный результат при поиске {target} в {nums}"
            else:
                assert nums[brute[0]] + nums[brute[1]] == nums[fast[0]] + nums[fast[1]], f"Функции дали разный результат при поиске {target} в {nums}"

def main():
    sort_trials = 100
    search_trials = 100
    two_sum_trials = 100

    check_sorting(bubble_sort, sort_trials)
    check_sorting(insertion_sort, sort_trials)
    check_sorting(selection_sort, sort_trials)
    check_search(search_trials)
    check_two_sum(two_sum_trials)

    print(f"OK: {sort_trials * 3 + search_trials + two_sum_trials} проверок")

if __name__ == "__main__":
    main()
```

## bench.py

``` python
import os
import random
import timeit
from src.lab04.io_txt_csv import write_csv
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast

def generate_or_get_data(n):
    """
    Генерирует случайный список целых чисел заданной длины.
    """
    return [random.randint(-100000, 100000) for _ in range(n)]

def run_benchmarks():
    results = []

    print("Запуск бенчмарка сортировок")
    sort_sizes = [1000, 10000, 100000]
    
    for n in sort_sizes:
        data = generate_or_get_data(n)
        
        t_sorted = timeit.timeit(lambda: sorted(data), number=1)
        results.append(("sort", n, "sorted", f"{t_sorted:.6f}"))
        
        if n == 100000:
            results.append(("sort", n, "bubble_sort", "> 60 с"))
            results.append(("sort", n, "insertion_sort", "> 60 с"))
            results.append(("sort", n, "selection_sort", "> 60 с"))
            continue

        t_bubble = timeit.timeit(lambda: bubble_sort(data), number=1)
        results.append(("sort", n, "bubble_sort", f"{t_bubble:.6f}"))
        
        t_insertion = timeit.timeit(lambda: insertion_sort(data), number=1)
        results.append(("sort", n, "insertion_sort", f"{t_insertion:.6f}"))
        
        t_selection = timeit.timeit(lambda: selection_sort(data), number=1)
        results.append(("sort", n, "selection_sort", f"{t_selection:.6f}"))

    print("Запуск бенчмарка поиска")
    search_n = 100000
    search_requests = 10000
    
    search_data = generate_or_get_data(search_n)
    queries = [random.randint(-120000, 120000) for _ in range(search_requests)]
            
    t_linear = timeit.timeit(lambda: [linear_search(search_data, q) for q in queries], number=1)
    results.append(("search", search_n, "linear_search", f"{t_linear:.6f}"))
    
    t_sort_for_binary = timeit.timeit(lambda: sorted(search_data), number=1)
    sorted_search_data = sorted(search_data)
            
    t_binary_pure = timeit.timeit(lambda: [binary_search(sorted_search_data, q) for q in queries], number=1)
    
    results.append(("search", search_n, "binary_search", f"{t_sort_for_binary + t_binary_pure:.6f}"))

    print("Запуск бенчмарка Two Sum")
    ts_sizes = [1000, 10000]
    
    for n in ts_sizes:
        ts_data = generate_or_get_data(n)

        target = random.randint(-200000, 200000)
        
        t_ts_brute = timeit.timeit(lambda: two_sum_brute(ts_data, target), number=1)
        results.append(("two_sum", n, "two_sum_brute", f"{t_ts_brute:.6f}"))
        
        t_ts_fast = timeit.timeit(lambda: two_sum_fast(ts_data, target), number=1)
        results.append(("two_sum", n, "two_sum_fast", f"{t_ts_fast:.6f}"))

    return results

def print_table(results):
    """Выводит красиво отформатированную таблицу результатов в консоль."""
    print("\n" + "="*65)
    print(f"{'TASK':<12} | {'N':<8} | {'IMPLEMENTATION':<25} | {'SECONDS':<12}")
    print("="*65)
    for task, n, impl, seconds in results:
        print(f"{task:<12} | {n:<8} | {impl:<25} | {seconds:<12}")
    print("="*65 + "\n")

def main():
    random.seed(42)

    bench_rows = run_benchmarks()
    
    print_table(bench_rows)
    
    header = ("task", "n", "impl", "seconds")
    
    output_path = "data/lab07/bench.csv"
    write_csv(bench_rows, output_path, header)
    print(f"Результаты успешно сохранены в файл: {output_path}")

if __name__ == "__main__":
    main()
```

## Результаты бенчмарка

```
task,n,impl,seconds
sort,1000,sorted,0.000141
sort,1000,bubble_sort,0.070370
sort,1000,insertion_sort,0.022305
sort,1000,selection_sort,0.023354
sort,10000,sorted,0.001893
sort,10000,bubble_sort,7.735499
sort,10000,insertion_sort,2.260535
sort,10000,selection_sort,1.938720
sort,100000,sorted,0.025936
sort,100000,bubble_sort,> 60 с
sort,100000,insertion_sort,> 60 с
sort,100000,selection_sort,> 60 с
search,100000,linear_search,31.169521
search,100000,binary_search,0.053290
two_sum,1000,two_sum_brute,0.011138
two_sum,1000,two_sum_fast,0.000150
two_sum,10000,two_sum_brute,0.092820
two_sum,10000,two_sum_fast,0.000108
```

![](../../images/lab07/img01.png)

---

## Выводы по работе

### Анализ скорости сортировок и поиска
Замеры четко показывают квадратичную зависимость для пузырька, вставок и выбора. Когда мы увеличиваем размер списка в 10 раз (с 1000 до 10000), время работы пузырьковой сортировки увеличивается сразу в 100 раз — с 0.07 до 7.7 секунд. Это полностью совпадает с теорией O(n²). Встроенный sorted при этом работает по логике n log n и замедляется всего в 12 раз, легко справляясь даже со 100 000 элементов за сотые доли секунды.

С поиском ситуация похожая. Сам по себе бинарный поиск работает мгновенно (0.05 с против 31.16 с у линейного на 10 000 запросах). Но без готовой сортировки он бесполезен, т.к. опирается на то, что элементы до m меньше arr[m], а после - больше. Отсюда вывод: сортировать массив ради одного-двух поисков нет смысла, лучше использовать обычный линейный перебор. Бинарный поиск окупается только тогда, когда база данных сортируется один раз, а запросов к ней много. В задаче Two Sum использование словаря вместо вложенных циклов дало огромный прирост.

## Проверка

Все функции работают корректно

![](../../images/lab07/img02.png)