from abc import abstractmethod


class Piece:
    def __init__(self, color):
        self._color = color
        self._moveable = []

    @abstractmethod
    def movement(self, x, y):
        pass


class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def movement(self, x, y):
        if x < 7:
            self._moveable.append([x + 1, y])
            if y < 7:
                self._moveable.append([x + 1, y + 1])
        if x > 0:
            self._moveable.append([x - 1, y])
            if y > 0:
                self._moveable.append([x - 1, y - 1])
        if y < 7:
            self._moveable.append([x, y + 1])
            if x > 0:
                self._moveable.append([x - 1, y + 1])
        if y > 0:
            self._moveable.append([x, y - 1])
            if x < 7:
                self._moveable.append([x + 1, y - 1])
        return self._moveable


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def movement(self, x, y):
        ymp = y
        xmp = x
        while xmp < 7:
            xmp += 1
            self._moveable.append([xmp, ymp])
            while ymp < 7:
                ymp += 1
                self._moveable.append([xmp, ymp])
        ymp = y
        xmp = x
        while xmp > 0:
            xmp -= 1
            self._moveable.append([xmp, ymp])
            while ymp > 0:
                ymp -= 1
                self._moveable.append([xmp, ymp])
        ymp = y
        xmp = x
        while ymp < 7:
            ymp += 1
            self._moveable.append([xmp, ymp])
            while xmp > 0:
                xmp -= 1
                self._moveable.append([xmp, ymp])
        ymp = y
        xmp = x
        while ymp > 0:
            ymp -= 1
            self._moveable.append([xmp, ymp])
            while xmp < 7:
                xmp += 1
                self._moveable.append([xmp, ymp])
        return self._moveable


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)

    def movement(self, x, y):
        ymp = y
        xmp = x
        while xmp < 7 and ymp < 7:
            xmp += 1
            ymp += 1
            self._moveable.append([xmp, ymp])
        ymp = y
        xmp = x
        while xmp > 0 and ymp > 0:
            xmp -= 1
            ymp -= 1
            self._moveable.append([xmp, ymp])
        ymp = y
        xmp = x
        while ymp < 7 and xmp > 0:
            ymp += 1
            xmp -= 1
            self._moveable.append([xmp, ymp])
        ymp = y
        xmp = x
        while ymp > 0 and xmp < 7:
            ymp -= 1
            xmp += 1
            self._moveable.append([xmp, ymp])
        return self._moveable


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

    def movement(self, x, y):
        if x < 7 and y > 1:
            self._moveable.append([x + 1, y - 2])
        if x < 7 and y < 6:
            self._moveable.append([x + 1, y + 2])
        if x > 0 and y > 1:
            self._moveable.append([x - 1, y - 2])
        if x > 0 and y < 6:
            self._moveable.append([x - 1, y + 1])
        if x > 1 and y < 7:
            self._moveable.append([x - 2, y + 1])
        if x < 6 and y < 7:
            self._moveable.append([x + 2, y + 1])
        if x > 1 and y > 0:
            self._moveable.append([x - 2, y - 1])
        if x < 6 and y > 0:
            self._moveable.append([x + 2, y - 1])
        return self._moveable


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)

    def movement(self, x, y):
        xmp = x
        while xmp < 7:
            xmp += 1
            self._moveable.append([xmp, y])
        xmp = x
        while xmp > 0:
            xmp -= 1
            self._moveable.append([xmp, y])
        ymp = y
        while ymp < 7:
            ymp += 1
            self._moveable.append([x, ymp])
        ymp = y
        while ymp > 0:
            ymp -= 1
            self._moveable.append([x, ymp])
        return self._moveable


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)

    def movement(self, x, y):
        if self._color == 'b' and x < 7:
            self._moveable.append([x + 1, y])
        elif self._color == 'w' and x > 0:
            self._moveable.append([x - 1, y])
        return self._moveable


class Square:
    kiw, kib = King('w'), King('b')
    qw, qb = Queen('w'), Queen('b')
    bw1, bw2, bb1, bb2 = Bishop('w'), Bishop('w'), Bishop('b'), Bishop('b')
    kw1, kw2, kb1, kb2 = Knight('w'), Knight('w'), Knight('b'), Knight('b')
    rw1, rw2, rb1, rb2 = Rook('w'), Rook('w'), Rook('b'), Rook('b')
    pw1, pw2, pw3, pw4 = Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w')
    pw5, pw6, pw7, pw8 = Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w')
    pb1, pb2, pb3, pb4 = Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b')
    pb5, pb6, pb7, pb8 = Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b')


class Board(Square):
    def __init__(self):
        self.chess_board = (['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
                            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
                            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
                            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
                            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
                            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
                            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
                            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])

    def set_reset(self):                                                          # set piece to their main index
        self.chess_board = [list(map(lambda x: '   ', r)) for r in self.chess_board]
        self.chess_board[7][4], self.chess_board[0][3], self.chess_board[7][3], self.chess_board[0][4] = 'kiw', 'kib', 'qw', 'qb'
        self.chess_board[7][2], self.chess_board[7][5], self.chess_board[0][2], self.chess_board[0][5] = 'bw1', 'bw2', 'bb1', 'bb2'
        self.chess_board[7][1], self.chess_board[7][6], self.chess_board[0][1], self.chess_board[0][6] = 'kw1', 'kw2', 'kb1', 'kb2'
        self.chess_board[7][0], self.chess_board[7][7], self.chess_board[0][0], self.chess_board[0][7] = 'rw1', 'rw2', 'rb1', 'rb2'
        self.chess_board[6][0], self.chess_board[6][1], self.chess_board[6][2], self.chess_board[6][3] = 'pw1', 'pw2', 'pw3', 'pw4'
        self.chess_board[6][4], self.chess_board[6][5], self.chess_board[6][6], self.chess_board[6][7] = 'pw5', 'pw6', 'pw7', 'pw8'
        self.chess_board[1][0], self.chess_board[1][1], self.chess_board[1][2], self.chess_board[1][3] = 'pb1', 'pb2', 'pb3', 'pb4'
        self.chess_board[1][4], self.chess_board[1][5], self.chess_board[1][6], self.chess_board[1][7] = 'pb5', 'pb6', 'pb7', 'pb8'
        return self.chess_board

    def change_index(self):
        x, y = list(map(int, input("Enter first index: ").split()))                     # check first index have piece
        while self.chess_board[x][y] == '   ':
            print("there is empty: ")
            x, y = list(map(int, input("Enter first index: ").split()))

        temp = self.chess_board[x][y]                                             # check the able index for move
        movement_index = eval(f"self.{temp}.movement({x}, {y})")
        moveable_index = []
        for d in movement_index:
            r, z = d
            if self.chess_board[r][z] == '   ':
                moveable_index.append([r, z])
        print("You can move there: ")
        print(moveable_index)

        i, j = map(int, input("Enter second index: ").split())                    # get and check second index
        while [i, j] not in movement_index:
            i, j = map(int, input("Enter moveable index: ").split())
        self.chess_board[x][y], self.chess_board[i][j] = self.chess_board[i][j], self.chess_board[x][y]       # change index
        return

    def table_show(self):                                                         # print board
        for x in self.chess_board:
            print(x)
        return


if '__main__' == __name__:
    c = Board()
    c.set_reset()
    c.table_show()
    c.change_index()
    c.table_show()

