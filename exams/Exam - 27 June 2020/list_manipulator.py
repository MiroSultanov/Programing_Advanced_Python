from collections import deque


def list_manipulator(nums: list, add_remove: str, beginning_end: str, *args) -> list:
    retval = deque(nums)

    if add_remove == 'add':
        if beginning_end == 'beginning':
            retval.extendleft(reversed([arg for arg in args]))
        elif beginning_end == 'end':
            retval.extend([arg for arg in args])

    elif add_remove == 'remove':
        if beginning_end == 'beginning':
            if args:
                for _ in range(args[0]):
                    if retval:
                        retval.popleft()
            else:
                if retval:
                    retval.popleft()

        elif beginning_end == 'end':
            if args:
                for _ in range(args[0]):
                    if retval:
                        retval.pop()
            else:
                if retval:
                    retval.pop()

    return [el for el in retval]

print(list_manipulator([1,2,3], "remove", "end"))                   
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
