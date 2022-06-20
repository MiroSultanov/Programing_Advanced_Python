from collections import deque


def stock_availability(boxes: list, delivery_sell: str, *args):
    inventory = deque(boxes)

    if delivery_sell == "delivery":
        inventory.extend(arg for arg in args)

    elif delivery_sell == "sell":
        if inventory and not args:
            inventory.popleft()

        elif len(args) == 1 and type(args[0]) == int:
            for _ in range(int(args[0])):
                if inventory:
                    inventory.popleft()

        else:
            for arg in args:
                while inventory and arg in inventory:
                    inventory.remove(arg)

    return [el for el in inventory]

print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
