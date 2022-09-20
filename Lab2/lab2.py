import sys
from typing import Dict, List, Union
from Lab1 import lab1


def interpolationSearch(arr: List, item: int) -> bool:
    if len(arr) == 1:
        return False
    else:
        low = 0
        height = len(arr) - 1
        mid = low + ((item - arr[low]) * (height - low)) // (arr[height] - arr[low])
        if mid > len(arr) - 1 or arr[mid] != item:
            return False
        if item == arr[mid]:
            return True
        elif item < arr[mid]:
            return interpolationSearch(arr[0:mid], item)
        else:
            return interpolationSearch(arr[mid:len(arr)], item)


def binary_search(arr: List, item: int) -> bool:
    if len(arr) == 1:
        return False
    else:
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
    print(interpolationSearch(
        sorted([6, 1, 8, 1, 7, 5, 2, 5]), 5))


# x - ключ по которому ищем
# N - длинна массивов
# M - диапазон массивов
if __name__ == "__main__":
    tmp = {}
    for i in list(map(lambda x: x.split('='), sys.argv[1:])):
        tmp[i[0]] = int(i[1])
    print(tmp)
    main(tmp)
