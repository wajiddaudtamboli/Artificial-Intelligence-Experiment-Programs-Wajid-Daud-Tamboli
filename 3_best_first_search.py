print('Topic Name- "Best First Search"\nDone By: Wajid Daud Tamboli\nB.Tech-CSE-\'A\'\nTitle Name -> 3.bfs')

import heapq


def best_first_search(graph, heuristics, start, goal):
    visited = set()
    priority_queue = []
    
    heapq.heappush(priority_queue, (heuristics[start], start, [start]))

    while priority_queue:
        _, current, path = heapq.heappop(priority_queue)
        print("Visiting:", current)

        if current == goal:
            print("\nGoal Found!")
            return path

        visited.add(current)

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristics[neighbor], neighbor, path + [neighbor]))

    print("\nGoal not found!")
    return None


graph = {
    'S': ['A', 'B', 'C'],
    'A': ['D', 'E'],
    'B': [],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

heuristics = {
    'S': 7, 'A': 6, 'B': 4, 'C': 5,
    'D': 3, 'E': 2, 'F': 1, 'G': 0
}

start_node = 'S'
goal_node = 'G'

path = best_first_search(graph, heuristics, start_node, goal_node)

if path:
    print("Path to goal:", " -> ".join(path))
