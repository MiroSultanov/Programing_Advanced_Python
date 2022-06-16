# You will be given two sequences of integers representing bowls of ramen and customers. Your task is to find out if you can serve all the customers.
# Start by taking the last bowl of ramen and the first customer. Try to serve every customer with ramen until we have no more ramen or customers left:
# •	Each time the value of the ramen is equal to the value of the customer, remove them both and continue with the next bowl of ramen and the next customer.
# •	Each time the value of the ramen is bigger than the value of the customer, decrease the value of that ramen with the value of that customer and remove the 
# customer. Then try to match the same bowl of ramen (which has been decreased) with the next customer.
# •	Each time the customer's value is bigger than the value of the ramen bowl, decrease the value of the customer with the value of the ramen bowl and remove the bowl. Then try to match the same customer (which has been decreased) with the next bowl of ramen.
# Look at the examples provided for a better understanding of the problem.


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
