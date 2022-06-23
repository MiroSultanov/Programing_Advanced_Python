def numbers_searching(*args):
    duplicates = [arg for arg in args if args.count(arg) > 1]
    missing_numbers = next((i for i in range(min(args), max(args)) if i not in args))
    result = list()
    result.append(missing_numbers)
    result.append(sorted(set(duplicates)))
    return result

print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
