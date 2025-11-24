print('Topic Name- "8-Puzzle BFS"\nDone By: Wajid Daud Tamboli\nB.Tech-CSE-\'A\'\nTitle Name -> 4.8 puzzle')

from collections import deque

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]


def print_board(state):
    for row in state:
        print(row)
    print()


def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def get_neighbors(state):
    neighbors = []
    x, y = find_zero(state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors


def to_tuple(state):
    return tuple(tuple(row) for row in state)


def bfs(start_state):
    visited = set()
    queue = deque([(start_state, [])])
    visited.add(to_tuple(start_state))

    while queue:
        state, path = queue.popleft()

        if state == goal_state:
            print("Goal reached! Path length:", len(path))
            return path + [state]

        for neighbor in get_neighbors(state):
            t = to_tuple(neighbor)
            if t not in visited:
                visited.add(t)
                queue.append((neighbor, path + [state]))

    print("No solution found!")
    return None


start_state = [[1, 2, 3],
               [4, 0, 6],
               [7, 5, 8]]

solution = bfs(start_state)

if solution:
    print("\nSolution Path:")
    for step, s in enumerate(solution):
        print("Step", step)
        print_board(s)
