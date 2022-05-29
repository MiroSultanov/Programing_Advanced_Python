# Write a program to flatten several lists of numbers received in the following format:
# 	String with numbers or empty strings separated by "|"
# 	Values are separated by spaces (" ", one or several)
# 	Order the output list from the last to the first matrix sub-lists and their values from left to right as shown below


sublist = input().split("|")
result = []

for index in range(len(sublist)-1, -1, -1):
    current_element = sublist[index].strip().split()
    result.extend(current_element)

print(" ".join(result))
