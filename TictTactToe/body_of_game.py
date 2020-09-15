L = [['', '', ''], ['', '', ''], ['', '', '']]


# check the index of user enter is empty or not
def usr_validation():
    i, j = map(int, input("Enter index of your goal >>> ").split())
    while i > 2 or i < 0:
        print("Oops! rows out of range, ", end='')
        i = int(input("Try enter rows >>> "))
    while j > 2 or j < 0:
        print("Oops! column out of range, ", end='')
        j = int(input("Try enter column >>> "))
    while L[i][j] != '':
        print("Oops! there is not empty, ", end='')
        i, j = map(int, input("Try again >>> ").split())
    else:
        return i, j


# get index from user
def get_index():
    i, j = usr_validation()
    L[i][j] = 'X'
    return L


# check x axis, are they equal or not
def x_axis(rul):
    r = 0
    while r != 3:
        if L[r][0] == rul and L[r][1] == rul and L[r][2] == rul:
            return 0
        else:
            r += 1
    return -1


# check y axis, are they equal or not
def y_axis(rul):
    c = 0
    while c != 3:
        if L[0][c] == rul and L[1][c] == rul and L[2][c] == rul:
            return 0
        else:
            c += 1
    return -1


# check z axis, are they equal or not
def z_axis(rul):
    if L[0][0] == rul and L[1][1] == rul and L[2][2] == rul:
        return 0
    elif L[0][2] == rul and L[1][1] == rul and L[2][0] == rul:
        return 0
    return -1


# get result for user
def check_usr():
    x = x_axis('X')
    if x == 0:
        return 1
    y = y_axis('X')
    if y == 0:
        return 1
    z = z_axis('X')
    if z == 0:
        return 1


# get result for cpu
def check_cpu():
    x = x_axis('O')
    if x == 0:
        return -1
    y = y_axis('O')
    if y == 0:
        return -1
    z = z_axis('O')
    if z == 0:
        return -1