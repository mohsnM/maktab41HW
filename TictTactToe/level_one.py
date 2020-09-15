from HW4_Maktab41.body_of_game import L
from random import randint


# check the index of cpu enter is empty or not
def cpu_validation():
    i, j = randint(0, 2), randint(0, 2)
    while L[i][j] != '':
        i, j = randint(0, 2), randint(0, 2)
    else:
        return i, j


# get index from cpu
def set_index_one():
    i, j = cpu_validation()
    L[i][j] = 'O'
    return L