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