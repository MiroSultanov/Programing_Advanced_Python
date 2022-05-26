result = 0

for i in range(int(input())):
    row = [int(x) for x in input().split()]
    result += row[i]

print(result)