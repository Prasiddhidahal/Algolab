import time
import matplotlib.pyplot as plt
from itertools import combinations, chain

# Brute Force for 0/1 Knapsack
def knapsack_bruteforce_01(weights, values, capacity):
    n = len(weights)
    best_value, best_subset = 0, ()
    for subset in chain.from_iterable(combinations(range(n), r) for r in range(n + 1)):
        total_weight = sum(weights[i] for i in subset)
        total_value = sum(values[i] for i in subset)
        if total_weight <= capacity and total_value > best_value:
            best_value, best_subset = total_value, subset
    return best_value, best_subset

# Brute Force for Fractional Knapsack
def knapsack_bruteforce_fractional(weights, values, capacity):
    n = len(weights)
    max_value = 0
    for subset in chain.from_iterable(combinations(range(n), r) for r in range(n + 1)):
        total_weight = sum(weights[i] for i in subset)
        if total_weight <= capacity:
            total_value = sum(values[i] for i in subset)
            remaining_capacity = capacity - total_weight
            remaining_items = sorted([(values[i]/weights[i], weights[i]) for i in range(n) if i not in subset], reverse=True)
            for value_density, weight in remaining_items:
                if remaining_capacity == 0:
                    break
                if weight <= remaining_capacity:
                    total_value += value_density * weight
                    remaining_capacity -= weight
                else:
                    total_value += value_density * remaining_capacity
                    remaining_capacity = 0
            max_value = max(max_value, total_value)
    return max_value

# Greedy Method for Fractional Knapsack
def knapsack_greedy_fractional(weights, values, capacity):
    items = sorted([(v/w, w, v) for v, w in zip(values, weights)], reverse=True)
    total_value = 0
    for ratio, weight, value in items:
        if capacity == 0:
            break
        if weight <= capacity:
            capacity -= weight
            total_value += value
        else:
            total_value += ratio * capacity
            capacity = 0
    return total_value

# Performance Measurement
def measure_time(weights, values, capacity, method):
    start = time.time()
    if method == 'bruteforce_01':
        knapsack_bruteforce_01(weights, values, capacity)
    elif method == 'bruteforce_fractional':
        knapsack_bruteforce_fractional(weights, values, capacity)
    elif method == 'greedy_fractional':
        knapsack_greedy_fractional(weights, values, capacity)
    return time.time() - start

# Data Generation and Measurement
item_counts = range(1, 15)  # 1 to 14 items
methods = ['bruteforce_01', 'bruteforce_fractional', 'greedy_fractional']
times = {method: [] for method in methods}

for count in item_counts:
    weights = list(range(1, count + 1))
    values = [w * 2 for w in weights]
    capacity = sum(weights) // 2

    print(f"Measuring time for {count} items")
    for method in methods:
        times[method].append(measure_time(weights, values, capacity, method))

# Plotting the Results
plt.figure(figsize=(12, 8))
for method in methods:
    plt.plot(item_counts, times[method], label=f'{method.replace("_", " ").title()}', marker='o')
plt.xlabel('Number of Items')
plt.ylabel('Time (seconds)')
plt.title('Performance of Knapsack Solvers')
plt.legend()
plt.grid(True)
plt.show()
