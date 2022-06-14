# Write a program that prints the calculated logarithm of any given number
# Input
# •	On the first line, you will receive the number (an integer)
# •	On the second line, you will receive a number, which is the logarithm base. It can be either a number or the word "natural"
# The output should be formatted to the 2nd decimal digit


from math import log

value = int(input())
base = input()

if base == "natural":
    print(f"{log(value):.2f}")
else:
    print(f"{log(value, int(base)):.2f}")
