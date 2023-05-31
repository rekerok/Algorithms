# 3. Реализовать алгоритм DSATUR
import numpy as np


def generate_random_graph(size, min_value, max_value, replace_nonzeros=False):
    graph = np.random.randint(min_value, max_value, size=(size, size))
    if replace_nonzeros:
        graph = np.where(graph != 0, 1, graph)
    np.fill_diagonal(graph, 0)
    return graph


def dsatur(graph):
    num_vertices = len(graph)
    colors = [-1] * num_vertices  # Инициализируем массив цветов для вершин
    saturation = [0] * num_vertices  # Инициализируем массив насыщенности вершин
    degree = np.sum(graph, axis=1)  # Вычисляем степени вершин

    # Находим вершину с наибольшей степенью и назначаем ей первый цвет
    max_degree_vertex = np.argmax(degree)
    colors[max_degree_vertex] = 0

    # Обновляем насыщенность соседних вершин
    for neighbor in range(num_vertices):
        if graph[max_degree_vertex][neighbor] != 0:
            saturation[neighbor] += 1

    # Раскрашиваем остальные вершины
    for _ in range(1, num_vertices):
        # Находим вершину с максимальной насыщенностью
        max_saturation_vertex = np.argmax(saturation)

        # Проверяем цвета соседних вершин и помечаем их как недоступные
        available_colors = set(range(num_vertices))
        for neighbor in range(num_vertices):
            if graph[max_saturation_vertex][neighbor] != 0 and colors[neighbor] != -1:
                available_colors.discard(colors[neighbor])

        # Находим наименьший доступный цвет
        color = min(available_colors)

        # Назначаем вершине найденный цвет
        colors[max_saturation_vertex] = color

        # Обновляем насыщенность соседних вершин
        for neighbor in range(num_vertices):
            if graph[max_saturation_vertex][neighbor] != 0:
                saturation[neighbor] += 1

    return colors


# Пример использования:
size = 5
min_value = 0
max_value = 2
replace_nonzeros = True

graph = generate_random_graph(size, min_value, max_value, replace_nonzeros)
print("Матрица смежности графа:")
print(graph)

colors = dsatur(graph)
print("Раскраска вершин графа:")
for v, color in enumerate(colors):
    print("Вершина", v, "имеет цвет", color, "и степень", np.sum(graph[v]))
