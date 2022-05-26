
sum_elements = 0
rows, cols = [int(x) for x in input().split(', ')]

matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

for i in range(rows -1):
    for j in range(cols - 1):
        sub_matrix = [[matrix[i + x][j + y] for y in range(2)] for x in range(2)]
        temp_sum = sum([x for y in sub_matrix for x in y])
        if temp_sum > sum_elements:
            sum_elements = temp_sum
            output = sub_matrix.copy()

for row in output:
    print(*row, sep=' ')

print (sum_elements)
