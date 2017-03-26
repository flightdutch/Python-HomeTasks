import random


class BoardPlayer(object):
    def next_move(self):
        pass


class BoardGame(BoardPlayer):
    def create_board(self):
        pass

    def move(self):
        pass

    def check_win(self):
        pass

    def __init__(self):
        self.d = int(input("Длина доски равна "))
        self.h = int(input("Ширина доски равна "))
        self.board = []
        for i in range(self.d):
            self.board.append([])
            for j in range(self.h):
                self.board[i].append('.')
        self.print_board()
        self.count = 0
        self.c = None
        while self.c not in ('x', 'o'):
            self.c = input("Символ - ")
        if self.d > self.h:
            c = self.h
        else:
            c = self.d
        self.n = 0
        while (self.n < 3) or (self.n > c):
            self.n = int(input("Введите количество элементов "))
        self.turn = self.c

    def main_loop(self, player1, player2):
        while self.count < self.d * self.h:
            self.count += 1
            # наш ход
            print("Игрок:")
            while not game.move(*player1.next_move()):  # * распаковывает массив
                pass
            if self.check_win() == True:
                break
            # ход компа
            print("Компьютер:")
            while not game.move(*player2.get_possible_moves(self.board, self.d, self.h)):
                pass
            if self.check_win() == True:
                break

    def print_board(self):
        for i in range(self.d):
            for j in range(self.h):
                print(self.board[i][j],)
            print()


class XOGame(BoardGame):
    def move(self, x, y):
        if x < self.d and y < self.h and self.board[x][y] == '.':
            if (self.turn == 'x'):
                self.board[x][y] = 'x'
                self.turn = 'o'
            else:
                self.board[x][y] = 'o'
                self.turn = 'x'

            self.print_board()
            return True

        else:
            print('ERROR!')
            print('Введите координаты еще раз')
            return False

    def check_win(self):
        buf = self.c
        if self.turn == 'x':
            buf = 'o'
        else:
            buf = 'x'
        # проверка горизонталей
        for i in range(self.d):
            # print
            for j in range(self.h - (self.n - 1)):
                # print i,j,i,j+1,i,j+2
                for l in range(self.n):
                    if buf != self.board[i][j + l]:
                        break
                    if l == self.n - 1:
                        print('Победа!')
                        return True
        # проверка вертикалей
        for i in range(self.h):
            # print
            for j in range(self.d - (self.n - 1)):
                # print j,i,j+1,i,j+2,i
                for l in range(self.n):
                    if buf != self.board[j + l][i]:
                        break
                    if l == self.n - 1:
                        print('Победа!')
                        return True
        # проверка диагоналей
        for i in range(self.d - self.n + 1):
            for j in range(self.h):
                if self.check_win_1(self.board, self.n, buf, i, j, 1, 1) == True:
                    print('Победа!')
                    return True
                if self.check_win_1(self.board, self.n, buf, i, j, 1, -1) == True:
                    print('Победа!')
                    return True

    def check_win_1(self, board, n, buf, i, j, i1, j1):
        for l in range(n):
            if i >= self.d or j >= self.h or i < 0 or j < 0:
                return False
            if buf != board[i][j]:
                return False
            if l == n - 1:
                return True
            i += i1
            j += j1


class XOPlayer(BoardPlayer):
    def print_board():
        pass

    def ask_human():
        pass

    def next_move(self):
        x = int(input("x: ")) - 1
        y = int(input("y: ")) - 1
        return x, y


class XOAI(BoardPlayer):
    def get_possible_moves(self, board, d, h):
        l = []
        for i in range(d):
            for j in range(h):
                if (board[i][j] == '.'):
                    l.append([i, j])
        return random.choice(l)


game = XOGame()
player1 = XOPlayer()
player2 = XOAI()
game.main_loop(player1, player2)