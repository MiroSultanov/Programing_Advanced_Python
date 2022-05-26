number_of_rows = int(input())
matrix = []

for _ in range(number_of_rows):
    row = [int(x) for x in input().split(', ')]
    matrix.extend(row)

print(matrix)