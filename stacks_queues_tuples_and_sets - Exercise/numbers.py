first_set = set([int(x) for x in input().split()])
second_set = set([int(x) for x in input().split()])

number = int(input())

for _ in range(number):
    input_command = input().split()
    command = input_command[0]
    target_set = input_command[1]

    if command == "Add":
        if target_set == "First":
            first_set = first_set.union([int(x) for x in input_command[2:]])
        else:
            second_set = second_set.union([int(x) for x in input_command[2:]])
    elif command == "Remove":
        if target_set == "First":
            first_set = first_set.difference([int(x) for x in input_command[2:]])
        else:
            second_set = second_set.difference([int(x) for x in input_command[2:]])
    else:
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")