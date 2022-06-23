from collections import deque

customers = deque([int(x) for x in input().split(", ")])
taxis = deque([int(x) for x in input().split(", ")])
total_time = 0

while customers and taxis:
    if customers[0] <= taxis[-1]:
        total_time += customers.popleft()
        taxis.pop()
    else:
        taxis.pop()

if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(str(x) for x in customers)}",sep="")