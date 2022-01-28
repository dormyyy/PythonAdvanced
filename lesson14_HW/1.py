from abc import ABC, abstractmethod
plate = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}


class Figure(ABC):
    def __init__(self, color: str, position: list):
        self.c = color
        self.p = position

    def __str__(self):
        return f"figure is on the {self.p}"

    @abstractmethod
    def move(self, move_p):
        pass


class King(Figure):
    def __init__(self, color, position):
        super().__init__(color, position)

    def move(self, move_p):
        pf = self.p
        move_x = plate[f'{move_p[0]}']
        move_y = move_p[1]
        stay_x = plate[f'{self.p[0]}']
        stay_y = self.p[1]
        if abs(move_x - move_x) > 1 or abs(move_y - move_y) > 1:
            print('you can`t move here')
        else:
            self.p = move_p


class Pawn(Figure):
    def __init__(self, color, position):
        super().__init__(color, position)

    def move(self, move_p):
        pf = self.p
        move_x = plate[f'{move_p[0]}']
        move_y = move_p[1]
        stay_x = plate[f'{self.p[0]}']
        stay_y = self.p[1]
        if move_x != stay_x or abs(move_y - stay_y) > 1:
            print('you can`t move here')
        else:
            self.p = move_p


class Rook(Figure):
    def __init__(self, color, position):
        super().__init__(color, position)

    def move(self, move_p):
        pf = self.p
        move_x = plate[f'{move_p[0]}']
        move_y = move_p[1]
        stay_x = plate[f'{self.p[0]}']
        stay_y = self.p[1]
        if move_x != stay_x and move_y != stay_y:
            print('you can`t move here')
        else:
            self.p = move_p


class Bishop(Figure):
    def __init__(self, color, position):
        super().__init__(color, position)

    def move(self, move_p):
        pf = self.p
        move_x = plate[f'{move_p[0]}']
        move_y = move_p[1]
        stay_x = plate[f'{self.p[0]}']
        stay_y = self.p[1]
        if abs(move_x - stay_x) != abs(move_y - stay_y):
            print('you can`t move here')
        else:
            self.p = move_p


class Knight(Figure):
    def __init__(self, color, position):
        super().__init__(color, position)

    def move(self, move_p):
        pf = self.p
        move_x = plate[f'{move_p[0]}']
        move_y = move_p[1]
        stay_x = plate[f'{self.p[0]}']
        stay_y = self.p[1]
        if (abs(move_x - stay_x) == 1 and abs(move_y - stay_y) == 2) or \
                (abs(move_x - stay_x) == 2 and abs(move_y - stay_y) == 1):
            self.p = move_p
        else:
            print('you can`t move here')


class Queen(Figure):
    def __init__(self, color, position):
        super().__init__(color, position)

    def move(self, move_p):
        pf = self.p
        move_x = plate[f'{move_p[0]}']
        move_y = move_p[1]
        stay_x = plate[f'{self.p[0]}']
        stay_y = self.p[1]
        if (abs(move_x - stay_x) == abs(move_y - stay_y)) or ((move_x == stay_x) or (stay_y == move_y)):
            self.p = move_p
        else:
            print('you can`t move here')


king = King('black', ['a', 5])
king.move(['b', 6])
print(king)
pawn = Pawn('white', ['b', 7])
pawn.move(['b', 9])
print(pawn)
rook = Rook('black', ['c', 3])
rook.move(['b', 8])
print(rook)
bishop = Bishop('white', ['d', 5])
bishop.move(['f', 7])
print(bishop)
knight = Knight('black', ['c', 4])
knight.move(['d', 2])
print(knight)
queen = Queen('white', ['d', 5])
queen.move(['c', 4])
print(queen)
