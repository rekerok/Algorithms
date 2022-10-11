import sys
from time import process_time
from typing import List, Dict

import numpy as np


def euclid_algorithm(a: int, b: int) -> int:
    iter = 0
    if a < b:
        a, b = b, a
    mod = None
    while mod != 0:
        mod = a % b
        a, b = b, mod
        iter += 1
    return iter


def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr


def hybrid_sort_quick_insertion(arr: List[int], k) -> List[int]:
    if len(arr) < 2:
        return arr
    pivot = arr[len(arr) // 2]
    left_side = list(filter(lambda x: x < pivot, arr))
    center = list(filter(lambda x: x == pivot, arr))
    right_side = list(filter(lambda x: x > pivot, arr))
    return (insertion_sort(left_side) if len(left_side) < k else hybrid_sort_quick_insertion(left_side)) + center + (
        insertion_sort(right_side) if len(right_side) < k else hybrid_sort_quick_insertion(right_side))


def hybrid_sort_merge_insertion(arr: List[int], k=5) -> List[int]:
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = insertion_sort(left) if len(left) < k else hybrid_sort_merge_insertion(left)
    right = insertion_sort(right) if len(right) < k else hybrid_sort_merge_insertion(right)
    i = j = 0
    sorted_arr = list()
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    if i < len(left):
        sorted_arr += left[i:]
    elif j < len(right):
        sorted_arr += right[j:]
    return sorted_arr


# Функция считает лучшее 'k' для кучи массивов
def check_time(arr: List[List], func):
    best_k = 0
    best_sum = None
    for k in range(len(arr[0]) // 2):
        sum_time = 0
        print(f"k = {k}")
        for j in arr:
            print(f"\t{j}")
            start = process_time()
            print(f"\t{func(j, k)}")
            end = process_time()
            run_time = end - start
            print("\trun_time = {:,.10f}\n".format(run_time))
            sum_time += run_time
        if not best_sum or best_sum > sum_time:
            best_sum = sum_time
            best_k = k

        print("k = {:d}\tsum_time = {:,.10f}\n".format(k, sum_time))
    print("for this arrays best k is {:d} with time {:,.10f}".format(best_k, best_sum))


def generate_list_range(min_element: int, max_element: int, length_array: int) -> np.array:
    return np.random.uniform(min_element, max_element, length_array).tolist()
    # return generate_list_range(0, 10, 100)


# R - количество массивов
# N - длинна массивов
# M - диапазон массивов
def generate_list(args: Dict) -> List[List]:
    list_arrays = list()
    for i in range(args["R"]):
        list_arrays.append(generate_list_range(0, args['M'], args['N']))
    return list_arrays


def main(args: Dict[str, int]):
    arrays = generate_list(args)
    check_time(arrays, hybrid_sort_merge_insertion)


# R - количество массивов
# N - длинна массивов
# M - диапазон массивов
if __name__ == "__main__":
    tmp = {}
    if len(sys.argv) == 1:
        tmp['R'] = int(input("R - количество массивов = "))
        tmp['N'] = int(input("N - длинна массивов = "))
        tmp['M'] = int(input("M - диапазон массивов = "))
    else:
        for i in list(map(lambda x: x.split('='), sys.argv[1:])):
            tmp[i[0]] = int(i[1])
    main(tmp)
