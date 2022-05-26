# Write a program that reads a matrix from the console and prints the sum for each column on separate lines. 
# On the first line, you will get matrix sizes in format "{rows}, {columns}". On the next rows, you will get elements for each column separated with a single space. 


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
