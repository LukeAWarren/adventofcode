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

def count_accessible_rolls(paper_roll_locations):
    rows = len(paper_roll_locations) # get the height of the grid
    cols = len(paper_roll_locations[0]) # get the width of the grid

    accessible = 0
    for row in range(rows):
        for col in range(cols):
            if paper_roll_locations[row][col] != '@':
                continue
            if neighbors_are_rolls(row, col, rows, cols, paper_roll_locations) < 4:
                accessible += 1

    return accessible

accessible_rows = 0


accessible_rows = count_accessible_rolls(paper_roll_locations)

print(f'accessible_rows: {accessible_rows}')