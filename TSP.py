from itertools import permutations

nodes = ['A', 'B', 'C', 'D', 'E']

distances = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20, 'E': 12},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25, 'E': 18},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30, 'E': 22},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0, 'E': 16},
    'E': {'A': 12, 'B': 18, 'C': 22, 'D': 16, 'E': 0}
}

start = 'A'
other_nodes = [node for node in nodes if node != start]

minimum_distance = float('inf')
best_route = None

for route in permutations(other_nodes):
    full_route = (start,) + route + (start,)
    total_distance = 0

    for i in range(len(full_route) - 1):
        current_node = full_route[i]
        next_node = full_route[i + 1]
        total_distance += distances[current_node][next_node]

    print("Route:", " -> ".join(full_route),
          "| Distance:", total_distance)

    if total_distance < minimum_distance:
        minimum_distance = total_distance
        best_route = full_route

print("\n===== BEST ROUTE =====")
print("Route:", " -> ".join(best_route))
print("Minimum Distance:", minimum_distance)