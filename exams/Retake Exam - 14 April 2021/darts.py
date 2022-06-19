# You will be given a matrix with 7 rows and 7 columns representing the dartboard.
# Each of the two players starts with a score of 501 and they take turns to throw a dart – one throw for each player. The score for each turn is deducted from the 
# player’s total score. The first player who reduces their score to zero or less wins the game.
# You are going to receive the information for every throw on a separate line. The coordinate information of a hit will be in the format: "({row}, {column})".
# •	If a player hits outside the dartboard, he does not score any points.
# •	If a player hits a number, it is deducted from his total.
# •	If a player hits a "D" the sum of the 4 corresponding numbers per column and row is doubled and then deducted from his total.
# •	If a player hits a "T" the sum of the 4 corresponding numbers per column and row is tripled and then deducted from his total.
# •	"B" is the bullseye. If a player hits it, he wins the game, and the program ends.
# For example, if Peter hits position with coordinates (2, 1), he wins (23 + 2 + 9 + 18) * 2 = 104 points and they are deducted from his total.
# Your job is to find who won the game and with how many turns.
# Input
# •	The name of the first player and the name of the second player, separated by ", "
# •	7 lines – the dartboard (separated by single space)
# •	On the next lines - the coordinates in the format: "({row}, {column})"
# Output
# •	You should print only one line containing the winner and his count of throws: 
# "{name} won the game with {count_turns} throws!"


def valid_coordinates(row_index, col_index, size):
    return 0 <= row_index < size and 0 <= col_index < size


def calculate_score(row, col, size, multiplier):
    sum_score = int(board[0][col]) + int(board[size - 1][col]) + int(board[row][0]) + int(board[row][size - 1])
    if multiplier == "D":
        return sum_score * 2
    elif multiplier == "T":
        return sum_score * 3
    elif multiplier == "B":
        return 501


size = 7
player_1, player_2 = input().split(", ")
board = [input().split() for _ in range(size)]

players_scores = {player_1: 501, player_2: 501}
players_throws = {player_1: 0, player_2: 0}

current_player, next_player = player_1, player_2
winner = ""

while True:

    throw_row, throw_col = eval(input())
    players_throws[current_player] += 1

    if valid_coordinates(throw_row, throw_col, size):

        if board[throw_row][throw_col].isdigit():
            players_scores[current_player] -= int(board[throw_row][throw_col])

        else:
            multiplier = board[throw_row][throw_col]
            score = calculate_score(throw_row, throw_col, size, multiplier)
            players_scores[current_player] -= score

        if players_scores[current_player] <= 0:
            winner = current_player
            break

    current_player, next_player = next_player, current_player

print(f"{winner} won the game with {players_throws[winner]} throws!")
