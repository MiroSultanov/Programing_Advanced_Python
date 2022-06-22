# You will be given a chess board (8x8). On the board there will be 3 types of symbols:
# •	"." – empty square
# •	"Q" – a queen
# •	"K" – the king
# Your job is to find which queens can capture the king and print them. The moves that the queen can do is to move diagonally, horizontally and vertically 
# (basically all the moves that all the other figures can do except from the knight). Beware that there might be queens that stand in the way of other queens 
# and can stop them from capturing the king. For more clarification see the examples.
# Input
# •	8 lines – the state of the board (each square separated by single space)
# Output
# •	The positions of the queens that can capture the king as lists
# •	If the king cannot be captured, print: "The king is safe!"
# •	The order of output does not matter
# Constrains
# •	There will always be exactly 8 lines
# •	There will always be exactly one King
# •	Only the 3 symbols described above will be present in the input


def is_inside(row, col, matrix_size):
    return 0 <= row < matrix_size and 0 <= col < matrix_size

matrix_size = 8
matrix = []

for _ in range(matrix_size):
    matrix.append(input().split())

movement = {
    "up": lambda row, col: (row - 1, col),
    "down": lambda row, col: (row + 1, col),
    "left": lambda row, col: (row, col - 1),
    "right": lambda row, col: (row, col + 1),
    "up-right": lambda row, col: (row - 1, col + 1),
    "up-left": lambda row, col: (row - 1, col - 1),
    "down-right": lambda row, col: (row + 1, col + 1),
    "down-left": lambda row, col: (row + 1, col - 1)
}

player_path = []

for row in range(matrix_size):
    for col in range(matrix_size):
        if matrix[row][col] == "Q":
            for move in movement:
                next_row, next_col = movement[move](row, col)
                while is_inside(next_row, next_col, matrix_size):
                    if matrix[next_row][next_col] == "Q":
                        break
                    if matrix[next_row][next_col] == "K":
                        player_path.append([row, col])
                        break
                    next_row, next_col = movement[move](next_row, next_col)
if len(player_path) == 0:
    print("The king is safe!")
else:
    print(*player_path, sep="\n")
