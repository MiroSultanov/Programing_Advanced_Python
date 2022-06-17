# Everything in the Satna Claus' workshop was going well until, on one freezing Sunday, a dangerous storm destroyed almost all toys. Now Santa's elves fear they won't 
# be able to meet their December deadline. It could be a disaster, and some children around the world may not get their Christmas toys. Luckily, you've come up with an
# idea, and you just need to write a program that manages your plan.
# The Christmas elves have special toy-making skills - еach elf can make a toy from a given number of materials.
# First, you will receive a sequence of integers representing each elf's energy. On the following line, you will be given another sequence of integers, each 
# representing a number of materials in a box.
# Your task is to calculate the total elves' energy used for making toys and the total number of successfully made toys.
# You are very clever and have immediately recognized the pros and cons of the work process - the first elf takes the last box of materials and tries to create the toy:
# •	Usually, the elf needs energy equal to the number of materials. If he has enough energy, he makes the toy. His energy decreases by the used energy, and the toy 
# goes straight to Santa's bag. Then, the elf eats a cookie reward which increases his energy by 1, and goes to the end of the line, preparing for the upcoming boxes.
# •	Every third time one of the elves takes a box, he tries his best to be creative, and he will need twice as much energy as usual. If he has enough, he manages to 
# create 2 toys. Then, his energy decreases; he eats a cookie reward and goes to the end of the line, similar to the first bullet.
# •	Every fifth time one of the elves takes a box, he is a little clumsy and somehow manages to break the toy when he just made it (if he made it). The toy is thrown
# away, and the elf doesn't get a cookie reward. However, his energy is already spent, and it needs to be added to the total elves' energy.
# o	If an elf creates 2 toys, but he is clumsy, he breaks them.
# •	If an elf does not have enough energy, he leaves the box of materials to the next elf. Instead of making the toy, the elf drinks a hot chocolate which doubles 
# his energy, and goes to the end of the line, preparing for the upcoming boxes.
# Note: North Pole's social policy is very tolerant of the elves. If the current elf's energy is less than 5 units, he does NOT TAKE a box, but he takes a day off. 
# Remove the elf from the collection.
# Stop crafting toys when you are out of materials or elves.


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
