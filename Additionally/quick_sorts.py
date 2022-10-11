import random


def quick_sort_middle_element(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[len(array) // 2]
        less = list(filter(lambda x: x < pivot, array))
        middle = list(filter(lambda x: x == pivot, array))
        more = list(filter(lambda x: x > pivot, array))
        return quick_sort_middle_element(less) + middle + quick_sort_middle_element(more)


def quick_sort_second_element(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[1]
        less = list(filter(lambda x: x < pivot, array))
        middle = list(filter(lambda x: x == pivot, array))
        more = list(filter(lambda x: x > pivot, array))
        return quick_sort_second_element(less) + middle + quick_sort_second_element(more)


def median_element(*args):
    return sorted([i for i in args])


def quick_sort_median_element(array):
    if len(array) < 2:
        return array
    else:
        pivot = sorted([array[0], array[len(array) // 2], array[-1]])[1]
        less = list(filter(lambda x: x < pivot, array))
        middle = list(filter(lambda x: x == pivot, array))
        more = list(filter(lambda x: x > pivot, array))
        return quick_sort_median_element(less) + middle + quick_sort_median_element(more)


def quick_sort_lower_upper_median_element(array):
    if len(array) < 2:
        return array
    else:
        if len(array) == 2:
            tmp = sorted([array[0], array[len(array) // 2], array[-1]])
        else:
            tmp = sorted([array[0], array[len(array) // 2], array[(len(array) // 2) + 1], array[-1]])
        pivot = tmp[1] if len(tmp) % 2 == 0 else tmp[2]
        less = list(filter(lambda x: x < pivot, array))
        middle = list(filter(lambda x: x == pivot, array))
        more = list(filter(lambda x: x > pivot, array))
        return quick_sort_lower_upper_median_element(less) + middle + quick_sort_lower_upper_median_element(more)


def quick_sort_random_element(array):
    if len(array) < 2:
        return array
    else:
        pivot = random.choice(array)
        less = list(filter(lambda x: x < pivot, array))
        middle = list(filter(lambda x: x == pivot, array))
        more = list(filter(lambda x: x > pivot, array))
        return quick_sort_random_element(less) + middle + quick_sort_random_element(more)


def quick_sort_Hoara(array, low=None, high=None):
    if low is None and high is None:
        low, high = 0, len(array) - 1
    if low >= high:
        return
    pivot = min(array[low], array[high])
    i, j = low - 1, high + 1
    while True:
        while True:
            i = i + 1
            if array[i] >= pivot:
                break
        while True:
            j = j - 1
            if array[j] <= pivot:
                break
        if i >= j:
            break
        array[i], array[j] = array[j], array[i]
    quick_sort_Hoara(array, low, j)
    quick_sort_Hoara(array, j + 1, high)
    return array


def quick_sort_Lomuto(array, low=None, high=None):
    if low is None and high is None:
        low, high = 0, len(array) - 1
    if low < high:
        pivot = array[-1]
        i = low
        for j in range(low, high):
            if array[j] <= pivot:
                array[i], array[j] = array[j], array[i]
                i += 1
        array[i], array[high] = array[high], array[i]
        return quick_sort_Lomuto(array[low:i]) + quick_sort_Lomuto(array[i:high + 1])
    return array
