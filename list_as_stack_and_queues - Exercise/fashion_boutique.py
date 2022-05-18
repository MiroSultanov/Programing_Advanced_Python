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