def shopping_cart(*args):
    number_of_meals = {
        'Soup': 3,
        'Pizza': 4,
        'Dessert': 2
    }
    meal_types = {
        'Soup': [],
        'Pizza': [],
        'Dessert': []
    }
    shopping_card = 0
    for couple in args:
        if couple == 'Stop':
            break
        meal, product = couple
        shopping_card += 1
        number_of_meals[meal] -= 1
        if meal in meal_types and number_of_meals[meal] >= 0:
            meal_types[meal].append(product)

    result = ''
    sorted_meals_types = (sorted(meal_types.items(), key=lambda x: (-len(x[1]), x[0])))
    if shopping_card == 0:
        result += 'No products in the cart!'
    else:
        for meal, product in sorted_meals_types:
            product_result = [f" - {pro}\n" for pro in sorted(set(product))]
            result += f'{meal}:\n'
            result += f"{''.join(product_result)}"

    return result



print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))


# VARIANT II

def shopping_cart(*args):
    meals_count = {
        'Soup': 3,
        'Pizza': 4,
        'Dessert': 2,
    }
    meals = {
        'Soup': [],
        'Pizza': [],
        'Dessert': [],
    }

    for info in args:
        if info == 'Stop':
            break

        meal = info[0]
        product = info[1]

        if product not in meals[meal]:
            if len(meals[meal]) < meals_count[meal]:
                meals[meal].append(product)

    output = list()
    if not meals['Dessert'] and not meals['Pizza'] and not meals['Soup']:
        output.append(f'No products in the cart!')
    else:
        for key, value in sorted(meals.items(), key=lambda x: (-len(x[1]), x[0])):
            output.append(f'{key}:')
            if value:
                for item in sorted(value):
                    output.append(f' - {item}')

    return '\n'.join(output)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))