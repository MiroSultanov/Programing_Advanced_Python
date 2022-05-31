def operate(operator, *args):
    result = args[0]

    calc = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b if b != 0 else a
    }

    for num in args[1:]:
        result = calc[operator](result, num)
    return result

# test_output

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
