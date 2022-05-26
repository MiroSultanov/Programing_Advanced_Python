number_of_rows = int(input())
matrix = []

for _ in range(number_of_rows):
    row = [int(x) for x in input().split(', ')]
    matrix.append(
        [int(x) for x in row if x % 2 == 0]
    )

print(matrix)