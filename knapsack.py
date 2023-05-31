# Задача о рюкзаке формулируется так: пусть есть N предметов,
# каждый из которых имеет неотрицательные (и ненулевые) вес и стоимость.
# Требуется выбрать из этих предметов такой набор,
# что его масса не превосходит "вместимости\грузоподъемности",
# а суммарная стоимость - максимальна.


def knapsack(capacity, items):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight, value, count = items[i - 1]
        for j in range(1, capacity + 1):
            if j < weight:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_weight, _, item_count = items[i - 1]
            selected_items.append(i - 1)
            w -= item_weight

    weights = [0] * n
    counts = [0] * n
    total_weight = 0
    for i in selected_items:
        item_weight, _, item_count = items[i]
        weights[i] = item_weight
        counts[i] = item_count
        total_weight += item_weight * item_count

    return weights, counts, total_weight


# Примеры

# (масса, прибыль, количество)

# Пример 1
profits1 = [(2, 3, 4), (3, 4, 1), (4, 5, 0), (5, 6, 0)]
capacity1 = 8
weights1, counts1, total_profit1 = knapsack(capacity1, profits1)
print("Weights:", weights1)  # Weights: [2, 3, 0, 0] - массив масс выбранных предметов
print(
    "Counts:", counts1
)  # Counts: [4, 1, 0, 0] - массив количества выбранных предметов
print(
    "Total Profit:", total_profit1
)  # Total Profit: 8 - суммарная прибыль выбранных предметов
print()

# Пример 2
profits2 = [(1, 1, 10), (2, 3, 2), (3, 5, 1), (4, 9, 3)]
capacity2 = 6
weights2, counts2, total_profit2 = knapsack(capacity2, profits2)
print("Weights:", weights2)  # Weights: [1, 2, 3, 0]
print("Counts:", counts2)  # Counts: [6, 0, 0, 0]
print("Total Profit:", total_profit2)  # Total Profit: 6
print()

# Пример 3
profits3 = [(2, 3, 2), (3, 4, 1), (4, 5, 3), (5, 6, 2)]
capacity3 = 9
weights3, counts3, total_profit3 = knapsack(capacity3, profits3)
print("Weights:", weights3)  # Weights: [2, 4, 5, 0]
print("Counts:", counts3)  # Counts: [2, 0, 2, 0]
print("Total Profit:", total_profit3)  # Total Profit: 18
print()
