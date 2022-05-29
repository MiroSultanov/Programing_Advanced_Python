# Chess is the oldest game, but it is still popular these days. It will be used only one chess piece for this task - the Knight. 
# A chess knight has 8 possible moves it can make, as illustrated. It can move to the nearest square but not on the same row, column, or diagonal. 
# (e.g., it can move two squares horizontally, then one square vertically, or it can move one square horizontally then two squares vertically - i.e., in an "L" pattern.) 
# The knight game is played on a board with dimensions N x N.
# You will receive a board with "K" for knights and "0" for empty cells. Your task is to remove knights until no knights that can attack one another with 
# one move are left.


def find_counter(board, row, col):
    moves = [
        [row - 2, col - 1],
        [row - 2, col + 1],
        [row - 1, col - 2],
        [row - 1, col + 2],
        [row + 1, col - 2],
        [row + 1, col + 2],
        [row + 2, col - 1],
        [row + 2, col + 1]
    ]
    result = 0

    for r, c in moves:
        if 0 <= r < len(board) and 0 <= c < len(board) and board[r][c] == "K":
            result += 1
    return result

matrix_size = int(input())
board = []

for _ in range(matrix_size):
    board.append(list(input()))

removed_knights = 0

while True:
    best_count = 0
    knight_row = 0
    knight_col = 0

    for row in range(matrix_size):
        for col in range(matrix_size):
            if board[row][col] == "0":
                continue
            count = find_counter(board, row, col)
            if count > best_count:
                best_count = count
                knight_row = row
                knight_col = col

    if best_count == 0:
        break

    board[knight_row][knight_col] = '0'
    removed_knights += 1

print(removed_knights)


