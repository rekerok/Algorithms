# 1. Реализовать алгоритм 2-замены для задачи коммивояжера

import numpy as np


def generate_random_graph(size, min_value, max_value):
    graph = np.random.randint(min_value, max_value, size=(size, size))
    np.fill_diagonal(graph, 0)
    return graph


def generate_random_path(size):
    path = list(range(size))
    np.random.shuffle(path)
    return path


def two_opt(graph, path):
    best_path = path.copy()
    improved = True
    while improved:
        improved = False
        for i in range(1, len(path) - 2):
            for j in range(i + 1, len(path)):
                if j - i == 1:
                    continue
                new_path = path.copy()
                new_path[i:j] = path[j - 1 : i - 1 : -1]
                if calculate_path_length(graph, new_path) < calculate_path_length(
                    graph, best_path
                ):
                    best_path = new_path.copy()
                    improved = True
        path = best_path.copy()
    return best_path


def calculate_path_length(graph, path):
    length = 0
    for i in range(len(path) - 1):
        length += graph[path[i]][path[i + 1]]
    return length


# Пример использования:
size = 5
min_value = 1
max_value = 10

graph = generate_random_graph(size, min_value, max_value)
path = generate_random_path(size)

print("Матрица графа:")
print(graph)
print("Начальный путь:")
print(path)

optimized_path = two_opt(graph, path)
print("Оптимизированный путь:")
print(optimized_path)
print("Длина исходного пути:", calculate_path_length(graph, path))
print("Длина оптимизированного пути:", calculate_path_length(graph, optimized_path))
