import random

# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'F': ['G']
}

# Heuristic values (lower value = better state)
heuristic = {'A': 6,'B': 4,'C': 5,'D': 3,'E': 2,'F': 1,'G': 0}

# 1. Simple Hill Climbing (Descent)
def simple_hill_climbing(start):
    current = start
    path = [current]

    while True:
        moved = False

        for neighbor in graph.get(current, []):
            if heuristic[neighbor] < heuristic[current]:
                current = neighbor
                path.append(current)
                moved = True
                break   # move to first better neighbor

        if not moved:
            # stuck at local minimum
            return current, path
        


# 2. Steepest Descent Hill Climbing
def steepest_hill_climbing(start):
    current = start
    path = [current]

    while True:
        neighbors = graph.get(current, [])
        best = current

        # Find the best (lowest heuristic) neighbor
        for neighbor in neighbors:
            if heuristic[neighbor] < heuristic[best]:
                best = neighbor

        if best == current:
            break

        current = best
        path.append(current)

    return current, path

# 3. Stochastic Hill Climbing (Descent)
def stochastic_hill_climbing(start):
    current = start
    path = [current]

    while True:
        better_neighbors = []

        # Collect all better neighbors
        for neighbor in graph.get(current, []):
            if heuristic[neighbor] < heuristic[current]:
                better_neighbors.append(neighbor)

        if not better_neighbors:
            break

        # Randomly choose one better neighbor
        current = random.choice(better_neighbors)
        path.append(current)

    return current, path

start = 'A'

result, path = simple_hill_climbing(start)
print("Simple HC Path:", " > ".join(path), "| Stuck at:", result)

result, path = steepest_hill_climbing(start)
print("Steepest HC Path:", " > ".join(path), "| Stuck at:", result)

result, path = stochastic_hill_climbing(start)
print("Stochastic HC Path:", " > ".join(path), "| Final:", result)