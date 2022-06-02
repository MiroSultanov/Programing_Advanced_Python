def positive_and_negative_nums(*args):
    positive_sum = 0
    negative_sum = 0

    for elements in args:
        if elements > 0:
            positive_sum += elements
        else:
            negative_sum += elements
    return positive_sum, negative_sum

nums = [int(x) for x in input().split()]
positive_sum, negative_sum = positive_and_negative_nums(*nums)

print(negative_sum)
print(positive_sum)

if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")