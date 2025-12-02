import pprint

bingo_numbers = []
bingo_boards = []
SIZE_OF_BINGO_BOARDS = 5

with open('bingo_example.dat', 'r') as f:
    bingo_numbers = [int(x) for x in f.readline().strip().split(',')]
    print(bingo_numbers)
    while True:
        line = f.readline()
        if not line:
            break
        board = []
        for ndx in range(5):
            row = [[int(x), False] for x in f.readline().strip().split()]
            board.append(row)
        bingo_boards.append(board)
        print()
        pprint.pprint(board)

def mark_boards(drawn_number, bingo_boards):
    for board in bingo_boards:
        for row in board:
            for square in row:
                if (square[0] == drawn_number):
                    square[1] = True

def check_rows_for_bingo(board):
    for row in range(SIZE_OF_BINGO_BOARDS):
        solved = True
        for column in range(SIZE_OF_BINGO_BOARDS):
            if board[row][column][1] == False:
                solved = False
                break
        if solved == True:
            return True
    return False

def check_columns_for_bingo(board):
    for column in range(SIZE_OF_BINGO_BOARDS):
        solved = True
        for row in range(SIZE_OF_BINGO_BOARDS):
            if board[row][column][1] == False:
                solved = False
                break
        if solved == True:
            return True
    return False

def find_solved_board(bingo_boards):
    for board in bingo_boards:
        if check_rows_for_bingo(board) == True:
            return board
        if check_columns_for_bingo(board) == True:
            return board
    return None

def sum_unmarked_squares(board):
    sum = 0
    for row in board:
        for square in row:
            if square[1] == False:
                sum += square[0]
    return sum

last_drawn_number = None
last_solved_board = None

for drawn_number in bingo_numbers:
    mark_boards(drawn_number, bingo_boards)
    solved_board = find_solved_board(bingo_boards)
    if solved_board != None:
        bingo_boards.remove(solved_board)
        print(f'num boards remaining: {len(bingo_boards)}')
        print('solved board:')
        pprint.pprint(solved_board)
        sum = sum_unmarked_squares(solved_board)
        print(f'solution key = sum X last drawn number = {sum * drawn_number}')
    # if solved_board != None:
    #     last_drawn_number = drawn_number
    #     last_solved_board = solved_board
    #     #print('removing board:')
    #     #pprint.pprint(solved_board)
    #     bingo_boards.remove(last_solved_board)
    #     print(f'{len(bingo_boards)} boards remaining')

#pprint.pprint(bingo_boards)

# print('final solved board:')
# pprint.pprint(last_solved_board)
# sum = sum_unmarked_squares(last_solved_board)
# print(f'final drawn number: {last_drawn_number}')
# print(f'sum of unmarked square: {sum}')
# print(f'solution key = sum X last drawn number = {sum * last_drawn_number}')
