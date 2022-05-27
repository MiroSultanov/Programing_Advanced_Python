# Write a program that finds the difference between the sums of the square matrix diagonals (absolute value). On the first line, you will receive an integer N - the size 
# of a square matrix. The following N lines hold the values for each column - N numbers separated by a single space. Print the absolute difference between 
# the primary and the secondary diagonal sums.

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
