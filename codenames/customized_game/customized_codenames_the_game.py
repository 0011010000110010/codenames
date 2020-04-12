"""
@author [jokerock]
@create date 2020-02-01 12:25:14
@modify date 2020-02-07 19:27:42
@desc [creating random new-turns for a game called "codenames"]
"""
import random  # ! for "random"
import numpy as np  # ! creating matrix and calculations


# ? for seperating code blocks and improving readability.
def basic_decor():
    print("*"*75)

# ? Here, will be created 25 random words which has been gotten from a Turkish dictionary database of Zargan.
def secret_master_template():
    word_list = []
    for i in range(25):
        with open("customized_harder_games.txt", "r", encoding="utf-8") as file:
            words = random.choice(file.readlines())
            words = words.split()
            word = random.choice(words)
            word_list.append(word)

    word_matrix = np.array(word_list).reshape((25, 1))
    # print(word_matrix) # ! if you want to see selected words top-down, delete "#"

    print("\t\t********Agent Master's Secret Board********")
    basic_decor()

    # ? This part creates a random secret board for agent masters so as to arrange the new game.
    """
    1: first team
    2: second team
    M: innocent card #? M for 'Masum' as Turkish
    S: assassin card #? S for 'Suikastçı' as Turkish
    """
    game_board = ["1", "1", "1", "1", "1", "1", "1", "1", "1", "2", "2",
                "2", "2", "2", "2", "2", "2", "M", "M", "M", "M", "M", "M", "M", "S"]
    random.shuffle(game_board)
    secret_game_board = np.array(game_board).reshape(25, 1)
    print("     ", secret_game_board[0], "     ", secret_game_board[1], "     ", secret_game_board[2], "     ", secret_game_board[3], "     ", secret_game_board[4],
        "\n", word_matrix[0], word_matrix[1], word_matrix[2], word_matrix[3], word_matrix[4],
        "\n\n     ", secret_game_board[5], "     ", secret_game_board[6], "     ", secret_game_board[
            7], "     ", secret_game_board[8], "     ", secret_game_board[9],
        "\n", word_matrix[5], word_matrix[6], word_matrix[7], word_matrix[8], word_matrix[9],
        "\n\n     ", secret_game_board[10], "     ", secret_game_board[11], "     ", secret_game_board[
            12], "     ", secret_game_board[13], "     ", secret_game_board[14],
        "\n", word_matrix[10], word_matrix[11], word_matrix[12], word_matrix[13], word_matrix[14],
        "\n\n     ", secret_game_board[15], "     ", secret_game_board[16], "     ", secret_game_board[
            17], "     ", secret_game_board[18], "     ", secret_game_board[19],
        "\n", word_matrix[15], word_matrix[16], word_matrix[17], word_matrix[18], word_matrix[19],
        "\n\n     ", secret_game_board[20], "     ", secret_game_board[21], "     ", secret_game_board[
            22], "     ", secret_game_board[23], "     ", secret_game_board[24],
        "\n", word_matrix[20], word_matrix[21], word_matrix[22], word_matrix[23], word_matrix[24])
    basic_decor()

# ? This part, chooses a team for beginning the game. Normally arranged as 6 people but it can be changed later, or extra players can be ignored if not necessary.

def team_selector():
    teammate = ["001", "002", "003", "004", "005", "006"]
    random.shuffle(teammate)
    blue_team = [teammate[0], teammate[2], teammate[4]]
    random.shuffle(blue_team)
    red_team = [teammate[1], teammate[3], teammate[5]]
    random.shuffle(red_team)
    cap1 = random.choice(blue_team)
    cap2 = random.choice(red_team)
    teams = ("Red", "Blue")
    print(f"Code numbers of 'Blue Team' are: {blue_team}\nCaptain of Blue team is {cap1}\n\nCode numbers of 'Red Team' are: {red_team}\n'Captain of Red Team is {cap2}\n\n'{random.choice(teams)} Team' is starting the game!")
    basic_decor()

# ? whole game setup is here, when starts code, it'll work step by step.
def main():
    basic_decor()
    print("\t\t********Welcome to the Codenames********")
    basic_decor()

    import time

    team_selector() # ! First players will choose codes for themselves.
    print("Hey 'team captains'!\nPlease be ready to see the 'Secret Board' in 30 seconds.\nDO NOT share this secret template with your teammates.")
    time.sleep(15)
    print('\nFew seconds remained. The Secret Board will be showing...\nDon\'t forget! "Secret Board" is only can be seen for team captains!')
    time.sleep(15)
    secret_master_template()
    print("Here is your secret template, caps! As captains, you can arrange cards for your teammates, now. Have fun!")

if __name__ == '__main__':
    main()