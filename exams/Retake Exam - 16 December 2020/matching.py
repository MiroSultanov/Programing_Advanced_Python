from collections import deque

males = deque([int(x) for x in input().split(" ")])
females = deque([int(x) for x in input().split(" ")])
matches = 0

while males and females:
    m = males.pop()
    if m % 25 == 0 or m <= 0:
        if m % 25 == 0 and m != 0 and males:
            males.pop()
        continue
    f = females.popleft()
    if f % 25 == 0 or f <= 0:
        if f % 25 == 0 and f != 0 and females:
            females.popleft()
        males.append(m)
        continue

    if m == f:
        matches += 1
    else:
        males.append(m - 2)

print(f"Matches: {matches}")

if males:
    print(f"Males left: {', '.join(reversed([str(x) for x in males]))}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join([str(x) for x in females])}")
else:
    print("Females left: none")

