# You have a fast-food restaurant, and the food you are offering is previously prepared.
# Write a program that checks if you have enough food to serve lunch to all your customers. You also want to know who the client with the biggest order for that day is. 
# First, you will be given the quantity of the food you have for the day (an integer number). Next, you will be given a sequence of integers (separated by a single space),
# each representing the quantity of food in each order. Keep the orders in a queue.
# Find the biggest order and print it. Next, you will begin servicing your clients from the first one that came. Before each order, check if you have enough food left to 
# complete it:
# •	If you have, remove the order from the queue and reduce the quantity of food in the restaurant. 
# •	Otherwise, stop serving.


from collections import deque

food = int(input())
order_queue = deque(map(int, list(input().split())))
print(max(order_queue))

for _ in range(len(order_queue)):
    next_order = order_queue.popleft()
    if next_order > food:
        order_queue.appendleft(next_order)
        break
    else:
        food -= next_order

if len(order_queue) > 0:
    print(f"Orders left:", ' '.join(list(map(str, order_queue))))
else:
    print('Orders complete')
