# Your rover has landed on Mars, and it needs to find resources to start humanity's first interplanetary colony.
# You will receive a 6x6 field on separate lines with:
# •	One rover - marked with the letter "E"
# •	Water deposit (one or many) - marked with the letter "W"
# •	Metal deposit (one or many) - marked with the letter "M"
# •	Concrete deposit (one or many) - marked with the letter "C"
# •	Rock (one or many) - marked with the letter "R"
# •	Empty positions will be marked with "-"
# After that, you will be given the commands for the rover's movement on one line separated by a comma and a space (", "). Commands can be: "up", "down", "left", 
# or "right".
# For each command, the rover moves in the given directions with one step, and it can land on one of the given types of deposit or a rock:
# •	When it lands on a deposit, you must print the coordinates of that deposit in the format shown below and increase its value by 1.
# •	If the rover lands on a rock, it gets broken. Print the coordinates where it got broken in the format shown below, and the program ends.
# •	If the rover goes out of the field, it should continue from the opposite side in the same direction. Example: If the rover is at position (3, 0) and it
#     needs to move left (outside the matrix), it should be placed at position (3, 5).
# The rover needs to find at least one of each deposit to consider the area suitable to start our colony. 
# Stop the program if you run out of commands or the rover gets broken.


def validate_cell(cell: tuple) -> tuple:
    x, y = cell
    if x == 6:
        x = 0
    elif x == -1:
        x = 5
    if y == 6:
        y = 0
    elif y == -1:
        y = 5
    return x, y


def get_cell(cell: tuple, field: list) -> str:
    row, col = cell
    return field[row][col]


def set_cell(cell: tuple, field: list, value: int) -> None:
    row, col = cell
    matrix[row][col] = value


move = {
    'up': lambda x: (x[0]-1, x[1]),
    'down': lambda x: (x[0]+1, x[1]),
    'left': lambda x: (x[0], x[1]-1),
    'right': lambda x: (x[0], x[1]+1)
}


deposits = {
    'W': ['Water', 0],
    'M': ['Metal', 0],
    'C': ['Concrete', 0]
}


matrix = [[x for x in input().split(' ')] for _ in range(6)]
current_position = next((x, y) for x in range(6) for y in range(6) if matrix[x][y] == 'E')
commands = input().split(', ')

for command in commands:
    next_position = move[command](current_position)
    next_position = validate_cell(next_position)
    row, col = next_position
    item_at_cell = get_cell(next_position, matrix)
    if item_at_cell in ('W', 'M', 'C'):
        deposits[item_at_cell][1] += 1
        print(f"{deposits[item_at_cell][0]} deposit found at ({row}, {col})")
        set_cell(current_position, matrix, '-')
        set_cell(next_position, matrix, 'E')
    elif item_at_cell == 'R':
        print(f"Rover got broken at ({row}, {col})")
        break
    current_position = next_position

if deposits['W'][1] > 0 and deposits['C'][1] > 0 and deposits['M'][1] > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
