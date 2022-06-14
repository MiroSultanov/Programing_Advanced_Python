def perform_operation(sign, *args):
    if sign == '+':
        return sum(args)
    elif sign == '*':
        result = 1
        for x in args:
            result *= x
        return result

print(f"{2.5 * 2:.2f}")

print(f"{36.66 / 6:.2f}")