# Define the items (name, weight, value)
items = [
    ("Water", 200, 50),
    ("Food", 300, 60),
    ("Medicine", 100, 40),
    ("Blankets", 250, 30),
    ("Tents", 400, 70),
    ("Batteries", 150, 20),
]

# Define the weight capacity of the knapsack (helicopter)
capacity = 500




# Number of items
n = len(items)

# Initialize the DP table
dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

# Build the DP table
for i in range(1, n + 1):
    for w in range(1, capacity + 1):
        name, weight, value = items[i - 1]
        if weight <= w:
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
        else:
            dp[i][w] = dp[i - 1][w]

# Backtrack to find the selected items
selected_items = []
w = capacity
for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        selected_items.append(items[i - 1])
        w -= items[i - 1][1]

# Print the results
print("Selected Items:")
for item in selected_items:
    print(f"- {item[0]} (Weight: {item[1]}, Value: {item[2]})")

total_weight = sum(item[1] for item in selected_items)
total_value = sum(item[2] for item in selected_items)

print(f"\nTotal Weight: {total_weight}")
print(f"Total Value: {total_value}")
