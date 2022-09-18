import random
import sys
from time import process_time
from typing import List, Dict


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


def hybrid_sort_quick_insertion(arr: List[int], k=5) -> List[int]:
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


def check_time(arr: List[List], func):
    for item in arr:
        print(f"\n{item}")
        print(func(item))
        list_time = {}
        for k in range(1, 15):
            start = process_time()
            func(item)
            end = process_time()
            run_time = end - start
            # print(f"k = {k}\ttime = {'{:.0f}'.format(run_time)} seconds")
            print("k = {:d}\ttime = {:,.25f}".format(k,run_time))
            list_time[run_time] = k
        print(f"best k for this list is {list_time[min(list_time.keys())]}")


# R - количество массивов
# N - длинна массивов
# M - диапазон массивов
def generate_list(args: Dict) -> List[List]:
    list_arrays = list()
    for i in range(args["R"]):
        list_arrays.append(list(random.randint(0, args["M"]) for i in range(args["M"])))
    return list_arrays


def main(args: Dict[str, int]):
    arrays = generate_list(args)
    check_time(arrays, hybrid_sort_merge_insertion)


# R - количество массивов
# N - длинна массивов
# M - диапазон массивов
if __name__ == "__main__":
    tmp = {}
    for i in list(map(lambda x: x.split('='), sys.argv[1:])):
        tmp[i[0]] = int(i[1])
    main(tmp)