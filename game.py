import random
import time


def intro():
    print_pause("Tic-Tac-Toe It's a really simple game that played on"
                " a grid that's 3 squares by 3 squares.")
    print_pause("The first player to get 3 of her marks in a row "
                "(up, down, across, or diagonally) is the winner.")
    print_pause("When all 9 squares are full, the game is over. "
                "If no player has 3 marks in a row, the game ends")
    print_pause("you will play first with 'X' simpol, "
                "and bot will take 'O' simpol ")


def condition(n1, n2, n3):
    if n1 == n2 == n3 == 'X':
        print_pause('Congrats!, you win !')
        return True
    elif n1 == n2 == n3 == 'O':
        print('you lose !')
        return True


def win_case(bord):
    if (condition(bord[0], bord[1], bord[2]) or
            condition(bord[3], bord[4], bord[5]) or
            condition(bord[6], bord[7], bord[8]) or
            condition(bord[0], bord[4], bord[8]) or
            condition(bord[2], bord[4], bord[6]) or
            condition(bord[0], bord[3], bord[6]) or
            condition(bord[1], bord[4], bord[7]) or
            condition(bord[2], bord[5], bord[8])):
        return True


def print_pause(s):
    print(s)
    time.sleep(1)


def user_play(bord, used):
    user_answer = valid_answer(used)
    replace('X', user_answer, bord)
    used.append(user_answer)


def bot_play(bord, used):
    while True:
        bot_answer = random.choice(range(1, 10))
        if bot_answer not in used:
            break
    time.sleep(1)
    print("bot played at position ", bot_answer)
    replace('O', bot_answer, bord)
    used.append(bot_answer)


def valid_answer(used):
    while True:
        time.sleep(1)
        answer = int(input("choose position from 1 to 9 :\n"))
        if 1 <= answer <= 9:
            if answer not in used:
                break
    return answer


def print_bord(bord):
    time.sleep(1)
    x = 0
    for x in range(9):
        print(bord[x], end=" | ")
        if x % 3 == 2:
            print('')


def replace(char, answer, bord):
    for x in range(9):
        if bord[x] == answer:
            bord[x] = char


def play_game():
    bord = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    used = []
    intro()
    print_bord(bord)
    user_play(bord, used)
    for position in range(4):

        bot_play(bord, used)
        print_bord(bord)
        if win_case(bord):
            break

        user_play(bord, used)
        print_bord(bord)
        if win_case(bord):
            break

    print_pause('the game is over !')
    again = input('wanna play again ? ').lower()
    if 'yes' in again:
        play_game()
    elif 'no' in again:
        print_pause('goodbye ,see you again !')
    else:
        print_pause('sorry, i dont understand')


play_game()
