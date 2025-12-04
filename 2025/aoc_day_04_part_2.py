# ChatGPT Assisted
import os

paper_roll_locations = []

def load_paper_roll_locations(file_name, paper_roll_locations):
    file = open(file_name)
    for row in file.readlines():
        paper_roll_locations.append(row.rstrip())
    file.close()

load_paper_roll_locations('2025/aoc_day_04.dat', paper_roll_locations)


def neighbors_are_rolls(row, col, rows, cols, paper_roll_locations):
    count = 0
    for delta_row in (-1, 0, 1):
        for delta_column in (-1, 0, 1):
            if delta_row == 0 and delta_column == 0:
                continue
            neighbor_row, neighbor_col = row + delta_row, col + delta_column
            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                if paper_roll_locations[neighbor_row][neighbor_col] == '@':
                    count += 1
    return count

def count_removable_rolls(paper_roll_locations):
    # Make a mutable copy of the grid: list of lists of characters
    grid = [list(row) for row in paper_roll_locations]

    rows = len(grid)
    cols = len(grid[0])

    total_removed = 0

    while True:
        rolls_to_remove = []

        # Find all accessible rolls in the *current* grid
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != '@':
                    continue
                if neighbors_are_rolls(row, col, rows, cols, grid) < 4:
                    rolls_to_remove.append((row, col))

        # If nothing is accessible this round, we're done
        if not rolls_to_remove:
            break

        # Remove them: turn those positions into '.'
        for row, col in rolls_to_remove:
            grid[row][col] = '.'

        # Keep track of how many we've removed in total
        total_removed += len(rolls_to_remove)

    return total_removed

removable_rolls = 0

removable_rolls = count_removable_rolls(paper_roll_locations)

print(f'removable_rolls: {removable_rolls}')