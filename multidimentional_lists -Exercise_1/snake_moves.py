# You are tasked to visualize a snake's zigzag path in a rectangular matrix with a size N x M. 
# A string represents the snake. It starts moving from the top-left corner to the right. When the snake reaches the end of the row, it slithers its way down to 
# the next row and turns left. The moves are repeated to the very end. 
# The first cell is filled with the first symbol of the snake. The second cell is filled with the second symbol, etc. The snake's path is as long as it takes to
# fill the matrix completely - if you reach the end of the string representing the snake, start again at the first symbol. In the end, you should print the snake's path.


rows, columns = [ int(x) for x in input().split()]
word = input()
index = 0

for row in range(rows):
    elements = [None] * columns

    if row % 2 == 0:
        for col in range(columns):
            elements[col] = word[index % len(word)]
            index += 1
    else:
        for col in range(columns -1, -1, -1):
            elements[col] = word[index % len(word)]
            index += 1
    print("".join(elements))
