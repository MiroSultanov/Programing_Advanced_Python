# Write a program that finds the longest intersection. You will be given a number N. On each of the next N lines you will be given two ranges in the 
# format: "{first_start},{first_end}-{second_start},{second_end}". You should find the intersection of these two ranges. The start and end numbers in the ranges are 
# inclusive. Finally, you should find the longest intersection of all N intersections, print the numbers that are included and its length in the 
# format: "Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}"


number_of_intersection = int(input())
best_intersection = set()

for _ in range(number_of_intersection):
    first_range, second_range = input().split("-")
    first_start, first_end = [int(x) for x in first_range.split(',')]
    second_start, second_end = [int(x) for x in second_range.split(",")]

    first = set(range(first_start, first_end + 1))
    second = set(range(second_start, second_end + 1))

    current_intersection = first.intersection(second)

    if len(current_intersection) > len(best_intersection):
        best_intersection = current_intersection

print(f"Longest intersection is [{', '.join(str(x) for x in best_intersection)}] with length {len(best_intersection)}")
