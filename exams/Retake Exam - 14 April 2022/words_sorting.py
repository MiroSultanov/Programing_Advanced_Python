# Write a function words_sorting which receives a different number of words.
# Create a dictionary, which will have as keys the words that the function received. For each key, create a value that is the sum of all ASCII values of that key.
# Then, sort the dictionary:
# •	By values in descending order, if the sum of all values of the dictionary is odd
# •	By keys in ascending order, if the sum of all values of the dictionary is even
# Note: Submit only the function in the judge system
# Input
# •	There will be no input, just any number of words passed to your function
# Output
# •	The function should return a string in the format "{key} - {value}" for each key and value on a separate lines

# TEST CODE:
#     print(
#     words_sorting(
#         'escape', 
#         'charm', 
#         'mythology'
#   ))


def words_sorting(*args):
    word_dict = {}
    for word in args:
        if word not in word_dict:
            word_dict[word] = 0
        ascii_sum = sum(ord(el) for el in word)
        word_dict[word] += ascii_sum
    sum_of_values = sum(el for el in word_dict.values())
    if sum_of_values % 2 == 0:
        sorted_dict = [item for item in sorted(word_dict.items(), key=lambda item: item[0])]
    else:
        sorted_dict = [item for item in sorted(word_dict.items(), key=lambda item: -item[1])]

    retdict = []
    for item in sorted_dict:
        key, value = item[0], item[1]
        retdict.append(f"{key} - {value}")

    return '\n'.join([el for el in retdict])

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
