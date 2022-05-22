# Write a program that reads a text from the console and counts the occurrences of each character in it. Print the results in alphabetical (lexicographical) order.  

text = input()
symbols = {}

for char in text:
    if char in symbols:
        symbols[char] += 1
    else:
        symbols[char] = 1

for key, value in sorted(symbols.items()):
    print(f"{key}: {value} time/s")
