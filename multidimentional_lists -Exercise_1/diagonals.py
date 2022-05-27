# Using a nested list comprehension, write a program that reads rows of a square matrix and its elements, separated by a comma and a space ", ". 
# You should find the matrix's diagonals, prints them and their sum in the format:
# "Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
# Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}".


number_of_elements = int(input())
matrix = []

for _ in range(number_of_elements):
    matrix.append([int(x) for x in input().split(', ')])

primary_diagonal = []
secondary_diagonal = []

for index in range(number_of_elements):
    primary_diagonal.append(matrix[index][index])
    secondary_diagonal.append(matrix[index][number_of_elements - 1 - index])

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
