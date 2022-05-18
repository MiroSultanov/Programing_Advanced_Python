# Our favorite super-spy action hero Sam is back from his vacation, and it is time to go on a mission. He needs to unlock a safe locked by several locks in a row,
# which all have varying sizes. The hero possesses a special weapon called the Key Revolver, with special bullets. Each bullet can unlock a lock with a size equal 
# to or larger than the size of the bullet. The bullet goes into the keyhole, then explodes, completely destroying it. Sam doesn't know the size of the locks, so
# he needs to just shoot at all of them until the safe runs out of locks. What's behind the safe, you ask? Well, intelligence! It is told that Sam's sworn 
# enemy – Nikoladze, keeps his top-secret Georgian Chacha Brandy recipe inside. It's valued differently across different times of the year, so Sam's boss 
# will tell him what it's worth over the radio. One last thing, every bullet Sam fires will also cost him money, which will be deducted from his pay from the price 
# of the intelligence. 
# Good luck, operative.


from collections import deque


def reload_gun() -> None:
    global bullets
    global barrel
    for _ in range(barrel_size):
        if bullets:
            barrel.append(bullets.pop())
    return None


bullet_cost = int(input())
barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))
intel_value = int(input())
earnings = 0

barrel = deque()
reload_gun()

while True:
    if bullets and not barrel:
        print('Reloading!')
        reload_gun()

    if not (bullets or barrel) or not locks:
        break

    bullet = barrel.popleft()
    earnings -= bullet_cost
    if bullet <= locks[0]:
        print('Bang!')
        locks.popleft()
    else:
        print('Ping!')

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    earnings += intel_value
    print(f"{len(bullets) + len(barrel)} bullets left. Earned ${earnings}")
