# You will have to find all possible color combinations that can be used.
# Write a program that finds colors in a string. You will be given a string on a single line containing substrings (separated by a single space) from which you
# will be able to form the following colors: 
# Main colors: "red", "yellow", "blue"
# Secondary colors: "orange", "purple", "green"
# To form a color, you should concatenate the first and the last substrings and check if you can get any of the above colors' names. If there is only one substring left, you should use it to do the same check.
# You can only keep a secondary color if the two main colors needed for its creation could be formed from the given substrings:
# •	orange = red + yellow
# •	purple = red + blue
# •	green = yellow + blue
# Note: You could find some of the main colors needed to keep a secondary color after it is found. 
# When you form a color, remove both substrings. Otherwise, you should remove the last character of each substring and return them in the middle of the original string. 
# If the string contains an odd number of substrings, you should put the substrings one position ahead.
# For example, if you are given the string "re yellow bye" you could not form a color with the substring "re" and "bye", so you should remove the last character 
# and return them in the middle of the string: "r by yellow".
# In the end, print out the list with colors in the order in which they are found.


from collections import deque

primary_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}

collected_colors = []

words = deque(input().split())

while words:
    left = words.popleft()
    right = words.pop() if words else ''

    result = left + right
    if result in primary_colors or result in secondary_colors:
        collected_colors.append(result)
        continue
    result = right + left
    if result in primary_colors or result in secondary_colors:
        collected_colors.append(result)
        continue

    left = left[:-1]
    right = right[:-1]

    if left:
        words.insert(len(words) // 2, left)
    if right:
        words.insert(len(words) // 2, right)

result = []

forming_colors = {
    'orange': ['red', 'yellow'],
    'purple': ['red, blue'],
    'green': ['yellow', 'blue']
}

for color in collected_colors:
    if color in primary_colors:
        result.append(color)
        continue

    is_collected = True
    for helper_color in forming_colors[color]:
        if helper_color not in collected_colors:
            is_collected = False
            break

    if is_collected:
        result.append(color)

print(result)
