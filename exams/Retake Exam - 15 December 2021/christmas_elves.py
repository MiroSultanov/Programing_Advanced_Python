from collections import deque

elves_energy = deque(int(x) for x in input().split())
materials = [int(x) for x in input().split()]
toys = 0
energy = 0
counter = 0

while True:
    if not materials or not elves_energy:
        break
    elif materials and elves_energy and elves_energy[0] >= 5:
        elf = elves_energy.popleft()
        material = materials.pop()
    else:
        elves_energy.popleft()
        continue
    counter += 1
    if counter % 3 == 0:
        if elf >= material * 2:
            if counter % 5 != 0:
                elves_energy.append(elf + 1 - material * 2)
                energy += material * 2
                toys += 2
                continue
            else:
                elves_energy.append(elf - material * 2)
                energy += material * 2
                continue
        else:
            elves_energy.append(elf * 2)
            materials.append(material)
            continue
    if counter % 5 == 0:
        if elf >= material:
            elves_energy.append(elf - material)
            energy += material
            continue
        else:
            materials.append(material)
            elves_energy.append(elf * 2)
            continue
    if elf >= material:
        elves_energy.append(elf - material + 1)
        energy += material
        toys += 1
    else:
        elves_energy.append(elf * 2)
        materials.append(material)

print(f'Toys: {toys}')
print(f'Energy: {energy}')
if elves_energy:
    print(f'Elves left: {", ".join([str(x) for x in elves_energy])}')
if materials:
    print(f'Boxes left: {", ".join([str(x) for x in materials])}')