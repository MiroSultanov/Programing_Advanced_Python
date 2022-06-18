def shopping_list(budget: int, **kwargs):
    if budget < 100:
        return "You do not have enough budget."

    basket = []

    for name, value in kwargs.items():
        cost = float(value[0]) * int(value[1])

        if cost <= budget:
            budget -= cost
            basket.append((name, cost))

        if budget == 0 or len(basket) == 5:
            break

    output = ''

    for item in basket:
        output += f"You bought {item[0]} for {item[1]:.2f} leva.\n"

    return output

# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))

# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))





