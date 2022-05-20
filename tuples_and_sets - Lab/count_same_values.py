# You will be given numbers separated by a space. 
# Write a program that prints the number of occurrences of each number in the format "{number} - {count} times". 
# The number must be formatted to the first decimal point.

numbers_input = input()
occurrence_count = {}
numbers = [float(x) for x in numbers_input.split(' ')]

for number in numbers:
    if number not in occurrence_count:
        occurrence_count[number] = 0
    occurrence_count[number] += 1

for number, counts in occurrence_count.items():
    print(f"{number:.1f} - {counts} times")
