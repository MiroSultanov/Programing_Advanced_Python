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