# This year Santa has decided to share his secret with you. Get ready to learn how his elves craft all the presents.
# First, you will receive a sequence of integers representing the number of materials for crafting toys in one box. After that, you will be given another 
# sequence of integers – their magic level.
# Your task is to mix materials with magic so you can craft presents, listed in the table below with the exact magic level:


# Present	Magic needed
# Doll	150
# Wooden train	250
# Teddy bear	300
# Bicycle 	400

# You should take the last box with materials and the first magic level value to craft a toy. Their multiplication calculates the total magic level. 
# If the result equals one of the levels described in the table above, you craft the present and remove both materials and magic value. Otherwise:
# •	If the product of the operation is a negative number, you should sum the values together, remove them both from their positions, and add the result to the 
# materials.
# •	If the product doesn't equal one of the magic levels in the table and is a positive number, remove only the magic value and increase the material value by 15.
# •	If the magic or material (or both) equals 0, remove it (or both) and continue crafting the presents.
# Stop crafting presents when you run out of boxes of materials or magic level values.
# Your task is considered done if you manage to craft either one of the pairs:
# •	a doll and a train
# •	a teddy bear and a bicycle


from collections import deque

materials = [int(x) for x in input().split()]
magic_value = deque([int(x) for x in input().split()])

crafting_table = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}
crafted_toys = {}

while materials and magic_value:
    material = materials.pop()
    value = magic_value.popleft()

    if material == 0 and value == 0:
        continue

    if material == 0:
        magic_value.appendleft(value)
        continue

    if value == 0:
        materials.append(material)
        continue

    result = material * value
    if result in crafting_table:
        toy_name = crafting_table[result]
        if toy_name in crafted_toys:
            crafted_toys[toy_name] += 1
        else:
            crafted_toys[toy_name] = 1
        continue

    if result < 0:
        materials.append(material + value)
    else:
        materials.append(material + 15)

if ('Doll' in crafted_toys and 'Wooden train' in crafted_toys) or ('Teddy bear' in crafted_toys and 'Bicycle' in crafted_toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")

if magic_value:
    print(f"Magic left: {', '.join([str(x) for x in magic_value])}")

for toy, count in sorted(crafted_toys.items()):
    print(f"{toy}: {count}")
