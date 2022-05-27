rows, cols = [int(x) for x in input().split()]

chars = 'abcdefghijklmnopqrstuvwxyz'

for i in range(rows):
    row = [f'{chars[i]}{chars[j]}{chars[i]}' for j in range(i, cols + i)]
    print (*row, sep=' ')