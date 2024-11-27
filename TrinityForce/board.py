size = 5


def validateMove(move, board):
    if len(move) != 3:
        print("Nevalidan potez: Nepotpun unos!")
        return False

    center_row = size - 1
    row_char, column_char, direction = move
    row = ord(row_char.upper()) - 65
    if not column_char.isdigit():
        print("Nevalidan potez: Kolona mora biti broj!")
        return False
    column = int(column_char)
    column -= 1

    direction = direction.upper()

    if row < 0 or row >= len(board) or column < 0 or column >= len(board[row]):
        print("Nevalidan potez: Pocetna pozicija je izvan granica table!")
        return False

    # moze se malo refaktorisati da bude bolje i citljivije, kod granicnih slucajeva pogotovo i da izadje odma kad 
    # nadje da nije validan al me jako mrzi, ipak su u pitanju 4 iteracije...
    if direction == "DD":
        valid = True
        for i in range(3):
            if row + i >= center_row:
                if row + i + 1 >= len(board) or len(board[row + i + 1]) <= column:
                    valid = False
            else:
                if column + 1 >= len(board[row + i + 1]):
                    valid = False
                column += 1
        if valid:
            print(f"Potez {direction} sa ({row_char}, {column}) je validan.")
            return True
        else:
            print(f"Potez {direction} nije validan.")
            return False

    elif direction == "DL":
        valid = True
        for i in range(4):
            if row + i <= center_row:
                continue
            else:
                if column - 1 < 0:
                    valid = False
                column -= 1
        if valid:
            print(f"Potez {direction} sa ({row_char}, {column}) je validan.")
            return True
        else:
            print(f"Potez {direction} nije validan.")
            return False

    elif direction == "D":
        if column - 1 + 3 < len(board[row]):
            print(f"Potez {direction} sa ({row_char}, {column}) je validan.")
            return True
    else:
            print(f"Potez {direction} nije validan.")
            return False



def printBoard(board, size):
    center = size - 1
    #ovo treba dodraditi da printa / i - prilikom dodavanja poteza
    for i, cells in enumerate(board):
        if i < center:
            shift = size - 1 - i
        else:
            shift = i - center
        print(f"{chr(i + 65)}\t" + "\t" * shift + "\t\t".join(cells))
        print()

def makeBoard(size: int):
    if 4 <= size <= 8:
        board = []
        center = size * 2 - 1
        for i in range(size):
            board.append(["."] * (size + i))

        for i in range(1, size):
            board.append(["."] * (center - i))
        return board
    else:
        print('Losa velicina tabele! - postavi velicinu od 4 do 8!')
        return

tabla = makeBoard(size)
printBoard(tabla, size)
potez = ('d', '6', 'dd')
validateMove(potez, tabla)
while True:
    user_input = input("Unesite podatke (format: red(A, B, ...) kolona(1, 2, ...) potez(DD,D,DL)): ")

    parts = user_input.split()

    move = (parts[0], parts[1], parts[2])
    validateMove(move, tabla)