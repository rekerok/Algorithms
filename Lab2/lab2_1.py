import sys
from typing import Dict, List

from Lab1 import lab1


def interpolation_search(arr: List, item: int) -> bool:
    low = 0
    high = len(arr) - 1
    arr.sort()
    if arr[low] == arr[high] and arr[low] != item:
        return False
    else:
        mid = low + ((item - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if mid < low or mid > high:
            return False

        if arr[mid] == item:
            return True

        if item < arr[mid]:
            return interpolation_search(arr[low:mid], item)
        else:
            print(arr[mid:low])
            return interpolation_search(arr[mid:high], item)


def binary_search(arr: List, item: int) -> bool:
    if len(arr) == 1:
        return True if arr[0] == item else False
    else:
        arr.sort()
        mid = len(arr) // 2
        if item == arr[mid]:
            return True
        elif item < arr[mid]:
            return binary_search(arr[0:mid], item)
        else:
            return binary_search(arr[mid:len(arr)], item)


# x - ключ по которому ищем
# N - длинна массива
# M - диапазон массива
def main(args: Dict[str, int]):
    arr = lab1.generate_list_range(0, args['M'], args['N'])
    print(sorted(arr))
    print(f"interpolation_search - {interpolation_search(arr, args['x'])}")
    print(f"binary_search - {binary_search(arr, args['x'])}")
    print(f"python_function - {args['x'] in arr}")


# x - ключ по которому ищем
# N - длинна массивов
# M - диапазон массивов
if __name__ == "__main__":
    tmp = {}
    if len(sys.argv) == 1:
        tmp['x'] = int(input("x - ключ по которому ищем = "))
        tmp['N'] = int(input("N - длинна массивов = "))
        tmp['M'] = int(input("M - диапазон массивов = "))
    else:
        for i in list(map(lambda x: x.split('='), sys.argv[1:])):
            tmp[i[0]] = int(i[1])
    main(tmp)
