# Write program that:
# •	Reads an input string
# •	Reverses it using a stack
# •	Prints the result back on the console


string = input()

s = []

for c in string:
    s.append(c)

reversed_string = ""
while s:
    reversed_string += s.pop()

print(reversed_string)
