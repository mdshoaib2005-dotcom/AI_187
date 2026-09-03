import heapq

graph = {
    'S': [('A', 7), ('C', 8)],
    'A': [('S', 7), ('B', 8), ('G', 10)],
    'B': [('A', 8), ('C', 5), ('G', 4)],
    'C': [('S', 8), ('B', 5), ('D', 6)],
    'D': [('C', 6), ('G', 6)],
    'G': [('A', 10), ('B', 4), ('D', 6)]
}


def uniform_cost_search(start, goal):

    queue = [(0, start, [start])]
    visited = set()

    while queue:

        cost, node, path = heapq.heappop(queue)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return path, cost

        for neighbour, edge_cost in graph[node]:

            if neighbour not in visited:

                new_cost = cost + edge_cost
                new_path = path + [neighbour]

                heapq.heappush(
                    queue,
                    (new_cost, neighbour, new_path)
                )

    return None, None


start = 'S'
goal = 'G'

path, cost = uniform_cost_search(start, goal)

print("Uniform Cost Search")
print("-------------------")
print("Path:", " -> ".join(path))
print("Minimum Cost:", cost)