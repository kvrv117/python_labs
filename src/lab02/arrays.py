from testing import test

def min_max(nums: list[float | int]):
    if len(nums) == 0:
        raise ValueError
    
    mn = nums[0]
    mx = nums[0]
    for a in nums:
        if a < mn:
            mn = a
        if a > mx:
            mx = a
    return (mn, mx)

def unique_sorted(nums: list[float | int]):
    unique_nums = set(nums)

    return qsort(list(unique_nums))

def qsort(a):
    if len(a) < 2:
        return a
    elif len(a) == 2:
        return [min(a), max(a)]
    m = a[0]
    mins = []
    maxs = []
    for c in a[1:]:
        if c <= m:
            mins.append(c)
        else:
            maxs.append(c)
    return qsort(mins) + [m] + qsort(maxs)

def flatten(mat: list[list | tuple]):
    out = []
    for a in mat:
        if type(a) not in [list, tuple]:
            raise TypeError
        out.extend(a)
    return out


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
print('==FLATTEN==')
test(flatten, tests_flatten)