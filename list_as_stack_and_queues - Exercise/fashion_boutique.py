# You own a fashion boutique and receive a delivery of a huge box of clothes, represented as a sequence of integers. On the following line, you will be given an integer 
# representing the capacity for one rack in your store.  
# You must arrange the clothes in the store and use the racks to hang up every piece of clothing. You start from the last piece of clothing on the top of the pile to the 
# first one at the bottom. Use a stack for this purpose. Each piece of clothing has its value (an integer). You must sum their values while you take them out of the box:
# •	If the sum becomes equal to the capacity of the current rack, you must take a new one for the next clothes (if there are any left in the box). 
# •	If the sum becomes greater than the capacity, do not hang the piece of clothing on the current rack. Take a new rack and then hang it up.
# In the end, print how many racks you have used to hang up the clothes.


clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
current_rack_capacity = rack_capacity
rack_counter = 1

while clothes:
    piece_of_clothes = clothes[-1]

    if piece_of_clothes > current_rack_capacity:
        rack_counter += 1
        current_rack_capacity = rack_capacity
    else:
        current_rack_capacity -= piece_of_clothes
        clothes.pop()

print(rack_counter)
