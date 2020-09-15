from HW4_Maktab41.level_one import set_index_one
from HW4_Maktab41.level_tow import set_index_tow
from HW4_Maktab41.body_of_game import *


# this make better visual for game
def graphical():
    print()
    print("{} | {} | {}".format(L[0][0], L[0][1], L[0][2]))
    print("{} | {} | {}".format(L[1][0], L[1][1], L[1][2]))
    print("{} | {} | {}".format(L[2][0], L[2][1], L[2][2]))
    print()


# this is final function for level one
def main_one():
    while True:
        for z in range(5):
            graphical()
            get_index()
            usr = check_usr()
            if usr == 1:
                return 1
            elif z == 4:
                return 0
            set_index_one()
            cpu = check_cpu()
            if cpu == -1:
                return -1


# this is final function for level tow
def main_tow():
    while True:
        for z in range(5):
            graphical()
            get_index()
            usr = check_usr()
            if usr == 1:
                return 1
            elif z == 4:
                return 0
            set_index_tow()
            cpu = check_cpu()
            if cpu == -1:
                return -1


# for check level and run final function
def start_game():
    finl = 0
    lvl = int(input("Enter your level as you want play (1 or 2) >>> "))
    if lvl == 1:
        finl = main_one()
    elif lvl == 2:
        finl = main_tow()
    print()
    if finl == 1:
        print('===^=^=== Congratulation!`You win ===^=^===')
    elif finl == 0:
        print("End game! The match draw")
    elif finl == -1:
        print("---_-_--- Sorry! You lose ---_-_---")
    graphical()


start_game()
