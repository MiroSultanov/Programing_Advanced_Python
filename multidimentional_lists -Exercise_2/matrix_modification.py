# Write a program that reads a matrix from the console and changes its values. On the first line, you will get the matrix's rows - N. You will get elements for 
# each column on the following N lines, separated with a single space. You will be receiving commands in the following format:
# •	"Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
# •	"Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
# If the coordinate is invalid, you should print "Invalid coordinates". A coordinate is valid if both of the given indexes are in range [0; len() – 1].
# When you receive "END", you should print the matrix and stop the program.


matrix_size = int(input())
matrix = []

for _ in range(matrix_size):
    matrix.append([int(x) for x in input().split()])

while True:
    line = input()
    if line == "END":
        break

    parts = line.split()
    command = parts[0]
    row, col, value = [int(x) for x in parts[1:]]

    if row < 0 or col < 0 or row >= matrix_size or col >= matrix_size:
        print("Invalid coordinates")
        continue

    if command == "Add":
        matrix[row][col] += value
    else:
        matrix[row][col] -= value

for row in matrix:
    print(*row, sep=' ')
