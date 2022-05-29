# The presents are ready, and Santa has to deliver them to the kids. 
# You will receive an integer m for the number of presents Santa has and an integer n for the size of the neighborhood with a square shape. On the following lines, 
# you will receive the matrix, which represents the neighborhood. 
# Santa will be in a random cell, marked with the letter "S". Each cell stands for a house where children may live. If the cell has "X" on it, that means there lives
# a naughty kid. Otherwise, if a nice kid lives there, the cell is marked by "V". There can also be cells marked with "C" for cookies. All of the empty positions will 
# be marked with "-".
# Santa can move "up", "down", "left", "right" with one position each time. These will be the commands that you receive. If he moves to a house with a nice kid, the 
# kid receives a present, but if Santa reaches a house with a naughty kid, he doesn't drop a present. If the command sends Santa to a cell marked with "C", Santa eats 
# cookies and becomes happy and extra generous to all the kids around him* (meaning all of them will receive presents - it doesn't matter if naughty or nice). 
# If Santa has been to a house, the cell becomes "-".
# Note: *around him means on his left, right, upwards, and downwards by one cell. In this case, Santa doesn't move to these cells, or if he does, he returns to 
# the cell where the cookie was. If Santa runs out of presents or receives the command "Christmas morning", you should end the program. 
# Keep in mind that you should check whether all the nice kids received presents.


def get_next_post(row, col, direction):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_around_kids(matrix, row, col):
    result = []
    if is_inside(row, col - 1, len(matrix)) and matrix[row][col - 1] == 'X' or matrix[row][col - 1] == 'V':
        result.append([row, col - 1])
    if is_inside(row, col + 1, len(matrix)) and matrix[row][col + 1] == 'X' or matrix[row][col + 1] == 'V':
        result.append([row, col + 1])
    if is_inside(row - 1, col, len(matrix)) and matrix[row - 1][col] == 'X' or matrix[row - 1][col] == 'V':
        result.append([row - 1, col])
    if is_inside(row + 1, col, len(matrix)) and matrix[row + 1][col] == 'X' or matrix[row + 1][col] == 'V':
        result.append([row + 1, col])

    return result


gifs = int(input())
size = int(input())
matrix = []
santa_row = 0
santa_col = 0
nice_kids = 0

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == 'S':
            santa_row = row
            santa_col = col
        elif row_elements[col] == 'V':
            nice_kids += 1
    matrix.append(row_elements)

nice_kids_gifted = 0

while gifs > 0:
    line = input()
    if line == 'Christmas morning':
        break

    matrix[santa_row][santa_col] = '-'
    santa_row, santa_col = get_next_post(santa_row, santa_col, line)

    if matrix[santa_row][santa_col] == 'V':
        gifs -= 1
        nice_kids_gifted += 1
    elif matrix[santa_row][santa_col] == 'C':
        around_kids = get_around_kids(matrix, santa_row, santa_col)
        for kid_row, kid_col in around_kids:
            if matrix[kid_row][kid_col] == 'V':
                nice_kids_gifted += 1
            gifs -= 1
            matrix[kid_row][kid_col] = '-'
            if gifs == 0:
                break
    matrix[santa_row][santa_col] = 'S'

if nice_kids_gifted != nice_kids and gifs == 0:
    print(f'Santa ran out of presents!')

for row in matrix:
    print(*row, sep=" ")

if nice_kids_gifted == nice_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - nice_kids_gifted} nice kid/s.")
