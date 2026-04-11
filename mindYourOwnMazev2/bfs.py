from collections import deque

def neighbours(r, c, rows, cols):
    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc

def bfs(start, goal, grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        r, c = queue.popleft()

        if (r, c) == goal:
            break

        for nr, nc in neighbours(r, c, rows, cols):
            if (nr, nc) in visited:
                continue

            visited.add((nr, nc))
            parent[(nr, nc)] = (r, c)
            queue.append((nr, nc))

    # ⭐ If goal was never reached
    if goal not in parent:
        return None

    # ⭐ Reconstruct path
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]

    path.reverse()
    return path