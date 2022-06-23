# Write a function called numbers_searching which receives a different amount of parameters. All parameters will be integer numbers forming a sequence of consecutive 
# numbers. Your task is to find an unknown amount of duplicates from the given sequence and a missing value, such that all the duplicate values and the missing value 
# are between the smallest and the biggest received number. The function should return a list with the last missing number as a first argument and a sorted list, 
# containing the duplicates found, in ascending order. For example: if we have the following numbers: 1, 2, 4, 2, 5, 4 will return 3 as missing number and 2, 4 as 
# duplicate numbers in the following format: [3, [2, 4]]


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
