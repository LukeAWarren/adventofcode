from collections import deque

def find_path_from_0_to_9(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Find the start cell (containing 0) and the target (containing 9)
    start = None
    target_value = 9

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                start = (r, c)
                break
        if start is not None:
            break

    if start is None:
        print("No cell with value 0 found.")
        return None

    # Directions: up, down, left, right
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    # BFS Initialization
    queue = deque([start])
    visited = set([start])
    parent = {start: None}  # To reconstruct the path

    # BFS Loop
    while queue:
        r, c = queue.popleft()
        current_value = grid[r][c]

        # Check if we've reached value 9
        if current_value == target_value:
            # Reconstruct the path
            path = []
            cell = (r, c)
            while cell is not None:
                path.append(cell)
                cell = parent[cell]
            path.reverse()
            return path

        # Explore neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited:
                    # We can only proceed if grid[nr][nc] == current_value + 1
                    if grid[nr][nc] == current_value + 1:
                        visited.add((nr, nc))
                        parent[(nr, nc)] = (r, c)
                        queue.append((nr, nc))

    # If we exit the loop, no path was found
    return None


# Example usage with the given grid
grid = [
[8,9,0,1,0,1,2,3],
[7,8,1,2,1,8,7,4],
[8,7,4,3,0,9,6,5],
[9,6,5,4,9,8,7,4],
[4,5,6,7,8,9,0,3],
[3,2,0,1,9,0,1,2],
[0,1,3,2,9,8,0,1],
[1,0,4,5,6,7,3,2]
]

path = find_path_from_0_to_9(grid)
if path:
    print("Path found from 0 to 9:")
    # Print values along the path for clarity
    for (r,c) in path:
        print(f"({r},{c})={grid[r][c]}")
else:
    print("No path found.")
