# On the first line, you will receive a sequence of numbers, each representing an egg with its size. On the second line, you will receive another sequence of 
# numbers, each representing a piece of paper with its size. 
# You should take the first egg and wrap it with the last piece of paper. Then, try to put it in a box with a size of 50. Each wrapped-in-a-paper egg fills one 
# box if it fits in it. Your task is to check whether you have filled at least one box.
# You should comply with the following conditions:
# •	If the egg is not fresh anymore (its size is less than or equal to 0), you need to remove it from the sequence before it is wrapped with a piece of paper.
# •	If the sum of the egg's size and the paper's size is less than or equal to the box's size (50), put the wrapped egg in the box and remove both from the sequences.
# o	Otherwise, you cannot fill a box, so remove both the egg and the paper from the sequences without putting them in a box.
# •	During your work, you noticed that Old MacDonald is superstitious. If the size of an egg is 13 it brings bad luck to him. You should remove this egg from the 
# sequence before it is wrapped with a piece of paper. 
# o	Furthermore, each time you take an egg with a size of 13, it will be best to swap the first and last pieces of paper positions to bring the good luck back to 
# Old MacDonald.
# 	Note: There will be NO case where there will be just one piece of paper left.
# For more clarification see the examples below.
# Input
# •	In the first line, you will be given a sequence of eggs with their sizes - integers separated by comma and space ", " in the range [-100, 100]
# •	In the second line, you will be given a sequence of pieces of paper with their sizes - integers separated by comma and space ", " in the range [1, 100]
# Output
# •	On the first line:
# o	If you have at least one box filled, print: 
# 	"Great! You filled {total count} boxes."
# o	If you couldn't fill any boxes, print:
# 	"Sorry! You couldn't fill any boxes!"
# •	On the following lines, print the eggs left or pieces of paper left if there are any:
# o	Eggs left: {left eggs joined by ", "}
# o	Pieces of paper left: {left pieces of paper joined by ", "}


from collections import deque

eggs = deque([int(el) for el in input().split(', ')])
papers = deque([int(el) for el in input().split(', ')])

number_of_box = 0

while eggs and papers:
    current_egg = eggs.popleft()
    if current_egg == 13:
        first_paper_el = papers.popleft()
        last_paper_el = papers.pop()
        papers.append(first_paper_el)
        papers.appendleft(last_paper_el)
    elif current_egg <= 0:
        continue
    else:
        current_paper = papers.pop()
        sum_of_egg_and_paper = current_egg + current_paper
        if sum_of_egg_and_paper <= 50:
            number_of_box += 1

if number_of_box > 0:
    print(f"Great! You filled {number_of_box} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(str(egg) for egg in eggs)}")
if papers:
    print(f"Pieces of paper left: {', '.join(str(paper) for paper in papers)}")



# VARIANT II
# from collections import deque
#
# eggs = deque([int(x) for x in input().split(", ")])
# papers = deque([int(x) for x in input().split(", ")])
# total_count = 0
#
# while eggs and papers:
#     egg = eggs.popleft()
#     paper = papers.pop()
#
#     if egg <= 0:
#         continue
#     if egg == 13:
#         egg = eggs.popleft()
#         papers.append(paper)
#         papers[0], papers[-1] = papers[-1], papers[0]
#         continue
#
#
#     if egg + paper <= 50:
#         total_count += 1
#         continue
#     else:
#         egg = eggs.popleft()
#         paper = papers.pop()
#         continue
#
#
# if total_count >= 1:
#     print(f"Great! You filled {total_count} boxes.")
# else:
#     print("Sorry! You couldn't fill any boxes!")
#
# if eggs:
#     print(f"Eggs left: {', '.join([str(x) for x in eggs])}")
#
# if papers:
#     print(f"Pieces of paper left: {', '.join([str(x) for x in papers])}")


