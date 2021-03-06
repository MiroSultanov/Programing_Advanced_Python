# Create a function called even_odd() that can receive a different quantity of numbers and a command at the end. The command can be "even" or "odd". 
# Filter the numbers depending on the command and return them in a list.

def even_odd(*args):
    filter_command = args[-1]
    parity = 0 if filter_command == 'even' else 1
    result = []

    for index in range(len(args) - 1):
        number = args[index]
        if number % 2 == parity:
            result.append(number)
    return result

# test_output
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

