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


