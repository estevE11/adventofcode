data = open("input.txt", "r").read().split("\n")

numbers = data[0].split(",")

class Board:
    def parse(self, board_data):
        self.data = board_data
        self.checked = [
            [False,False,False,False,False],
            [False,False,False,False,False],
            [False,False,False,False,False],
            [False,False,False,False,False],
            [False,False,False,False,False]
        ]
    
    def checkNumber(self, number):
        for y in range(5):
            for x in range(5):
                if int(self.data[y][x]) == int(number):
                    self.checked[y][x] = True
                    return self.checkWin(x, y, int(number))
        return 0
        
    def checkWin(self, x, y, number):
        win = True

        for xx in range(5):
            if not self.checked[y][xx]:
                win = False

        if win:
            return self.get_result(number)

        for yy in range(5):
            if not self.checked[yy][x]:
                win = False

        if win:
            return self.get_result(number)
        
        return 0
    
    def get_result(self, number):
        res = 0
        for y in range(5):
            for x in range(5):
                if not self.checked[y][x]:
                    res += int(self.data[y][x])
        return res*int(number)


    def print_board_checked(self):
        for y in range(5):
            for x in range(5):
                print((1 if self.checked[y][x] else 0), end=" ")
            print("")

    def print_board(self):
        for y in range(5):
            for x in range(5):
                print(self.data[y][x], end=" ")
            print("")

boards = []
curr_board = []

for i in range(2, len(data)):
    if len(data[i]) == 0:
        board = Board()
        board.parse(curr_board)
        boards.append(board)
        curr_board = []
    else:
        row = data[i].split(" ")
        row = [x for x in row if x != ""]
        curr_board.append(row)

board = Board()
board.parse(curr_board)
boards.append(board)

def calc(numbers, boards):
    for it in numbers:
        for board in boards:
            res = board.checkNumber(it)
            if res != 0:
                board.print_board()
                board.print_board_checked()
                return res

print(calc(numbers, boards))