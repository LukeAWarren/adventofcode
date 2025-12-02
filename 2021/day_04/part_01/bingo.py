import pprint

bingo_numbers = []
bingo_boards = []

BOARD_SIZE = 5

with open('bingo_test.dat', 'r') as f:
    bingo_numbers_line = f.readline()
    bingo_numbers = [int(x) for x in list(bingo_numbers_line.split(','))]
    f.readline()
    while True:
        bingo_board = []
        for i in range(BOARD_SIZE):
            board_line = f.readline()
            bingo_board.append([[int(x), False] for x in list(board_line.strip().split())])
        bingo_boards.append(bingo_board)
        line = f.readline()
        if not line:
            break

print()

def mark_numbers(drawn_number, bingo_boards):
    for board in bingo_boards:
        for line in board:
            for position in line:
                if position[0] == drawn_number:
                    position[1] = True

def check_for_bingo(bingo_boards):
    for board in bingo_boards:
        for row in range(5):
            row_solved = True
            for column in range(BOARD_SIZE):
                position = board[row][column]
                if position[1] == False:
                    row_solved = False
            if row_solved:
                return board
        for column in range(BOARD_SIZE):
            column_solved = True
            for row in range(BOARD_SIZE):
                position = board[row][column]
                if position[1] == False:
                    column_solved = False
            if column_solved:
                return board

    return None

def sum_unmarked_numbers(board):
    sum = 0
    for line in board:
        for position in line:
            if position[1] == False:
                sum += position[0]
    return sum

for drawn_number in bingo_numbers:
    mark_numbers(drawn_number, bingo_boards)
    board = check_for_bingo(bingo_boards)
    if (board != None):
        for line in board:
            print(line)
        sum = sum_unmarked_numbers(board)
        print(f'sum: {sum}')
        print(f'solution = drawn_number X sum = {drawn_number * sum}')
        break


# # for board in bingo_boards:
# #     for line in board:
# #         print(line)
# #     print()
