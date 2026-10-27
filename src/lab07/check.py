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