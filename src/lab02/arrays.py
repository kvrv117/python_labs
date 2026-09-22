import traceback

def min_max(nums: list[float | int]):
    if len(nums) == 0:
        raise ValueError
    return (min(nums), max(nums))

def unique_sorted(nums: list[float | int]):
    unique_nums = set(nums)
    return list(sorted(unique_nums))

def flatten(mat: list[list | tuple]):
    out = []
    for a in mat:
        if type(a) not in [list, tuple]:
            raise TypeError
        out.extend(a)
    return out

def test(func, cases):
    for c in cases:
        out = ''
        try:
            out = func(c)
        except Exception as e:
            out = traceback.format_exception(e)[-1].strip()
        print(f'{c} -> {out}')

tests_min_max = [
    [3, -1, 5, 5, 0],
    [42],
    [-5, -2, -9],
    [],
    [1.5, 2, 2.0, -3.1]
]

tests_unique_sorted = [
    [3, 1, 2, 1, 3],
    [],
    [-1, -1, 0, 2, 2],
    [1.0, 1, 2.5, 2.5, 0]
]

tests_flatten = [
    [[1, 2], [3, 4]],
    [[1, 2], (3, 4, 5)],
    [[1], [], [2, 3]],
    [[1, 2], "ab"]
]

print('==MIN MAX==')
test(min_max, tests_min_max)
print()
print('==UNIQUE SORTED==')
test(unique_sorted, tests_unique_sorted)
print()
print('==Flatten==')
test(flatten, tests_flatten)