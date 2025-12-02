import os

word_search_puzzle = []
WORD_TO_FIND = "XMAS"
def load_data(file_name, word_search_puzzle):
    f = open(file_name)
    for line in f.readlines():
        word_search_puzzle.append(list(line.strip()))

def match_word_at_position(word_at_position, word_to_find):
    count = 0
    # match word
    if word_to_find == word_at_position:
        count += 1
    # match word reversed
    if word_to_find[::-1] == word_at_position:
        count += 1
    return count

def hor(word_search_puzzle, word_to_find, row, col):
    starting_pos = col
    ending_pos = starting_pos + len(word_to_find)
    word_at_position = "".join(word_search_puzzle[row][starting_pos:ending_pos])
    return match_word_at_position(word_at_position, word_to_find)

def ver(word_search_puzzle, word_to_find, row, col):
    starting_row = row
    ending_row = starting_row + len(word_to_find)
    word_at_position = ""
    for current_row in range(starting_row, ending_row):
        if (current_row < len(word_search_puzzle[starting_row])):
            word_at_position += word_search_puzzle[current_row][col]
    return match_word_at_position(word_at_position, word_to_find)


def diag_down_right(word_search_puzzle, word_to_find, row, col):
    word_at_position = ""
    for current_pos in range(0, len(word_to_find)):
        if (row + current_pos) < len(word_search_puzzle[row]):
            if (col + current_pos) < len(word_search_puzzle):
                word_at_position += word_search_puzzle[row + current_pos][col + current_pos]
    return match_word_at_position(word_at_position, word_to_find)

def diag_down_left(word_search_puzzle, word_to_find, row, col):
    word_at_position = ""
    word_length = len(word_to_find)
    for current_pos in range(0, word_length):
        row_pos = row + current_pos
        col_pos = col - current_pos
        if row_pos < len(word_search_puzzle):
            if col_pos >= 0:
               word_at_position += word_search_puzzle[row_pos][col_pos]
    return match_word_at_position(word_at_position, word_to_find)

load_data('aoc_day_04_part_1.dat', word_search_puzzle)

count = 0
for row in range(0, len(word_search_puzzle)):
    for col in range(0, len(word_search_puzzle[row])):
        count += hor(word_search_puzzle, WORD_TO_FIND, row, col)
        count += ver(word_search_puzzle, WORD_TO_FIND, row, col)
        count += diag_down_right(word_search_puzzle, WORD_TO_FIND, row, col)
        count += diag_down_left(word_search_puzzle, WORD_TO_FIND, row, col)

print(count)