def knapsack(weights, value, capacity):
    n = len(weights)
    max_value = 0
    best_items = []

    for mask in range(1 , n):
        total_weight = 0
        total_value = 0
        items = []

        for i in range(n):
                if mask & (1 << i):
                    total_weight += weights[i]
                    total_value += values[i]
                    items.append(i + 1)

        if total_weight <= capacity and total_value > max_value:
                max_value = total_value
                best_items = items

    return max_value, best_items

n = int(input("Enter number of items:"))

weights = []
values = []

for i in range (n):
      w = int(input(f"Enter weight of item{i + 1}: "))
      v = int(input(f"Enter value of item{i + 1}: "))
      weights.append(w)
      values.append(v)

capacity = int(input("Enter Knapsack Capacity: "))

max_value, best_items = knapsack(weights, values, capacity)


print("\nMaximum Value:", max_value)
print("Selected items;", best_items)