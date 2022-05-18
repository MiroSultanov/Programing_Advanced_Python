# The super-spy action hero Sam has finally found some time to go on a holiday. He is taking his wife somewhere nice, and they're going to have a really good time,
# but first, they have to get there. Even on his holiday trip, Sam is still going to run into some problems, and the first one is getting to the airport. 
# Right now, he is stuck in a traffic jam at a crossroads where a lot of accidents happen.
# Your job is to keep track of the traffic at the crossroads and report whether a crash happened or everyone passed the crossroads safely.
# Sam is on a single lane of cars that queue until the light goes green. When it does, they start passing one by one on a flashing green light and during the 
# free window before the intersecting road's light goes green. For each second, only one part of a car (a single character) passes the crossroad. If a car is 
# still in the middle of the crossroads when the free window ends, it will get hit at the first character that is still in the crossroads.


from collections import deque


def queue_len(lst: list) -> int:
    if lst:
        return sum([len(x) for x in lst])
    else:
        return 0


road_queue = deque()
crossroad = deque()
entry_window = int(input())
exit_window = int(input())
passed_cars = 0
crash_char = ''

while True:
    input_line = input()
    if input_line == 'END':
        break

    if input_line == 'green':
        time_to_enter = entry_window
        while road_queue and time_to_enter > 0:
            entering_car = road_queue.popleft()
            crossroad.append(entering_car)
            time_to_enter -= len(entering_car)

        time_left = entry_window + exit_window
        while crossroad:
            car = crossroad.popleft()
            if len(car) <= time_left:
                time_left -= len(car)
                passed_cars += 1
                continue
            else:
                crash_char = car[time_left]
                break

        if crash_char:
            print("A crash happened!")
            print(f"{car} was hit at {crash_char}.")
            break

    else:
        road_queue.append(input_line)

if not crash_char:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")
