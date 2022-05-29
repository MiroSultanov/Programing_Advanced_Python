# You are participating in a Firearm course. It is a training day at the shooting range.
# You will be given a matrix with 5 rows and 5 columns. It is a shotgun range represented as some symbols separated by a single space:
# •	Your position is marked with the symbol "A"
# •	Targets marked with symbol "x"
# •	All of the empty positions will be marked with "."
# After the field state, you will be given an integer representing the number of commands you will receive. The possible commands are:
# •	"move {right/left/up/down} {steps}" – you should move in the given direction with the given steps. You can only move if the field you want to step on is 
# marked with ".".
# •	"shoot {right/left/up/down}" – you should shoot in the given direction (from your current position without moving). Beware that there might be targets that 
# stand in the way of other targets, and you cannot reach them - you can shoot only the nearest target. When you have shot a target, the field becomes empty 
# position (".").
# Validate the positions since they can be outside the field.
# Keep track of all the shot targets:
# •	If at any point there are no targets left, end the program and print: "Training completed! All {count_targets} targets hit.". 
# •	If, after you perform all the commands, there are some targets left print: "Training not completed! {count_left_targets} targets left.".
# Finally, print the index positions of the targets that you hit, as shown in the examples.


def get_next_position(row, col, direction, steps):
    if direction == 'up':
        return row - steps, col
    if direction == 'down':
        return row + steps, col
    if direction == 'left':
        return row, col - steps
    if direction == 'right':
        return row, col + steps


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = 5

player_row = 0
player_col = 0
targets = 0

matrix = []

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == 'A':
            player_row = row
            player_col = col
        elif row_elements[col] == 'x':
            targets += 1
    matrix.append(row_elements)

n = int(input())

matrix[player_row][player_col] = '.'
hit_targets = []

for _ in range(n):
    command_parts = input().split()
    command = command_parts[0]
    direction = command_parts[1]

    if command == 'move':
        steps = int(command_parts[2])
        next_row, next_col = get_next_position(player_row, player_col, direction, steps)

        if is_inside(next_row, next_col, size) and matrix[next_row][next_col] == '.':
            player_row, player_col = next_row, next_col
    else:
        bullet_row, bullet_col = get_next_position(player_row, player_col, direction, 1)
        while is_inside(bullet_row, bullet_col, size):
            if matrix[bullet_row][bullet_col] == 'x':
                targets -= 1
                matrix[bullet_row][bullet_col] = '.'
                hit_targets.append([bullet_row, bullet_col])
                break
            bullet_row, bullet_col = get_next_position(bullet_row, bullet_col, direction, 1)
        if targets == 0:
            break

if targets == 0:
    print(f'Training completed! All {len(hit_targets)} targets hit.')
else:
    print(f'Training not completed! {targets} targets left.')

print(*hit_targets, sep='\n')
