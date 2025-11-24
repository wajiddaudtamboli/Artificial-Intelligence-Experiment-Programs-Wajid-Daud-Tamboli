print('Topic Name- "Travelling Salesman Problem"\nDone By: Wajid Daud Tamboli\nB.Tech-CSE-\'A\'\nTitle Name -> 5.travelling_salesman')

from itertools import permutations

def travelling_salesperson_bruteforce(graph, start):
    cities = list(range(len(graph)))
    cities.remove(start)
    
    min_path = float('inf')
    best_route = None
    
    for perm in permutations(cities):
        current_cost = 0
        k = start
        for j in perm:
            current_cost += graph[k][j]
            k = j
        current_cost += graph[k][start]
        
        if current_cost < min_path:
            min_path = current_cost
            best_route = (start,) + perm + (start,)
    
    print("Best route:", best_route)
    print("Minimum cost:", min_path)


graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

travelling_salesperson_bruteforce(graph, start=0)
