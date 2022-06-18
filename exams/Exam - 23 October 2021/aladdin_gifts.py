from collections import deque

materials = deque([int(x) for x in input().split()])
magic_levels = deque([int(x) for x in input().split()])
presents = []

wedding_gifts = {
    1: "Gemstone",
    2: "Porcelain Sculpture",
    3: "Gold",
    4: "Diamond Jewellery"
}

while materials and magic_levels:
    material = materials.pop()
    level = magic_levels.popleft()
    mix = material + level

    if mix < 100:
        if mix % 2 == 0:
            mix = material * 2 + level * 3
        else:
            mix = material * 2 + level * 2

    if mix > 499:
        mix /= 2

    gift = wedding_gifts.get(mix//100)
    if gift:
        presents.append(gift)

if wedding_gifts.get(1) in presents and wedding_gifts.get(2) in presents:
    print("The wedding presents are made!")
elif wedding_gifts.get(3) in presents and wedding_gifts.get(4) in presents:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f'Materials left:', ', '.join([str(el) for el in materials]))
if magic_levels:
    print(f'Magic left:', ', '.join([str(el) for el in magic_levels]))

sorted_list = sorted([(el, presents.count(el)) for el in set(presents)])
for item in sorted_list:
    print(f'{item[0]}: {item[1]}')


