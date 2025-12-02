import os

word_search_puzzle = []
WORD_TO_FIND = "MAS"
def load_data(file_name, word_search_puzzle):
    f = open(file_name)
    for line in f.readlines():
        word_search_puzzle.append(list(line.strip()))

def match_word_at_position(word_at_position, word_to_find):
    # match word
    if word_to_find == word_at_position:
        return True
    # match word reversed
    if word_to_find[::-1] == word_at_position:
        return True
    return False

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
            if col_pos >= 0 and col_pos < len(word_search_puzzle):
               word_at_position += word_search_puzzle[row_pos][col_pos]
    return match_word_at_position(word_at_position, word_to_find)

load_data('aoc_day_04_part_2.dat', word_search_puzzle)

count = 0
for row in range(0, len(word_search_puzzle)):
    for col in range(0, len(word_search_puzzle[row])):
        found_down_right = diag_down_right(word_search_puzzle, WORD_TO_FIND, row, col)
        found_down_left = diag_down_left(word_search_puzzle, WORD_TO_FIND, row, col + len(WORD_TO_FIND) - 1)
        if (found_down_right and found_down_left):
            count += 1

print(count)