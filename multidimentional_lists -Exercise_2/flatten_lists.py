sublist = input().split("|")
result = []

for index in range(len(sublist)-1, -1, -1):
    current_element = sublist[index].strip().split()
    result.extend(current_element)

print(" ".join(result))
