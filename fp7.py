import random
import matplotlib.pyplot as plt

def roll_dice(num_dice=2, num_rolls=10000):
    sums = {}
    for _ in range(num_rolls):
        roll = sum(random.randint(1, 6) for _ in range(num_dice))
        sums[roll] = sums.get(roll, 0) + 1
    probabilities = {k: v / num_rolls for k, v in sums.items()}
    return probabilities

def print_table(probabilities):
    print("| Сума | Ймовірність |")
    print("|---|---|")
    for sum_, probability in probabilities.items():
        print(f"| {sum_} | {probability:.4f} |")

def plot_probabilities(probabilities):
    plt.bar(probabilities.keys(), probabilities.values())
    plt.xlabel("Сума")
    plt.ylabel("Ймовірність")
    plt.title("Ймовірності сум при киданні двох кубиків (метод Монте-Карло)")
    plt.show()

# Симуляція кидків
probabilities = roll_dice()

# Відображення графіка
plot_probabilities(probabilities)