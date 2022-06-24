from collections import deque

bomb_effect = deque(int(x) for x in input().split(", "))
bomb_casing = deque([int(x) for x in input().split(", ")])
bomb_materials = {
    "Datura Bombs": {
        "requirement": 40,
        "count": 0},
    "Cherry Bombs": {
        "requirement": 60,
        "count": 0},
    "Smoke Decoy Bombs": {
        "requirement": 120,
        "count": 0}
}
requirements = [bomb_materials[key]['requirement'] for key in bomb_materials.keys()]
pouch = 0

while bomb_effect and bomb_casing:
    if bomb_casing[-1] + bomb_effect[0] in requirements:
        effect = bomb_effect.popleft()
        casing = bomb_casing.pop()

        for key, value in bomb_materials.items():

            if value['requirement'] == effect + casing:
                bomb_materials[key]['count'] += 1
                break

    else:
        bomb_casing[-1] -= 5

    pouch = [bomb_materials[key]['count'] for key in bomb_materials.keys() if bomb_materials[key]['count'] >= 3]
    if len(pouch) == 3:
        break

if len(pouch) == 3:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effect:
    print("Bomb Effects: ", ', '.join([str(x) for x in bomb_effect]), sep="")
else:
    print("Bomb Effects: empty")

if bomb_casing:
    print("Bomb Casings: ", ', '.join([str(x) for x in bomb_casing]), sep='')
else:
    print("Bomb Casings: empty")

output = [(key, value['count']) for key, value in bomb_materials.items()]
for item in sorted(output):
    print(f"{item[0]}: {item[1]}")




