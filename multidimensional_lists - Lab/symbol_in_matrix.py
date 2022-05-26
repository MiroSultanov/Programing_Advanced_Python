number = int(input())
matrix = [list(input()) for _ in range(number)]
symbol = input()
is_found = False

for row_index in range(number):
    for column_index in range(number):
        if matrix[row_index][column_index] == symbol:
            is_found = True
            print(f"({row_index}, {column_index})")
            break

if not is_found:
    print(f"{symbol} does not occur in the matrix")