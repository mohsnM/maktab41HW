from abc import abstractmethod


class Piece:
    def __init__(self, color, x, y):
        self._color = color
        self._x = x
        self._y = y
        self._moveable = []

    @abstractmethod
    def movement(self):
        pass

    def change_x_y(self, x, y):
        self._moveable = []
        self._x = x
        self._y = y


class King(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def movement(self):
        if self._x < 7:
            self._moveable.append([self._x + 1, self._y])
            if self._y < 7:
                self._moveable.append([self._x + 1, self._y + 1])
        if self._x > 0:
            self._moveable.append([self._x - 1, self._y])
            if self._y > 0:
                self._moveable.append([self._x - 1, self._y - 1])
        if self._y < 7:
            self._moveable.append([self._x, self._y + 1])
            if self._x > 0:
                self._moveable.append([self._x - 1, self._y + 1])
        if self._y > 0:
            self._moveable.append([self._x, self._y - 1])
            if self._x < 7:
                self._moveable.append([self._x + 1, self._y - 1])
        return self._moveable


class Queen(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def movement(self):
        ymp = self._y
        xmp = self._x
        while xmp < 7:
            xmp += 1
            self._moveable.append([xmp, ymp])
            while ymp < 7:
                ymp += 1
                self._moveable.append([xmp, ymp])
        ymp = self._y
        xmp = self._x
        while xmp > 0:
            xmp -= 1
            self._moveable.append([xmp, ymp])
            while ymp > 0:
                ymp -= 1
                self._moveable.append([xmp, ymp])
        ymp = self._y
        xmp = self._x
        while ymp < 7:
            ymp += 1
            self._moveable.append([xmp, ymp])
            while xmp > 0:
                xmp -= 1
                self._moveable.append([xmp, ymp])
        ymp = self._y
        xmp = self._x
        while ymp > 0:
            ymp -= 1
            self._moveable.append([xmp, ymp])
            while xmp < 7:
                xmp += 1
                self._moveable.append([xmp, ymp])
        return self._moveable


class Bishop(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def movement(self):
        ymp = self._y
        xmp = self._x
        while xmp < 7 and ymp < 7:
            xmp += 1
            ymp += 1
            self._moveable.append([xmp, ymp])
        ymp = self._y
        xmp = self._x
        while xmp > 0 and ymp > 0:
            xmp -= 1
            ymp -= 1
            self._moveable.append([xmp, ymp])
        ymp = self._y
        xmp = self._x
        while ymp < 7 and xmp > 0:
            ymp += 1
            xmp -= 1
            self._moveable.append([xmp, ymp])
        ymp = self._y
        xmp = self._x
        while ymp > 0 and xmp < 7:
            ymp -= 1
            xmp += 1
            self._moveable.append([xmp, ymp])
        return self._moveable


class Knight(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def movement(self):
        if self._x < 7 and self._y > 1:
            self._moveable.append([self._x + 1, self._y - 2])
        if self._x < 7 and self._y < 6:
            self._moveable.append([self._x + 1, self._y + 2])
        if self._x > 0 and self._y > 1:
            self._moveable.append([self._x - 1, self._y - 2])
        if self._x > 0 and self._y < 6:
            self._moveable.append([self._x - 1, self._y + 1])
        if self._x > 1 and self._y < 7:
            self._moveable.append([self._x - 2, self._y + 1])
        if self._x < 6 and self._y < 7:
            self._moveable.append([self._x + 2, self._y + 1])
        if self._x > 1 and self._y > 0:
            self._moveable.append([self._x - 2, self._y - 1])
        if self._x < 6 and self._y > 0:
            self._moveable.append([self._x + 2, self._y - 1])
        return self._moveable


class Rook(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def movement(self):
        xmp = self._x
        while xmp < 7:
            xmp += 1
            self._moveable.append([xmp, self._y])
        xmp = self._x
        while xmp > 0:
            xmp -= 1
            self._moveable.append([xmp, self._y])
        ymp = self._y
        while ymp < 7:
            ymp += 1
            self._moveable.append([self._x, ymp])
        ymp = self._y
        while ymp > 0:
            ymp -= 1
            self._moveable.append([self._x, ymp])
        return self._moveable


class Pawn(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def movement(self):
        if self._color == 'b' and self._x < 7:
            self._moveable.append([self._x + 1, self._y])
        elif self._color == 'w' and self._x > 0:
            self._moveable.append([self._x - 1, self._y])
        return self._moveable


class Square:
    kiw, kib = King('w', 7, 4), King('b', 0, 3)
    qw, qb = Queen('w', 7, 3), Queen('b', 0, 4)
    bw1, bw2, bb1, bb2 = Bishop('w', 7, 2), Bishop('w', 7, 5), Bishop('b', 0, 2), Bishop('b', 0, 5)
    kw1, kw2, kb1, kb2 = Knight('w', 7, 1), Knight('w', 7, 6), Knight('b', 0, 1), Knight('b', 0, 6)
    rw1, rw2, rb1, rb2 = Rook('w', 7, 0), Rook('w', 7, 7), Rook('b', 0, 0), Rook('b', 0, 7)
    pw1, pw2, pw3, pw4 = Pawn('w', 6, 0), Pawn('w', 6, 1), Pawn('w', 6, 2), Pawn('w', 6, 3)
    pw5, pw6, pw7, pw8 = Pawn('w', 6, 4), Pawn('w', 6, 5), Pawn('w', 6, 6), Pawn('w', 6, 7)
    pb1, pb2, pb3, pb4 = Pawn('b', 1, 0), Pawn('b', 1, 1), Pawn('b', 1, 2), Pawn('b', 1, 3)
    pb5, pb6, pb7, pb8 = Pawn('b', 1, 4), Pawn('b', 1, 5), Pawn('b', 1, 6), Pawn('b', 1, 7)

    def set_new_index(self, piece, x, y):
        return eval(f"self.{piece}.change_x_y({x}, {y})")


class Board(Square):
    def __init__(self):
        self.ch_b = (['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])

    def set_reset(self):
        self.ch_b[7][4], self.ch_b[0][3], self.ch_b[7][3], self.ch_b[0][4] = 'kiw', 'kib', 'qw', 'qb'
        self.ch_b[7][2], self.ch_b[7][5], self.ch_b[0][2], self.ch_b[0][5] = 'bw1', 'bw2', 'bb1', 'bb2'
        self.ch_b[7][1], self.ch_b[7][6], self.ch_b[0][1], self.ch_b[0][6] = 'kw1', 'kw2', 'kb1', 'kb2'
        self.ch_b[7][0], self.ch_b[7][7], self.ch_b[0][0], self.ch_b[0][7] = 'rw1', 'rw2', 'rb1', 'rb2'
        self.ch_b[6][0], self.ch_b[6][1], self.ch_b[6][2], self.ch_b[6][3] = 'pw1', 'pw2', 'pw3', 'pw4'
        self.ch_b[6][4], self.ch_b[6][5], self.ch_b[6][6], self.ch_b[6][7] = 'pw5', 'pw6', 'pw7', 'pw8'
        self.ch_b[1][0], self.ch_b[1][1], self.ch_b[1][2], self.ch_b[1][3] = 'pb1', 'pb2', 'pb3', 'pb4'
        self.ch_b[1][4], self.ch_b[1][5], self.ch_b[1][6], self.ch_b[1][7] = 'pb5', 'pb6', 'pb7', 'pb8'
        return self.ch_b

    def change_index(self):
        x, y = map(int, input("Enter first index: ").split())
        while self.ch_b[x][y] == '   ':
            print("there is empty: ")
            x, y = map(int, input("Enter first index: ").split())
        temp = self.ch_b[x][y]
        move_index = eval(f"self.{temp}.movement()")
        print("You can move there: ")
        print(move_index)
        i, j = map(int, input("Enter second index: ").split())
        while [i, j] not in move_index:
            i, j = map(int, input("Enter moveable index: ").split())
        self.set_new_index(temp, i, j)
        self.ch_b[x][y], self.ch_b[i][j] = self.ch_b[i][j], self.ch_b[x][y]
        return

    def table_show(self):
        for x in self.ch_b:
            print(x)
        return


if '__main__' == __name__:
    c = Board()
    c.set_reset()
    c.table_show()
    c.change_index()
    c.table_show()
