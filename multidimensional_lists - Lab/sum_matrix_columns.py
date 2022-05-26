rows_count, column_count = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows_count):
    matrix.append(
        [int(x) for x in input().split(' ')]
    )

column_sum = [0] * column_count

for row_index in range(rows_count):
    for column_index in range(column_count):
        column_sum[column_index] += matrix[row_index][column_index]

[print(x) for x in column_sum]