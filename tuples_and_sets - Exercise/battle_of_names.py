# You will receive a number N. On the following N lines, you will be receiving names. You should sum the ASCII values of each letter in the name and integer 
# divide it to the number of the current row (starting from 1). Save the result to a set of either odd or even numbers, depending on if the resulting number is 
# odd or even. After that, sum the values of each set.
# •	If the sums of the two sets are equal, print the union of the values, separated by ", ". 
# •	If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values, separated by ", ".
# •	If the sum of the even numbers is bigger than the sum of the odd numbers, print the symmetric-different values, separated by ", ".


n = int(input())
even = set()
odd = set()

for row in range(1, n + 1):
    name = input()
    name_sum = sum([ord(x) for x in name]) // row
    if name_sum % 2 == 0:
        even.add(name_sum)
    else:
        odd.add(name_sum)

even_sum = sum(even)
odd_sum = sum(odd)

if even_sum == odd_sum:
    result = odd.union(even)
elif odd_sum < even_sum:
    result = odd.symmetric_difference(even)
else:
    result = odd.difference(even)

print(*result, sep=", ")
