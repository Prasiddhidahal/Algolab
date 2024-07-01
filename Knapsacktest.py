
# Test Case for Knapsack 0/1 and Fractional Knapsack
test_case_1 = {
    "capacity": 50,
    "items": [
        {"weight": 10, "value": 60},
        {"weight": 20, "value": 100},
        {"weight": 30, "value": 120},
    ],
    "expected_01": 220,  # Expected result for 0/1 Knapsack
    "expected_fractional": 240.0,  # Expected result for Fractional Knapsack
}

# Additional Test Case for the Greedy Algorithm
test_case_2 = {
    "activities": [
        {"start": 1, "end": 4},
        {"start": 3, "end": 5},
        {"start": 0, "end": 6},
        {"start": 5, "end": 7},
        {"start": 3, "end": 8},
        {"start": 5, "end": 9},
        {"start": 6, "end": 10},
        {"start": 8, "end": 11},
        {"start": 8, "end": 12},
        {"start": 2, "end": 13},
        {"start": 12, "end": 14},
    ],
    "expected_greedy": 4  # Expected number of activities selected
}












def knapsack_01(capacity, items):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if items[i - 1]['weight'] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[i - 1]['weight']] + items[i - 1]['value'])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

def fractional_knapsack(capacity, items):
    items.sort(key=lambda x: x['value'] / x['weight'], reverse=True)
    total_value = 0.0
    for item in items:
        if capacity >= item['weight']:
            total_value += item['value']
            capacity -= item['weight']
        else:
            total_value += item['value'] * (capacity / item['weight'])
            break
    return total_value

def activity_selection(activities):
    activities.sort(key=lambda x: x['end'])
    selected = []
    current_end = 0
    for activity in activities:
        if activity['start'] >= current_end:
            selected.append(activity)
            current_end = activity['end']
    return len(selected)

# Testing Knapsack 0/1
result_01 = knapsack_01(test_case_1['capacity'], test_case_1['items'])
print(f"Knapsack 0/1 result: {result_01} (Expected: {test_case_1['expected_01']})")

# Testing Fractional Knapsack
result_fractional = fractional_knapsack(test_case_1['capacity'], test_case_1['items'])
print(f"Fractional Knapsack result: {result_fractional} (Expected: {test_case_1['expected_fractional']})")

# Testing Greedy Algorithm for Activity Selection
result_greedy = activity_selection(test_case_2['activities'])
print(f"Greedy Algorithm result: {result_greedy} (Expected: {test_case_2['expected_greedy']})")
