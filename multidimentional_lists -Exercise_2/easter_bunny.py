# Your task is to collect as many eggs as possible.
# On the first line, you will be given a number representing the size of the field. On the following few lines, you will be given a field with:
# •	One bunny - randomly placed in it and marked with the symbol "B"
# •	Number of eggs placed at different positions of the field and traps marked with "X"
# Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs. The directions that should be considered as possible
# are up, down, left, and right. If you reach a trap while checking some of the directions, you should not consider the fields after the trap in this direction. 
# For more clarifications, see the examples below.
# Note: Consider ONLY the paths from which the bunny has collected 1 or more eggs.


matrix_size = int(input())
matrix = []

bunny_row = 0
bunny_col = 0

for row in range(matrix_size):
    row_elements = input().split()
    for col in range(matrix_size):
        if row_elements[col] == "B":
            bunny_row = row
            bunny_col = col
    matrix.append(row_elements)

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}

best_sum = float('-inf')
best_dir = ''
best_path = []

for direction in directions:
    current_sum = 0
    row, col = directions[direction](bunny_row, bunny_col)
    current_path = []

    while 0 <= row < matrix_size and 0 <= col < matrix_size and matrix[row][col] != "X":
        current_sum += int(matrix[row][col])
        current_path.append([row, col])
        row, col = directions[direction](row, col)

    if current_sum > best_sum:
        best_sum = current_sum
        best_dir = direction
        best_path = current_path

print(best_dir)
print(*best_path, sep='\n')
print(best_sum)
