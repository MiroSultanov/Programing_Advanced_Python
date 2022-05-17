# Write a program that keeps track of people getting water from a dispenser and the amount of water left at the end. 
# On the first line, you will receive the starting quantity of water (integer) in a dispenser. Then, on the following lines, you will be given the 
# names of some people who want to get water (each on a separate line) until you receive the command "Start". Add those people in a queue. Finally, you 
# will receive some commands until the command "End":
# -	"{liters}" - litters (integer) that the current person in the queue wants to get. Check if there is enough water in the dispenser for that person.
# o	If there is enough water, print "{person_name} got water" and remove him/her from the queue.
# o	Otherwise, print "{person_name} must wait" and remove the person from the queue without reducing the water in the dispenser.
# -	"refill {liters}" - add the given litters in the dispenser.
# In the end, print how many liters of water have left in the format: "{left_liters} liters left".


from collections import deque

water_quantity = int(input())
people = deque()

while True:
    command = input()
    if command == "Start":
        break
    people.append(command)

while True:
    command = input()
    if command == "End":
        break

    if command.startswith("refill "):
        params = command.split(" ")
        water_quantity += int(params[1])
    else:
        person = people.popleft()
        water_wanted = int(command)

        if water_wanted <= water_quantity:
            print(f"{person} got water")
            water_quantity -= water_wanted
        else:
            print(f"{person} must wait")

print(f"{water_quantity} liters left")
