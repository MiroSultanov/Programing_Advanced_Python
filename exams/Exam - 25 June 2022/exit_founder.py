# First, you will be given the names "Tom" and "Jerry", separated by a comma and a space ", ". The order in which they are received determines the order in which 
# they will take turns. The first player starts first.
# Next, you will be given a matrix with 6 rows and 6 columns representing the maze board. It consists of:
# •	Only one Exit - marked with the "E" letter
# •	Trap (one, many, or none) - marked with the "T" letter
# •	Wall (one, many, or none) - marked with the "W" letter
# •	Empty positions will be marked with "."
# In the beginning, Tom and Jerry are outside the board. On each line, after the matrix is given, you will be receiving coordinates for each of the players. 
# They will be taking turns and stepping on different positions on the board until one of them find the Exit or falls into a Trap. Here are the rules:
# •	If a player hits the letter "E", he escapes the maze and wins the game.
# o	Print "{player} found the Exit and wins the game!" and end the program.
# •	If the letter "T" is hit, the player falls into a Trap, the game ends, and his opponent wins automatically.
# o	Print "{player} is out of the game! The winner is {winner}." and end the program.
# •	If the letter "W" is hit, the player hits a wall, and he needs to rest. The player's next move is ignored.
# o	Print "{player} hits a wall and needs to rest."
# •	If a player steps on an empty position ".", nothing happens. 
# •	Both players can step in the same position at the same time.


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
