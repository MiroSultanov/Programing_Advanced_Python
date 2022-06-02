from collections import deque


def math_operations(*args, **kwargs):
    calc = {
        'a': lambda num: kwargs['a'] + num,
        's': lambda num: kwargs['s'] - num,
        'd': lambda num: kwargs['d'] / num if num != 0 else kwargs['d'],
        'm': lambda num: kwargs['m'] * num
    }

    operations = deque(('a', 's', 'd', 'm'))
    for arg in args:
        func = operations[0]
        kwargs[func] = calc[func](arg)
        operations.rotate(-1)

    return kwargs

# test_output

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
