# 2. Реализовать алгоритм "жадной раскраски"
import numpy as np


def generate_random_graph(size, min_value, max_value, replace_nonzeros=False):
    graph = np.random.randint(min_value, max_value, size=(size, size))
    if replace_nonzeros:
        graph = np.where(graph != 0, 1, graph)
    np.fill_diagonal(graph, 0)
    return graph


def greedy_coloring(graph):
    num_vertices = len(graph)
    colors = [-1] * num_vertices  # Инициализируем массив цветов для вершин

    colors[0] = 0  # Назначаем первой вершине первый цвет

    # Проходим по оставшимся вершинам и назначаем им цвета
    for v in range(1, num_vertices):
        available_colors = [
            True
        ] * num_vertices  # Инициализируем массив доступных цветов

        # Проверяем цвета соседних вершин и помечаем их как недоступные
        for neighbor in range(num_vertices):
            if graph[v][neighbor] != 0 and colors[neighbor] != -1:
                available_colors[colors[neighbor]] = False

        # Находим первый доступный цвет
        for color in range(num_vertices):
            if available_colors[color]:
                colors[v] = color
                break

    return colors


# Пример использования:
size = 25
min_value = 0
max_value = 2
replace_nonzeros = True

graph = generate_random_graph(size, min_value, max_value, replace_nonzeros)
print("Матрица смежности графа:")
print(graph)

colors = greedy_coloring(graph)
print("Раскраска вершин графа:")
for v, color in enumerate(colors):
    print("Вершина", v, "имеет цвет", color)
