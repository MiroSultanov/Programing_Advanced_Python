# You are learning how to make milkshakes.
# First, you will be given two sequences of integers representing chocolates and cups of milk.
# You have to start from the last chocolate and try to match it with the first cup of milk. If their values are equal, you should make a milkshake and remove both 
# ingredients. Otherwise, you should move the cup of milk at the end of the sequence and decrease the value of the chocolate by 5 without moving it from its position.
# If any of the values are equal to or below 0, you should remove them from the records right before mixing them with the other ingredient.
# When you successfully prepare 5 chocolate milkshakes, or you have no more chocolate or cups of milk left, you need to stop making chocolate milkshakes.


from collections import deque

chocolate_package = [int(x) for x in input().split(', ')]
milk_cups = deque([int(x) for x in input().split(", ")])

milkshakes = 0

while chocolate_package and milk_cups and milkshakes < 5:
    chocolate = chocolate_package.pop()
    milk = milk_cups.popleft()

    if chocolate <= 0 and milk <= 0:
        continue
    if chocolate <= 0:
        milk_cups.appendleft(milk)
        continue
    if milk <= 0:
        chocolate_package.append(chocolate)
        continue

    if chocolate == milk:
        milkshakes += 1
    else:
        milk_cups.append(milk)
        chocolate_package.append(chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate_package :
    print(f"Chocolate: {', '.join([str(x) for x in chocolate_package])}")
else:
    print("Chocolate: empty")

if milk_cups:
    print(f"Milk: {', '.join([str(x) for x in milk_cups])}")
else:
    print("Milk: empty")
