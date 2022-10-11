from pprint import pprint
from time import process_time

from quick_sorts import *


def tmp(array, func):
    start = process_time()
    print(func)
    end = process_time()
    return end - start


def check_time_sorts(array):
    dict_sorts = {}
    dict_sorts["quick_sort_middle_element"] = tmp(array, quick_sort_middle_element(array))
    dict_sorts["quick_sort_second_element"] = tmp(array, quick_sort_second_element(array))
    dict_sorts["quick_sort_median_element"] = tmp(array, quick_sort_median_element(array))
    dict_sorts["quick_sort_lower_upper_median_element"] = tmp(array, quick_sort_lower_upper_median_element(array))
    dict_sorts["quick_sort_random_element"] = tmp(array, quick_sort_random_element(array))
    dict_sorts["quick_sort_Hoara"] = tmp(array, quick_sort_Hoara(array.copy()))
    dict_sorts["quick_sort_Lomuto"] = tmp(array, quick_sort_Lomuto(array.copy()))
    pprint(dict_sorts)

def main():
    uniform_array = [round(random.uniform(0, 100), 3) for _ in range(10)]
    gauss_array = [round(random.gauss(50, 50), 3) for _ in range(10)]
    print(f"uniform array - {uniform_array}")
    print(f"gauss array - {gauss_array}")
    check_time_sorts(uniform_array)

if __name__ == "__main__":
    main()
