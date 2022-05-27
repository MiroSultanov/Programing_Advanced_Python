number_of_element = int(input())
matrix = []

for _ in range(number_of_element):
    matrix.append([int(x) for x in input().split()])

primary_diagonal = []
secondary_diagonal = []

for index in range(number_of_element):
    primary_diagonal.append(matrix[index][index])
    secondary_diagonal.append(matrix[index][number_of_element - 1 - index])

primary_sum = sum(primary_diagonal)
secondary_sum = sum(secondary_diagonal)

print(abs(primary_sum - secondary_sum))