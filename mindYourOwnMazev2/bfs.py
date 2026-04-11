from collections import deque

def neighbours(r, c, rows, cols):
    # Generate valid orthogonal neighbour coordinates (up, down, left, right)
    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        nr, nc = r + dr, c + dc
        # Only gets neighbours that stay within grid boundaries
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc

def bfs(start, goal, grid):
    # Grid dimensions
    rows, cols = len(grid), len(grid[0])
     # Queue for BFS frontier; start node is the first to explore
    queue = deque([start])
     # Track visited cells to avoid reprocessing
    visited = {start}
     # Parent dictionary used to reconstruct the final path
    parent = {start: None}

    while queue:
        r, c = queue.popleft()
# Stop early if the goal is reached
        if (r, c) == goal:
            break
# Explore to find all valid neighbours
        for nr, nc in neighbours(r, c, rows, cols):
# Skip already‑visited cells
            if (nr, nc) in visited:
                continue
# Skip walls or blocked cells
            if grid[nr][nc] == "#":
                continue
# Mark neighbour as visited and record its parent
            visited.add((nr, nc))
            parent[(nr, nc)] = (r, c)
 # Add neighbour to BFS queue
            queue.append((nr, nc))

    #  If goal was never reached
    if goal not in parent:
        return None

    #  Reconstruct shortest path
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]

    path.reverse()
    return path