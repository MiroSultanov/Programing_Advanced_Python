# You will be given a square matrix of integers, each integer separated by a single space, and each row will be on a new line. On the last line of input, 
# you will receive indexes - coordinates of several cells separated by a single space, in the following format: "{row1},{column1} {row2},{column2} … {row3},{column3}".
# On those cells, there are bombs. You must detonate every bomb in the order they were given. When a bomb explodes, it deals damage equal to its integer value to 
# all the cells around it (in every direction and in all diagonals). One bomb can't explode more than once, and after it does, its value becomes 0. 
# When a cell's value reaches 0 or below, it dies. Dead cells can't explode.
# You must print the count of all alive cells and their sum. Afterward, print the matrix with all its cells (including the dead ones).


def get_children(matrix, row, col):
    possible_children_cords = [
        [row - 1, col - 1],
        [row - 1, col],
        [row - 1, col + 1],
        [row, col - 1],
        [row, col + 1],
        [row + 1, col - 1],
        [row + 1, col],
        [row + 1, col + 1]
    ]

    result = []
    for child_row, child_col in possible_children_cords:
        if 0 <= child_row < len(matrix) and 0 <= child_col < len(matrix) and matrix[child_row][child_col] > 0:
            result.append([child_row, child_col])
    return result


size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

bombs = input().split()

for bomb in bombs:
    row, col = [int(x) for x in bomb.split(',')]
    power = matrix[row][col]

    if power <= 0:
        continue

    matrix[row][col] = 0

    children = get_children(matrix, row, col)
    for child_row, child_col in children:
        matrix[child_row][child_col] -= power

alive_cells_count = 0
alive_cells_sum = 0

for row in matrix:
    for el in row:
        if el > 0:
            alive_cells_count += 1
            alive_cells_sum += el

print(f'Alive cells: {alive_cells_count}')
print(f'Sum: {alive_cells_sum}')
for row in matrix:
    print(*row, sep=' ')
