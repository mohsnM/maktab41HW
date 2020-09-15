from HW4_Maktab41.body_of_game import L


# check x axis it is dangerous
def x_axis(n):                                       # n is count of X in axis
    r = 0
    while r < 3:
        c = 0
        ls = []
        while c < 3:
            ls.append(L[r][c])
            c += 1
            if ls.count('X') == n and ls.__contains__(''):
                ix = ls.index('')
                L[r][ix] = 'O'
                return L
        r += 1


# check y axis it is dangerous
def y_axis(n):                                         # n is count of X in axis
    c = 0
    while c < 3:
        ls = []
        r = 0
        while r < 3:
            ls.append(L[r][c])
            r += 1
            if ls.count('X') == n and ls.__contains__(''):
                iy = ls.index('')
                L[iy][c] = 'O'
                return L
        c += 1


# check z axis it is dangerous
def z_axis(n):                                          # n is count of X in axis
    ls = []
    r, c = 0, 0
    while r < 3:
        ls.append(L[r][c])
        r += 1
        c += 1                                                               # *
        if ls.count('X') == n and ls.__contains__(''):            # for check  # *  axis
            iz = ls.index('')                                                    # *
            L[iz][iz] = 'O'
            return L
    ls = []
    r, c = 0, 2
    while r < 3:
        ls.append(L[r][c])
        r += 1
        c -= 1                                                                   # *
        if ls.count('X') == n and ls.__contains__(''):            # for check  # *  axis
            iz = ls.index('')                                                # *
            if iz == 0:
                L[0][2] = 'O'
            elif iz == 1:
                L[1][1] = 'O'
            elif iz == 2:
                L[2][0] = 'O'
            return L


# call all func for check best place for set index
def set_index_tow():
    xa = x_axis(2)                                      # for many action from user
    if xa:
        return xa
    ya = y_axis(2)
    if ya:
        return ya
    za = z_axis(2)
    if za:
        return za
    xa = x_axis(1)                                      # for first 2 or more action
    if xa:
        return xa
    ya = y_axis(1)
    if ya:
        return ya
    za = z_axis(1)
    if za:
        return za
