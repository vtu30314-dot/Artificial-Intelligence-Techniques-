"""Task 5 - Ant Colony Optimization (route among multiple cities)"""
import numpy as np

distance = np.array([
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
])

n_cities = len(distance)
n_ants = 10
n_iterations = 100
alpha = 1.0      # pheromone importance
beta = 2.0       # distance importance
evaporation = 0.5
Q = 100

rng = np.random.default_rng(42)

# 1) Initialize pheromone values on all routes
pheromone = np.ones((n_cities, n_cities))

best_route = []
best_distance = float('inf')

for iteration in range(n_iterations):
    all_routes, all_lengths = [], []

    # 2) place ants randomly on cities
    for ant in range(n_ants):
        start = int(rng.integers(n_cities))
        route = [start]
        current = start

        # 3) each ant constructs a route by selecting next city
        #    based on pheromone and distance
        while len(route) < n_cities:
            unvisited = [c for c in range(n_cities) if c not in route]
            probs = np.array([
                (pheromone[current][c] ** alpha) * ((1.0 / distance[current][c]) ** beta)
                for c in unvisited
            ])
            probs = probs / probs.sum()
            nxt = int(rng.choice(unvisited, p=probs))
            route.append(nxt)
            current = nxt

        # 4) calculate total distance travelled by each ant (return to start)
        length = sum(distance[route[i]][route[(i + 1) % n_cities]]
                     for i in range(n_cities))
        all_routes.append(route)
        all_lengths.append(length)

        if length < best_distance:
            best_distance = length
            best_route = route[:]

    # 5) update pheromone trails
    pheromone *= (1 - evaporation)
    for route, length in zip(all_routes, all_lengths):
        for i in range(n_cities):
            a, b = route[i], route[(i + 1) % n_cities]
            pheromone[a][b] += Q / length
            pheromone[b][a] += Q / length

print("Best route:", best_route)
print("Minimum Distance:", best_distance)
