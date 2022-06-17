# Santa Claus is always watching and seeing if children are good or bad. Only the nice children get Christmas presents, so Santa Claus is preparing his list this 
# year to check which child has been good or bad.
# Write a function called naughty_or_nice_list which will receive
# •	A list representing Santa Claus' "Naughty or Nice" list full of kids' names
# •	A different number of arguments (strings) and/or keywords representing commands
# The function should sort the kids in the given Santa Claus list into 3 lists: "Nice", "Naughty", and "Not found".
# The list holds a different number of kids - tuples containing two elements: a counting number (integer) at the first position and a name (string) at the second 
#     position. 
# For example: [(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy")].
# Next, the function could receive arguments and/or keywords. 
# Each argument is a command. The commands could be the following:
# •	"{counting_number}-Naughty" - if there is only one tuple in the given list with the same number, MOVE the kid to a list with NAUGHTY kids and remove it from 
# the Santa list. Otherwise, ignore the command.
# •	"{counting_number}-Nice" - if there is only one tuple in the given list with the same number, MOVE the kid to a list with NICE kids and remove it from the 
# Santa list. Otherwise, ignore the command.
# Each keyword holds a key with a name (string), and each value will be a string ("Naughty" or "Nice"): 
# •	If there is only one tuple with the same name, MOVE the kid to a list with NAUGHTY or to the list with NICE kids depending on the value in the keyword. 
# Then, remove it from the Santa list.
# •	Otherwise, ignore the command.
# All remaining tuples in the given Santa's list are not found kids, and they should be MOVED to the "Not found" list.
# In the end, return the final lists, each on a new line as described below.
# Note: Submit only the function in the judge system



def naughty_or_nice_list(*args, **kwargs):
    santas_dict = {"Nice": [], "Naughty": [], "Not found": []}

    first_list = args[0]
    santas_list = []
    for num, name in first_list:
        santas_list.append(num)
        santas_list.append(name)

    for el in args[1:]:
        number, command = el.split("-")
        number = int(number)
        counter = santas_list.count(number)
        if counter == 1:
            idx = santas_list.index(number)
            santas_dict[command].append(santas_list[idx + 1])
            del santas_list[idx:idx + 2]

    for key in kwargs:
        if key in santas_list:
            counter = santas_list.count(key)
            if counter == 1:
                kid_name = key
                behaviour = kwargs[key]
                santas_dict[behaviour].append(kid_name)
                idx = santas_list.index(kid_name)
                del santas_list[idx - 1:idx + 1]

    for el in santas_list[1::2]:
        santas_dict["Not found"].append(el)

    res = [f"{key}: {', '.join(value)}" for key, value in santas_dict.items() if len(value) > 0]
    return '\n'.join(res)


# ВАРИАНТ 2

from collections import Counter


def naughty_or_nice_list(names_list, *args, **kwargs):
    santa_list = {"Nice": [], "Naughty": [], "Not found": []}
    num_counter = Counter(el[0] for el in names_list)

    for el in args:
        data = el.split("-")
        number = int(data[0])
        kid_type = data[1]
        if num_counter[number] == 1:
            name = [name for num, name in names_list if num == number]
            santa_list[kid_type].extend(name)
            names_list = [el for el in names_list if el[0] != number]

    name_counter = Counter(el[1] for el in names_list)

    for name, type in kwargs.items():
        if name_counter[name] == 1:
            santa_list[type].append(name)
            names_list = [el for el in names_list if el[1] != name]

    for num, name in names_list:
        santa_list["Not found"].append(name)

    output = ""

    for type, kids in santa_list.items():
        if kids:
            output += f"{type}: {', '.join(kids)}\n"

    return output
