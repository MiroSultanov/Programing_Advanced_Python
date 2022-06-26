from collections import deque

first_player, second_player = input().split(', ')

matrix = [input().split() for _ in range(6)]

find_the_exit = False
find_the_trap = False

players_moves = deque([first_player, second_player])
player_for_rest = []

while not find_the_trap or not find_the_exit:
    current_player_row, current_player_col = [int(el) for el in input()[1:-1].split(', ')]
    current_player = players_moves.popleft()
    if current_player in player_for_rest:
        player_for_rest.remove(current_player)
        players_moves.append(current_player)
        continue
    if matrix[current_player_row][current_player_col] == 'E':
        find_the_exit = True
        print(f"{current_player} found the Exit and wins the game!")
        exit(0)
    elif matrix[current_player_row][current_player_col] == 'T':
        find_the_trap = True
        print(f"{current_player} is out of the game! The winner is {players_moves.pop()}.")
        exit(0)
    elif matrix[current_player_row][current_player_col] == 'W':
        player_for_rest.append(current_player)
        print(f"{current_player} hits a wall and needs to rest.")
    players_moves.append(current_player)
