from collections import deque


pizza_orders = deque([int(x) for x in input().split(', ')])
employees = deque([int(x) for x in input().split(', ')])
pizzas = 0

while pizza_orders and employees:
    order = pizza_orders.popleft()
    if order > 10 or order <= 0:
        continue

    employee = employees.pop()

    if employee >= order:
        pizzas += order

    elif order > employee:
        order -= employee
        pizzas += employee
        while order > 0 and employees:
            employee = employees.pop()
            order -= employee
            pizzas += employee
        else:
            if order <= 0:
                pizzas += order
            else:
                pizza_orders.appendleft(order)

if pizza_orders:
    print('Not all orders are completed.')
    print('Orders left:', ', '.join([str(el) for el in pizza_orders]))
else:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {pizzas}')
    print(f'Employees:', ', '.join([str(x) for x in employees]))