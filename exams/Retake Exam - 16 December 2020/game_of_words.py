move = {
    'up': lambda x: [x[0] - 1, x[1]],
    'down': lambda x: [x[0] + 1, x[1]],
    'left': lambda x: [x[0], x[1] - 1],
    'right': lambda x: [x[0], x[1] + 1]
}


def is_valid_cell(cell: tuple, matrix: list) -> bool:
    return min(cell) >= 0 and max(cell) < len(matrix)


def get_cell(cell: tuple, matrix: list) -> str:
    row, col = cell
    return str(matrix[row][col])


def set_cell(cell: tuple, matrix: list, value: str) -> None:
    row, col = cell
    matrix[row][col] = value


def main() -> None:
    initial_string = input()
    matrix = [[el for el in input()] for _ in range(int(input()))]
    p_cell = next(((x, y) for x in range(len(matrix)) for y in range(len(matrix)) if get_cell((x, y), matrix) == 'P'))

    for _ in range(int(input())):
        direction = input()
        new_cell = move[direction](p_cell)

        if is_valid_cell(new_cell, matrix):
            letter = get_cell(new_cell, matrix)
            set_cell(p_cell, matrix, '-')
            set_cell(new_cell, matrix, 'P')
            p_cell = new_cell
            if letter != '-':
                initial_string += letter

        elif len(initial_string) > 0:
            initial_string = initial_string[:-1]

    print(initial_string)
    for row in matrix:
        print(*row, sep='')


if __name__ == '__main__':
    main()