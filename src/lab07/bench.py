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
