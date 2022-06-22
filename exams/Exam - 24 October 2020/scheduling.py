jobs = [int(x) for x in input().split(", ")]
index = int(input())

stack = sorted([(job, i) for i, job in enumerate(jobs)], key=lambda item: (-item[0], -item[1]))
cycle = 0

while True:
    job, i = stack.pop()
    cycle += job
    if i == index:
        break
print(cycle)