number_of_names = int(input())
names_set = set()

for _ in range(number_of_names):
    names_set.add(input())
[print(name) for name in names_set]