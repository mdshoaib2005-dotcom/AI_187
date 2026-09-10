# Greedy Best First Search

graph = {
    'S': {'A': 7, 'C': 8},
    'A': {'S': 7, 'B': 9, 'D': 10},
    'B': {'A': 9, 'E': 6, 'G': 12},
    'C': {'S': 8, 'D': 8},
    'D': {'A': 10, 'C': 8, 'E': 7},
    'E': {'B': 6, 'D': 7, 'G': 4},
    'G': {'B': 12, 'E': 4}
}

h = {
    'S': 23,
    'A': 17,
    'B': 8,
    'C': 18,
    'D': 10,
    'E': 3,
    'G': 0
}

start = 'S'
goal = 'G'

open_list = [start]
visited = []
parent = {start: None}

while open_list:

    current = min(open_list, key=lambda node: h[node])
    open_list.remove(current)

    print("Visiting:", current)

    if current == goal:
        break

    visited.append(current)

    for neighbor in graph[current]:

        if neighbor not in visited and neighbor not in open_list:
            open_list.append(neighbor)
            parent[neighbor] = current

path = []
current = goal

while current is not None:
    path.append(current)
    current = parent[current]

path.reverse()

cost = 0

for i in range(len(path) - 1):
    cost += graph[path[i]][path[i + 1]]

print("\nGBFS Path:", " -> ".join(path))
print("Total Cost:", cost)