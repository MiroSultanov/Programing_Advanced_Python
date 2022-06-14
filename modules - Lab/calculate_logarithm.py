from math import log

value = int(input())
base = input()

if base == "natural":
    print(f"{log(value):.2f}")
else:
    print(f"{log(value, int(base)):.2f}")