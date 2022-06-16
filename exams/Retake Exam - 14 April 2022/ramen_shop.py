from collections import deque

bowls_of_ramen = deque([int(x) for x in input().split(", ")])
customers = deque([int(x) for x in input().split(", ")])

while bowls_of_ramen and customers:
    bow = bowls_of_ramen.pop()
    client = customers.popleft()

    if bow == client:
        continue

    elif bow > client:
        bow -= client
        bowls_of_ramen.append(bow)

    elif client > bow:
        client -= bow
        customers.appendleft(client)

if not customers:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        bowls_left = ', '.join([str(el) for el in bowls_of_ramen])
        print(f"Bowls of ramen left: {bowls_left}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    clients_left = ', '.join([str(el) for el in customers])
    print(f"Customers left: {clients_left}")