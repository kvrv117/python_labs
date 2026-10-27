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