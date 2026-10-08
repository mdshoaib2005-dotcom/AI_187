weights = [10, 12, 8, 14, 17]
profits = [78, 60, 90, 100, 140]

capacity = int(input("Enter capacity of the knapsack:"))

n = len(weights)
max_profit = 0
best_items = []

for i in range(2 ** n):
    total_weight = 0
    total_profit = 0
    items = []

    for j in range (n):
        if i & (1 << j):
            total_weight += weights[j]
            total_profit += profits[j]
            items.append(j + 1)
    if total_weight <= capacity and total_profit > max_profit:
        max_profit = total_profit
        best_items = items

print("Selected items:", best_items)
print("Maximum Profit:", max_profit)



