# We think the process of making honey is amazing! Let's learn more about how bees make honey.
# Worker-bees collect nectar. When a worker-bee has found enough nectar, she returns to the hive to drop off the load and pass the nectar to waiting bees 
# so they can really start the honey-making process. 
# You will receive 3 sequences:
# •	a sequence of integers, representing working bees
# •	a sequence of integers, representing nectar
# •	a sequence of symbols – "+", "-", "*" or "/", representing the honey-making process.
# Your task is to check if the bee has collected enough nectar to return to the hive and keep track of the total honey waiting bees made with the collected nectar.
# Step one: check if a bee has collected enough nectar. You should take the first bee and try to match it with the last nectar:
# •	If the nectar value is more or equal to the value of the bee, it is considered collected, and the bee returns to the hive to drop off the load (step two).
# •	If the nectar value is less than the value of the bee, you should remove the nectar and try to match the bee with the next nectar's value until the bee 
# collects enough nectar.
# Step two: When a bee successfully collects nectar, she returns to the hive, and you should calculate the honey made. Take the first symbol in the 
#     sequence of symbols ("+", "-", "*" or "/") and make the corresponding calculation:
# "{matched_bee} {symbol} {matched_nectar}"
# The result represents the honey that is made from the passed nectar. The calculation should always return the absolute value of the result. 
# After the calculation, remove the bee, the nectar, and the symbol. Stop making honey when you are out of bees or nectar.


from collections import deque

bees = deque([int(x) for x in input().split()])
nectars = [int(x) for x in input().split()]
symbols = deque(input().split())

honey = 0

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}

while bees and nectars:
    bee = bees.popleft()
    nectar = nectars.pop()

    if nectar < bee:
        bees.appendleft(bee)
        continue

    if nectar == 0:
        continue

    operator = symbols.popleft()
    honey += abs(operations[operator](bee, nectar))
print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")

if nectars:
    print(f"Nectar left: {', '.join([str(x) for x in nectars])}")
