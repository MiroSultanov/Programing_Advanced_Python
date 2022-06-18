# Aladdin, rich and powerful with the help of the Genie, is now preparing to marry the princess Jasmine. He asks Genie for help to prepare the wedding presents.
# First, you will receive a sequence of integers representing the materials for every wedding present. After that, you will be given another sequence of 
# integers – Genie magic level for every aim to make a gift.
# Your task is to mix materials with magic levels so you can make presents, listed in the table below.

# Gift	              Magic needed
# Gemstone	            100 to 199
# Porcelain Sculpture	    200 to 299
# Gold	                300 to 399
# Diamond Jewellery	    400 to 499

# To make a present, you should take the last integer of materials and sum it with the first magic level value. If the result is between or equal to the numbers 
# described in the table above, you make the corresponding gift and remove both materials and magic value. Otherwise:
# •	If the product of the operation is under 100:
# o	And if it is an even number, double the materials, and triple the magic, then sum it again. 
# o	And if it is an odd number, double the sum of the materials and the magic level. Then, check again if it is between or equal to any of the numbers in the 
# table above.
# •	If the product of the operation is more than 499, divide the sum of the material and the magic level by 2. Then, check again if it is between or equal to any 
# of the numbers in the table above.
# •	If, however, the result is not between or equal to any of the numbers in the table above after performing the calculation, remove both the materials and the 
# magic level.
# Stop crafting gifts when you are out of materials or magic level.
# You have succeeded in crafting the presents when you've crafted either one of the pairs - a gemstone and a sculpture or gold and jewellery.


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


