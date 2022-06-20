from collections import deque

fireworks_show = deque([int(x) for x in input().split(", ")])
explosive_power = deque([int(x) for x in input().split(", ")])
fireworks = {
    "Palm": 0,
    "Willow": 0,
    "Crossette": 0
}
is_done = False

while fireworks_show and explosive_power:
    effect = fireworks_show.popleft()

    if effect <= 0:
        continue

    power = explosive_power.pop()
    if power <= 0:
        fireworks_show.appendleft(effect)
        continue

    fireworks_sum = effect + power

    if fireworks_sum % 3 == 0 and fireworks_sum % 5 != 0:
        fireworks["Palm"] += 1
    elif fireworks_sum % 3 != 0 and fireworks_sum % 5 == 0:
        fireworks["Willow"] += 1
    elif fireworks_sum % 3 == 0 and fireworks_sum % 5 == 0:
        fireworks["Crossette"] += 1
    else:
        fireworks_show.append(effect - 1)
        explosive_power.append(power)

    if fireworks["Palm"] >= 3 and fireworks["Willow"] >= 3 and fireworks["Crossette"] >= 3:
        is_done = True
        break

if is_done:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks_show:
    print(f"Firework Effects left: {', '.join(str(x) for x in fireworks_show)}", sep="")

if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}", sep="")

for key, value in fireworks.items():
    print(f"{key} Fireworks: {value}")

