def greedy_algorithm(items, budget):
    items_sorted = sorted(items.items(), key=lambda item: item[1]["calories"] / item[1]["cost"], reverse=True)
    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, data in items_sorted:
        if total_cost + data["cost"] <= budget:
            total_cost += data["cost"]
            total_calories += data["calories"]
            selected_items.append(item)

    return total_cost, total_calories, selected_items


def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item, data = list(items.items())[i - 1]
        for w in range(1, budget + 1):
            if data["cost"] <= w:
                dp[i][w] = max(data["calories"] + dp[i - 1][w - data["cost"]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    total_cost = 0
    total_calories = dp[n][budget]
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        item, data = list(items.items())[i - 1]
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item)
            w -= data["cost"]
            total_cost += data["cost"]

    return total_cost, total_calories, selected_items


# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Бюджет
budget = 50

# Жадібний алгоритм
cost_greedy, calories_greedy, items_greedy = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Загальна вартість:", cost_greedy)
print("Загальна калорійність:", calories_greedy)
print("Обрані страви:", items_greedy)

# Динамічне програмування
cost_dp, calories_dp, items_dp = dynamic_programming(items, budget)
print("\nДинамічне програмування:")
print("Загальна вартість:", cost_dp)
print("Загальна калорійність:", calories_dp)
print("Обрані страви:", items_dp)