from collections import deque


def num_islands(grid):
    """Count 4-connected groups of '1'. BFS from each unvisited land cell. O(R*C)."""
    if not grid:
        return 0
    rows, cols, seen, count = len(grid), len(grid[0]), set(), 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in seen:
                count += 1
                q = deque([(r, c)])
                seen.add((r, c))
                while q:
                    x, y = q.popleft()
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1" and (nx, ny) not in seen:
                            seen.add((nx, ny))
                            q.append((nx, ny))
    return count


def shortest_path_grid(grid):
    """Fewest steps from top-left to bottom-right through 0-cells, or -1. BFS O(R*C)."""
    rows, cols = len(grid), len(grid[0])
    if grid[0][0] or grid[-1][-1]:
        return -1
    q, seen = deque([(0, 0, 0)]), {(0, 0)}
    while q:
        r, c, d = q.popleft()
        if (r, c) == (rows - 1, cols - 1):
            return d
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not grid[nr][nc] and (nr, nc) not in seen:
                seen.add((nr, nc))
                q.append((nr, nc, d + 1))
    return -1
