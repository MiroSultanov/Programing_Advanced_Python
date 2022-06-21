def get_magic_triangle(n: int) -> None:
    retval = [[1], [1, 1]]
    for i in range(3, n + 1):
        temp_list = [1]
        for j in range(i - 2):
            el_sum = sum([el for i, el in enumerate(retval[i - 2]) if i in (j, j + 1)])
            temp_list.append(el_sum)
        temp_list.append(1)
        retval.append(temp_list)

    return retval

print(get_magic_triangle(5))