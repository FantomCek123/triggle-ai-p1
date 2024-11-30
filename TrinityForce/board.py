import copy
import os

from numpy.ma.extras import row_stack

size = 4
tab = '    '
half_tab = '  '
d_bond = '--------'


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
            print(f"Potez {direction} sa ({row_char}, {column_char}) je validan.")
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
            print(f"Potez {direction} sa ({row_char}, {column_char}) je validan.")
            return True
        else:
            print(f"Potez {direction} nije validan.")
            return False

    elif direction == "D":
        if column + 3 < len(board[row]):
            print(f"Potez {direction} sa ({row_char}, {column_char}) je validan.")
            return True
        else:
            print(f"Potez {direction} nije validan.")
    else:
            print(f"Potez {direction} nije validan.")
            return False

def deleteDuplicates(moves):
    # prepraviti
    grouped = {}
    for move in moves:
        key = move[1]
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(move)

    result = []
    for group in grouped.values():
        max_move = max(group, key=lambda x: x[3])
        result.append(max_move)
    return result


def filter_moves_with_max_x3(moves):
    max_moves = {}

    for move in moves:
        key = (move[0].upper(), move[1], move[2])
        if key not in max_moves or move[3] > max_moves[key][3]:
            max_moves[key] = move
    return list(max_moves.values())


def printDLAndDDMovesAndUpdateMoveList(dd_dl_moves, row, shift, center):
    to_print = "" #zbog slova...
    flagged = []
    dd_dl_moves = filter_moves_with_max_x3(dd_dl_moves)
    for index, move in enumerate(dd_dl_moves):
        if move[2].upper() == "DD":
            if index == 0:
                to_print += f" {tab * (shift + 1 + 2 * (move[1] - 1))}" #jedan space je namerno zbog slova...
                if move[1] > 1: to_print += f"{(move[1] - 1) * " "}"
            else:
                new = f" {tab * (shift + 1 + 2 * (move[1] - 1))}"
                if move[1] > 1: new += f"{(move[1] - 1) * " "}"
                to_print = to_print + new[len(to_print):]
            to_print += "  \\"
            move[3] -= 1
            if move[3] == 0:
                flagged.append(index) # dd_dl_moves.pop(index)
            else:
                if row < center:
                    dd_dl_moves[index] = [chr(row + 1 + 65), move[1] + 1, move[2], move[3]]
                else:
                    dd_dl_moves[index] = [chr(row + 1 + 65), move[1], move[2], move[3]]

        elif move[2].upper() == "DL":
            if index == 0:
                to_print += f" {tab * (shift + 2 * (move[1] - 1))}" #jedan space je namerno zbog slova...
                if move[1] > 1: to_print += f"{(move[1] - 1) * " "}"
            else:
                new = f" {tab * (shift + 2 * (move[1] - 1))}"
                if move[1] > 1: new += f"{(move[1] - 1) * " "}"
                to_print = to_print + new[len(to_print):]
            to_print += half_tab + '/'
            move[3] -= 1
            if move[3] == 0:
               flagged.append(index)# dd_dl_moves.pop(index) #ovde ga sjebe dal zbog enumerate bem li ga
            else:
                if row >= center:
                    dd_dl_moves[index] = [chr(row + 1 + 65), move[1] - 1, move[2], move[3]]
                else:
                    dd_dl_moves[index] = [chr(row + 1 + 65), move[1], move[2], move[3]]

    print(to_print)
    for index in sorted(flagged, reverse=True):
        dd_dl_moves.pop(index)
    return dd_dl_moves

# postoji mali bug... prepraviti
def printDMoves(moves, dot_number, row, shift):
    beg = f"{chr(row + 65)}{tab}"
    to_print = f"{chr(row + 65)}{tab}"
    flagged = []
    # msm da je najbolje da se proveri za svaki slucaj da li ima duplikata i ako ima da ostane 1 u niz
    # f"{chr(i + 65)}{tab}" + f"{tab}" * shift + f"{2 * tab}"
    for dot in range(dot_number):
        for index, move in enumerate(moves):
            if move[1] == dot + 1:
                new = beg + shift * tab + dot * 2 * tab
                if move[1] > 1: new += f"{(move[1] - 1) * " "}"
                new += "." + d_bond
                to_print = to_print + new[len(to_print):]
                move[3] -= 1
                move[1] += 1
                if move[3] == 0:
                    flagged.append(index)
            else:
                new = beg + shift * tab + dot * 2 * tab
                if move[1] > 1: new += f"{(move[1] - 1) * " "}"
                new += "." + 2 * tab
                to_print = to_print + new[len(to_print):]

        #promeniti, ne bi trebalo vise od 2 ista da ima...
        for flag in sorted(flagged, reverse=True):
            moves.pop(flag)
        if len(moves) == 0:
            to_print += '.'
            break
        moves = deleteDuplicates(moves)
    print(to_print)
    return


def printBoard(board, size, moves):
    center = size - 1
    #ovo treba dodraditi da printa / i - prilikom dodavanja poteza
    for i, cells in enumerate(board):
        if i < center:
            shift = size - 1 - i
        else:
            shift = i - center
        #printDMoves(len(cells), i, shift)
        d_moves = [move for move in moves if ord(move[0].upper()) - 65 == i and move[2].upper() == "D"]
        d_moves.sort(key=lambda x: int(x[1]))
        moves =  [item for item in moves if item not in d_moves]
        if len(d_moves) > 0:
            printDMoves(d_moves, len(cells), i, shift)
        else:
            print(f"{chr(i + 65)}{tab}" + f"{tab}" * shift + f"{2 * tab}".join(cells))
        dd_dl_for_row = [move for move in moves if ord(move[0].upper()) - 65 == i and (move[2].upper() == "DD" or move[2].upper() == "DL")]
        remaining_moves =  [item for item in moves if item not in dd_dl_for_row]
        dd_dl_for_row.sort(key = lambda x: (x[1], 0 if x[2].upper() == "DL" else 1))

        moves = printDLAndDDMovesAndUpdateMoveList(dd_dl_for_row, i, shift, center) + remaining_moves

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
moves = [ ["a", 2, "dl", 3],["a", 3, "dd", 3],["b", 2, "dd", 3], ["d", 3, "dd", 3], ["c", 3, "dl", 3] ,["d", 7, "dl", 3] ]
#["a", 1, "dl", 3], ["a", 4, "dd", 3]
old_moves = copy.deepcopy(moves)
printBoard(tabla, size, moves)
while True:
    moves = copy.deepcopy(old_moves)
    user_input = input("Unesite podatke (format: red(A, B, ...) kolona(1, 2, ...) potez(DD,D,DL)): ")

    parts = user_input.split()

    move = [parts[0], parts[1], parts[2]]
    if validateMove(move, tabla):
        to_draw = 3
        move.append(to_draw)
        moves.append(move)
        move[1] = int(move[1])
        old_moves = copy.deepcopy(moves)
        os.system('cls' if os.name == 'nt' else 'clear')
        printBoard(tabla, size, moves)


