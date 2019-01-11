#  by Davi Silveira | Tic Tac Toe Game
import random
from time import sleep

tic_dic = {
    "tl": ' ', "tm": ' ', "tr": ' ',
    "ml": " ", "mm": " ", "mr": " ",
    "bl": " ", "bm": " ", "br": " "
}

tic_lis = [
    'tl', 'tm', 'tr',
    'ml', 'mm', 'mr',
    'bl', 'bm', 'br'
]


#  Board to print
def board():
    print(tic_dic['tl'], tic_dic['tm'], tic_dic['tr'], sep="|")
    print("-+-+-")
    print(tic_dic['ml'], tic_dic['mm'], tic_dic['mr'], sep="|")
    print("-+-+-")
    print(tic_dic['bl'], tic_dic['bm'], tic_dic['br'], sep="|")


#  Rules_vs_user function will get the input from both human players
def rules_for_users():
    tic = 'X'
    rotations = 0
    while rotations <= 8:
        u = input(f"Where do you want to place your {tic}? ")

        if u not in tic_dic.keys():
            print("Oops, wrong value there buddy...")
            continue
        elif tic_dic[u] != " ":
            print("Come on, that's cheating... man")
            continue
        else:
            #  Set the value to the dict
            tic_dic[u] = tic
        board()

        #  Rules of the game
        if tic_dic['tl'] == tic and tic_dic['tm'] == tic and tic_dic['tr'] == tic:
            print(tic, "Wins the game!", sep=", ")
            exit()
        elif tic_dic['ml'] == tic and tic_dic['mm'] == tic and tic_dic['mr'] == tic:
            print(tic, "Wins the game!", sep=", ")
            exit()
        elif tic_dic['bl'] == tic and tic_dic['bm'] == tic and tic_dic['br'] == tic:
            print(tic, "Wins the game!", sep=", ")
            exit()
        elif tic_dic['tl'] == tic and tic_dic['ml'] == tic and tic_dic['bl'] == tic:
            print(tic, "Wins the game!", sep=", ")
            exit()
        elif tic_dic['tm'] == tic and tic_dic['mm'] == tic and tic_dic['bm'] == tic:
            print(tic, "Wins the game!", sep=", ")
            exit()
        elif tic_dic['tr'] == tic and tic_dic['mr'] == tic and tic_dic['br'] == tic:
            print(tic, "Wins the game!", sep=", ")
            exit()
        elif tic_dic['tl'] == tic and tic_dic['mm'] == tic and tic_dic['br'] == tic:
            print(tic, "Wins the game!", sep=", ")
            exit()
        elif tic_dic['tr'] == tic and tic_dic['mm'] == tic and tic_dic['bl'] == tic:
            print(tic, "Wins the game!", sep=", ")
            exit()
        if tic == 'X':
            tic = 'O'
        else:
            tic = 'X'

        rotations += 1
    #  Game over all values filled
    print("Game Over, guess we both lost this one")
    exit()


#  Rules function will get the input from user and call the 'comp function'
def rules_for_comp():
    tic = 'X'
    tac = "O"
    rotations = 0
    while rotations <= 8:
        u = input(f"Where do you want to place your {tic}? ")
        if u not in tic_dic.keys():
            print("Oops, wrong value there buddy...")
            continue
        elif tic_dic[u] != " ":
            print("Come on, that's cheating... man")
            continue
        else:
            #  Set the value to the dict
            tic_dic[u] = tic

        board()

        #  Rules of the game for 'X'
        if tic_dic['tl'] == tic and tic_dic['tm'] == tic and tic_dic['tr'] == tic:
            print(tic, "Wins the game!", sep=", ")
            exit()
        elif tic_dic['ml'] == tic and tic_dic['mm'] == tic and tic_dic['mr'] == tic:
            print(tic, "Wins the game!", sep=", ")
            exit()
        elif tic_dic['bl'] == tic and tic_dic['bm'] == tic and tic_dic['br'] == tic:
            print(tic, "Wins the game!", sep=", ")
            exit()
        elif tic_dic['tl'] == tic and tic_dic['ml'] == tic and tic_dic['bl'] == tic:
            print(tic, "Wins the game!", sep=", ")
            exit()
        elif tic_dic['tm'] == tic and tic_dic['mm'] == tic and tic_dic['bm'] == tic:
            print(tic, "Wins the game!", sep=", ")
            exit()
        elif tic_dic['tr'] == tic and tic_dic['mr'] == tic and tic_dic['br'] == tic:
            print(tic, "Wins the game!", sep=", ")
            exit()
        elif tic_dic['tl'] == tic and tic_dic['mm'] == tic and tic_dic['br'] == tic:
            print(tic, "Wins the game!", sep=", ")
            exit()
        elif tic_dic['tr'] == tic and tic_dic['mm'] == tic and tic_dic['bl'] == tic:
            print(tic, "Wins the game!", sep=", ")
            exit()
        #  Rules of the game for 'O'
        elif tic_dic['tl'] == tac and tic_dic['tm'] == tac and tic_dic['tr'] == tac:
            print(tac, "Wins the game!", sep=", ")
            exit()
        elif tic_dic['ml'] == tac and tic_dic['mm'] == tac and tic_dic['mr'] == tac:
            print(tac, "Wins the game!", sep=", ")
            exit()
        elif tic_dic['bl'] == tac and tic_dic['bm'] == tac and tic_dic['br'] == tac:
            print(tac, "Wins the game!", sep=", ")
            exit()
        elif tic_dic['tl'] == tac and tic_dic['ml'] == tac and tic_dic['bl'] == tac:
            print(tac, "Wins the game!", sep=", ")
            exit()
        elif tic_dic['tm'] == tac and tic_dic['mm'] == tac and tic_dic['bm'] == tac:
            print(tac, "Wins the game!", sep=", ")
            exit()
        elif tic_dic['tr'] == tac and tic_dic['mr'] == tac and tic_dic['br'] == tac:
            print(tac, "Wins the game!", sep=", ")
            exit()
        elif tic_dic['tl'] == tac and tic_dic['mm'] == tac and tic_dic['br'] == tac:
            print(tac, "Wins the game!", sep=", ")
            exit()
        elif tic_dic['tr'] == tac and tic_dic['mm'] == tac and tic_dic['bl'] == tac:
            print(tac, "Wins the game!", sep=", ")
            exit()

        sleep(1)
        response = ['my turn!', 'prepare your soul', "I'm coming to get ya!", "boy you're dumb", "okay cool",
                    "I see what ya doing", "clever huh..."]
        print(random.choice(response))
        sleep(1)
        tic_dic[comp()] = tac
        board()
        rotations += 1
    #  Game over all values filled
    print("Game Over, guess we both lost this one")
    exit()


# Comp function will hold the random logic for computer to play against
def comp():
    keys = list(tic_dic.keys())
    computer_choice = random.choice(keys)
    #  comps random logic
    while True:
        #  if tic_dic -> 'key'(randomly picked by computer) is " " empty then return 'key' -> rules_for_comp
        if tic_dic[computer_choice] == " ":
            return computer_choice
        else:
            # print(f"Aww nope, {computer_choice} is already taken")
            computer_choice = random.choice(keys)
            continue


def intro():
    while True:
        #  initial choice on which kind of TicTacToe user want's to play
        choice = input("Let's see,\nwhich game of Tic-Tac-Toe would you like to play. \nHuman or Computer? ")
        choice = choice.lower()
        #  print board to screen
        board()

        if choice == 'human':
            print("Awesome")
            rules_for_users()
        elif choice == 'computer':
            print("Oh, me.... hahaha okay, sure!")
            rules_for_comp()
        else:
            print("\n*****Please type 'Human' or 'Computer'******")
        continue


intro()
