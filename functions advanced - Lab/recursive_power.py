def recursive_power(value, power):
    if power == 0:
        return 1

    if power == 1:
        return value

    return value * recursive_power(value, power - 1)

# test_output

print(recursive_power(2, 10))
print(recursive_power(10, 100))
