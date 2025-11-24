print('Topic Name- "DFS Tree Search"\nDone By: Wajid Daud Tamboli\nB.Tech-CSE-\'A\'\nTitle Name -> 2.dfs')

def dfs_tree_search(graph, start, goal):
    stack = [(start, [start])]

    while stack:
        node, path = stack.pop()
        print("Exploring:", node)

        if node == goal:
            print("\nGoal found!")
            return path

        for child in graph.get(node, []):
            new_path = path + [child]
            stack.append((child, new_path))

    print("Goal not found!")
    return None


graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

start_node = 'A'
goal_node = 'G'

path = dfs_tree_search(graph, start_node, goal_node)

if path:
    print("Path to goal:", " -> ".join(path))
