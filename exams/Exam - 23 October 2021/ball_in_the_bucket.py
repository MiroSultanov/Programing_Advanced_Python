def get_cell(cell: tuple, matrix: list) -> str:
    row, col = cell
    return matrix[row][col]


def set_cell(cell: tuple, matrix: list, value: int) -> None:
    row, col = cell
    matrix[row][col] = value


def is_valid_cell(cell: tuple, matrix_size: int) -> bool:
    return min(cell) >= 0 and max(cell) < matrix_size


def get_col_value(cell: tuple, matrix: list) -> int:
    row, col = cell
    retval = 0
    for i in range(len(matrix)):
        if i != row:
            val = get_cell((i, col), matrix)
            if val.isnumeric():
                retval += int(val)

    return retval


def main() -> None:
    prices = {
        1: 'Football',
        2: 'Teddy Bear',
        3: 'Lego Construction Set'
    }
    pts = 0
    matrix = [[el for el in input().split()] for _ in range(6)]

    for _ in range(3):
        cell = tuple(map(int, input().replace('(', '').replace(')', '').split(', ')))
        if not is_valid_cell(cell, len(matrix)):
            continue

        value = get_cell(cell, matrix)

        if value == 'B':
            pts += get_col_value(cell, matrix)
            set_cell(cell, matrix, 0)

    if pts < 100:
        print(f"Sorry! You need {100 - pts} points more to win a prize.")
    elif pts > 400:
        print(f"Good job! You scored {pts} points, and you've won Lego Construction Set.")
    else:
        print(f"Good job! You scored {pts} points, and you've won {prices.get(pts//100)}.")


if __name__ == '__main__':
    main()