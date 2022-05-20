# Write a program, which will take a list of names and print only the unique names in the list.
# The order in which we print the result does not matter.


number_of_names = int(input())
names_set = set()

for _ in range(number_of_names):
    names_set.add(input())
[print(name) for name in names_set]
