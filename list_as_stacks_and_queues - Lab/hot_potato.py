# Hot Potato is a game in which children form a circle and toss a hot potato. The counting starts with the first kid. Every nth toss, the child holding the potato 
# leaves the game. When a kid leaves the game, it passes the potato to the next kid. It continues until there is only one kid left.
# Create a program that simulates the game of Hot Potato. On the first line, you will receive kids' names, separated by a single space. On the second line, you 
# will receive the nth toss (integer) in which a child leaves the game. Print every kid who is removed from the circle in the format "Removed {kid}". 
# In the end, print the only kid left in the format "Last is {kid}".


from collections import deque

kids_string = input()
tosses_count_string = input()

kids = deque(kids_string.split(' '))
tosses_count = int(tosses_count_string)

current_count = 0
while len(kids) > 1:
    current_count += 1

    kid = kids.popleft()

    if current_count < tosses_count:
        kids.append(kid)
    else:
        print(f'Removed {kid}')
        current_count = 0

print(f'Last is {kids.popleft()}')
