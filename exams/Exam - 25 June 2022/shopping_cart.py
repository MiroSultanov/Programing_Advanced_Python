# Write a function called shopping_cart that adds products to a shopping cart for the following three types of meals:  "Soup", "Pizza", and "Dessert". 
#     Every meal has a limit of products that can be added to it:
# •	Soup: 3
# •	Pizza: 4
# •	Dessert: 2
# Once you reach the limit of a meal, you should stop adding products to that meal.
# The function will receive a different number of arguments. The arguments will be passed as tuples with two elements - the first one is the type of meal, 
# and the second is the product for the meal. You need to take each argument and make a dictionary with the meal's name as a key and the products as a value of the corresponding key.
# There are some additional requirements:
# •	If you receive the same product for the same meal more than once, you must not add it again.
# •	If you run into the word "Stop" (not tuple) as an argument, you must immediately stop adding products to the cart - just sort and return the desired 
# result as described below.
# In the end, sort the meals by the number of bought products in descending order. If there are meals with an equal number of products, sort them (the meals) 
# by their name in ascending order (alphabetically). For each meal sort its products in ascending order (alphabetically).
# Return an output as described below.
# Note: Submit only the function in the judge system
# Input
# •	There will be no input, just parameters passed to your function
# Output
# •	Return a string for each of the 3 types of a meal of the sorted result in the format:
# o	"{meal_type}:"
# " - {first_product_added}"
# " - {second_product_added}"
#  …
# " - {Nth_product_added}"
# o	If there are no products given for a meal, return just its name in the format shown above.
# •	If there are NO products in the cart (at all), return the message: "No products in the cart!"


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
