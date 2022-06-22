from collections import deque


def best_list_pureness(num_list: list, rotations: int):
    function_memory = []
    temp_list = deque(num_list)
    for i in range(rotations + 1):
        pureness = sum([i * num for i, num in enumerate(temp_list)])
        function_memory.append((i, pureness))
        temp_list.rotate(1)

    sorted_list = sorted(function_memory, key=lambda el: (-el[1], el[0]))
    rotation, value = sorted_list[0]
    return f"Best pureness {value} after {rotation} rotations"

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)



