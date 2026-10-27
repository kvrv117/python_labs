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