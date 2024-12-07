import copy
import os
from collections import defaultdict

size = 4
tab = '    '
half_tab = '  '
d_bond = '--------'


def validateMove(move, board, moves):
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

	appanded_move = copy.deepcopy(move)
	appanded_move[1] = int(appanded_move[1])
	appanded_move.append(3)

	if appanded_move in moves:
		print("Ovaj potez je vec odigran!")
		return False

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
	# optimizovati
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


def triangle_under_column_occupied(triangles, column):
	triangles_n = []
	for triangle in triangles:
		if triangle[2] == column:
			triangles_n.append(triangle)
	return triangles_n


def printDLAndDDMovesAndUpdateMoveList(dd_dl_moves, row, shift, center, occupied_triangles):
	to_print = ""  # zbog slova...
	flagged = []
	dd_dl_moves = filter_moves_with_max_x3(dd_dl_moves)
	for index, move in enumerate(dd_dl_moves):
		if move[2].upper() == "DD":
			if index == 0:
				to_print += f" {tab * (shift + 1 + 2 * (move[1] - 1))}"  # jedan space je namerno zbog slova...
				if move[1] > 1: to_print += f"{(move[1] - 1) * ' '}"
			else:
				new = f" {tab * (shift + 1 + 2 * (move[1] - 1))}"
				if move[1] > 1: new += f"{(move[1] - 1) * ' '}"
				to_print = to_print + new[len(to_print):]
			t = triangle_under_column_occupied(occupied_triangles, move[1] - 1)
			if len(t) == 0:
				to_print += half_tab + '\\'
			elif len(t) == 1:
				to_print += " " + '\\'
				# edge case !!! !!!
				if move[1] == 1 and t[0][3] == True:
					to_print += half_tab + t[0][0]
			else:
				to_print += " " + '\\' + half_tab
				element = next((tr for tr in t if tr[3] is True), None)
				to_print += element[0]
			move[3] -= 1
			if move[3] == 0:
				flagged.append(index)
			else:
				if row < center:
					dd_dl_moves[index] = [chr(row + 1 + 65), move[1] + 1, move[2], move[3]]
				else:
					dd_dl_moves[index] = [chr(row + 1 + 65), move[1], move[2], move[3]]

		elif move[2].upper() == "DL":
			if index == 0:
				to_print += f" {tab * (shift + 2 * (move[1] - 1))}"  # jedan space je namerno zbog slova...
				if move[1] > 1: to_print += f"{(move[1] - 1) * ' '}"
			else:
				new = f" {tab * (shift + 2 * (move[1] - 1))}"
				if move[1] > 1: new += f"{(move[1] - 1) * ' '}"
				to_print = to_print + new[len(to_print):]
			to_print += half_tab + '/'
			x_or_o_arr = triangle_under_column_occupied(occupied_triangles, move[1] - 1)
			for x_or_o in x_or_o_arr:
				if x_or_o is not None:
					if not x_or_o[3]:
						to_print += ' ' + x_or_o[0]

			move[3] -= 1
			if move[3] == 0:
				flagged.append(index)  # dd_dl_moves.pop(index)
			else:
				if row >= center:
					dd_dl_moves[index] = [chr(row + 1 + 65), move[1] - 1, move[2], move[3]]
				else:
					dd_dl_moves[index] = [chr(row + 1 + 65), move[1], move[2], move[3]]

	print(to_print)
	for index in sorted(flagged, reverse=True):
		dd_dl_moves.pop(index)
	return dd_dl_moves


def printDMoves(moves, dot_number, row, shift):
	beg = f"{chr(row + 65)}{tab}"
	to_print = f"{chr(row + 65)}{tab}"
	flagged = []
	# msm da je najbolje da se proveri za svaki slucaj da li ima duplikata i ako ima da ostane 1 u niz
	# f"{chr(i + 65)}{tab}" + f"{tab}" * shift + f"{2 * tab}"
	for dot in range(dot_number):
		for index, move in enumerate(moves):
			if move[1] == dot + 1 and index not in flagged:
				new = beg + shift * tab + dot * 2 * tab
				if move[1] > 1: new += f"{(move[1] - 1) * ' '}"
				new += "*" + d_bond
				to_print = to_print + new[len(to_print):]
				move[3] -= 1
				move[1] += 1
				if move[3] == 0:
					flagged.append(index)
			else:
				new = beg + shift * tab + dot * 2 * tab
				if dot > 0: new += f"{dot * ' '}"
				new += "*" + 2 * tab
				to_print = to_print + new[len(to_print):]

		moves = deleteDuplicates(moves)
	print(to_print)
	return


# F-JE ZA ISCRTAVANJE SU OBJASNJENE NA KRAJU DOKUMENTACIJE !!!
def printBoard(board, moves=[], occupied_triangles=[]):
	size = len(board[0])
	center = size - 1
	for i, cells in enumerate(board):
		if i < center:
			shift = size - 1 - i
		else:
			shift = i - center
		# printDMoves(len(cells), i, shift)
		d_moves = [move for move in moves if ord(move[0].upper()) - 65 == i and move[2].upper() == "D"]
		d_moves.sort(key=lambda x: int(x[1]))
		moves = [item for item in moves if item not in d_moves]
		if len(d_moves) > 0:
			printDMoves(d_moves, len(cells), i, shift)
		else:
			print(f"{chr(i + 65)}{tab}" + f"{tab}" * shift + f"{2 * tab}".join(cells))
		dd_dl_for_row = [move for move in moves if
		                 ord(move[0].upper()) - 65 == i and (move[2].upper() == "DD" or move[2].upper() == "DL")]
		remaining_moves = [item for item in moves if item not in dd_dl_for_row]
		dd_dl_for_row.sort(key=lambda x: (x[1], 0 if x[2].upper() == "DL" else 1))
		triangles_for_row = [sublist for sublist in occupied_triangles if sublist[1] == i]
		moves = printDLAndDDMovesAndUpdateMoveList(dd_dl_for_row, i, shift, center, triangles_for_row)

		# sada printDLAndDDMovesAndUpdateMoveList vrati nove poteze za sledeci red i na njih se konkatenisu na remaining_moves...
		moves += remaining_moves


def makeBoard(size: int):
	if 4 <= size <= 8:
		board = []
		center = size * 2 - 1
		for i in range(size):
			board.append(["*"] * (size + i))

		for i in range(1, size):
			board.append(["*"] * (center - i))
		return board
	else:
		print('Losa velicina tabele! - postavi velicinu od 4 do 8!')
		return


def end_check(occupied_triangles, board_size):
	if len(occupied_triangles) == 6 * board_size ** 2:
		return True

	max_count = 3 * board_size ** 2

	count_x = 0
	count_o = 0

	for element in occupied_triangles:
		if element[0] == 'X':
			count_x += 1
		elif element[0] == 'O':
			count_o += 1

	if count_x > max_count or count_o > max_count:
		return True

	return False


def arbitrary_state(board_size):
	tabla = makeBoard(board_size)

	prepared_moves = [['a', 1, 'd', 3], ['a', 2, 'dl', 3], ['a', 2, 'dd', 3], ['b', 1, 'd', 3],
	                  ['a', 3, 'dl', 3], ['a', 3, 'dd', 3], ['c', 1, 'd', 3],
	                  ['d', 4, 'dd', 3], ['d', 4, 'dl', 3], ['e', 2, 'd', 3], ['b', 2, 'dl', 3],
	                  ['d', 1, 'dd', 3], ['d', 1, 'd', 3], ['d', 2, 'dd', 3], ['c', 3, 'dl', 3], ['e', 1, 'd', 3]]
	# Ovaj niz (matrica, trebalo bi da je set najbolje ali neka za pocetak) odnosi se na zauzete trouglove.
	# Uzima vrednost koju ce iscrta, vrstu i kolonu - tj. vrsta sa tacke "iscrtava" x i o ispod nje zato sto se x i o nalaze tacno ispod tacaka
	# a u fju za iscrtavanje veza poravnjavamo se po tacke iznad te vrste. Zato je ovako najlakse da se iscrtaju tacke
	# Za prvu fazu generisemo niz X i O staticki, a kasnije ce da generisemo ovaj set dinamicki kroz poteze.

	# Posto postoji ovakav niz poteza, ima i ovaj parametar TRUE ili FALSE na kraju.
	# Svaka tacka zaduzena za x ili o ispod nje, ali i pored nje, da bi se pokrili svi trouglovi.
	# Zato treba voditi racuna pri prosledjivanju ovih parametara, pogotovo kod redova ispod polovine.
	# Da se npr. ne iscrta x/o ispod prve tacke srednjeg reda. Kada se dinamicki generisu trouglici, u 2. fazi
	# bice implementirano da ne moze da se desi.

	# za razliku od poteza ovde se bas prenose indexi reda i kolone tacke ispod koje treba iscrtati x/o
	# odlucicemo se za 1 nacin u buducnosti...
	occupied_triangles = [['x', 0, 1, False], ['x', 0, 2, False], ['x', 1, 2, False], ['o', 3, 1, False],
	                      ['o', 3, 0, True], ['o', 3, 1, True], ['x', 4, 0, True]]  # <-
	printBoard(tabla, prepared_moves, occupied_triangles)
	print()


def initial_state(board_size):
	return makeBoard(board_size), [], [], [], defaultdict(list)  # board moves old_moves occupied_triangles links


def links_for_move(letter, number, direction, size):
	if direction == "D":
		lista = [(letter, number + i) for i in range(0, 4)]
		return [(lista[i], lista[i + 1]) for i in range(3)]

	elif direction == "DD":
		half_char = ord('A') + size
		lista = []
		broj = 1

		while ord(letter) + 1 < half_char:
			lista.append(((letter, number), (chr(ord(letter) + 1), number + 1)))
			broj += 1
			number += 1
			letter = chr(ord(letter) + 1)
			if broj == 4:
				return lista

		for i in range(4 - broj):
			lista.append(((letter, number), (chr(ord(letter) + 1), number)))
			letter = chr(ord(letter) + 1)

		return lista


	elif direction == "DL":
		half_char = ord('A') + size
		lista = []
		broj = 0

		while ord(letter) + 1 < half_char:
			lista.append(((letter, number), (chr(ord(letter) + 1), number)))
			broj += 1
			letter = chr(ord(letter) + 1)
			if broj == 3:
				return lista

		for i in range(3 - broj):
			lista.append(((letter, number - i), (chr(ord(letter) + 1), number - i - 1)))
			letter = chr(ord(letter) + 1)

		return lista


def end_game_screen(occupied_triangles):
	os.system('cls' if os.name == 'nt' else 'clear')
	count_x = 0
	count_o = 0

	for element in occupied_triangles:
		if element[0] == 'x':
			count_x += 1
		elif element[0] == 'o':
			count_o += 1

	if count_x > count_o:
		print(f"X IGRAC JE POBEDIO SA {count_x} BODOVA!!\n\nO igrac  je osvojio {count_o} bodova")
	if count_x < count_o:
		print(f"O IGRAC JE POBEDIO SA {count_o} BODOVA!!\n\nX igrac  je osvojio {count_x} bodova")
	if count_x == count_o:
		print(f"NERESENO OBA IGRACA IMAJU {count_x} BODOVA!")


def give_coordinates_and_direction():
	return input("Unesite podatke (format: red(A, B, ...) kolona(1, 2, ...) potez(DD,D,DL)): ")


def check_for_triangles(links_to_check, all_links, direction, occupied_triangles: list, board_size):
	for link in links_to_check:
		if direction == "D":
			triangles = check_triangles_for_d_link(link, all_links, board_size)
			if triangles:
				for el in triangles:
					print(el)
				occupied_triangles.extend(triangles)

		if direction == "DD":
			triangles = check_triangles_for_dd_link(link, all_links, board_size)
			if triangles:
				for el in triangles:
					print(el)
				occupied_triangles.extend(triangles)

		if direction == "DL":
			triangles = check_triangles_for_dl_link(link, all_links, board_size)
			if triangles:
				for el in triangles:
					print(el)
				occupied_triangles.extend(triangles)

# ((A,3),(B,4))
def check_triangles_for_dd_link(ddLink, all_links, board_size):
	to_return = []

	if ord(ddLink[0][0]) - ord("A") + board_size != ddLink[0][1]:
		char = ddLink[0][0]
		number = ddLink[0][1] + 1
		if (char, number) in all_links[ddLink[0]] and (char, number) in all_links[ddLink[1]]:
			to_return.append(['x', ord(ddLink[0][0]) - ord("A"), ddLink[0][1] - 1,
			                  True])  # TREBA -1 ZA TRECI PARAMETAR, ALI POSTO MORA SA TRUE FALSE NEMA GA

	if ord(ddLink[0][0]) - ord("A") < board_size - 1 or ddLink[0][1] != 1:
		char = ddLink[1][0]
		number = ddLink[1][1] - 1
		if (char, number) in all_links[ddLink[0]] and (char, number) in all_links[ddLink[1]]:
			to_return.append(['x', ord(ddLink[0][0]) - ord("A"), ddLink[0][1] - 1,
			                  False])  # TREBA -1 ZA TRECI PARAMETAR, ALI POSTO MORA SA TRUE FALSE NEMA GA
	return to_return

# ((A,3),(B,4))
def check_triangles_for_dl_link(dlLink, all_links, board_size):
	to_return = []

	if ord(dlLink[0][0]) - ord("A") >= board_size or dlLink[0][1] != 1:
		char = dlLink[0][0]
		number = dlLink[0][1] - 1
		if (char, number) in all_links[dlLink[0]] and (char, number) in all_links[dlLink[1]]:
			to_return.append(['x', ord(dlLink[0][0]) - ord("A"), dlLink[0][1] - 2,
			                  True])  # TREBA -1 ZA TRECI PARAMETAR, ALI POSTO MORA SA TRUE FALSE NEMA GA

	middle_char = chr(ord('A') + board_size - 1)

	if ord(dlLink[0][0]) - ord("A") < board_size - 1 or dlLink[0][1] != board_size * 2 - 1 - (
			ord(dlLink[0][0]) - ord(middle_char)):
		char = dlLink[1][0]
		number = dlLink[1][1] + 1
		if (char, number) in all_links[dlLink[0]] and (char, number) in all_links[dlLink[1]]:
			to_return.append(['x', ord(dlLink[0][0]) - ord("A"), dlLink[0][1] - 1,
			                  False])  # TREBA -1 ZA TRECI PARAMETAR, ALI POSTO MORA SA TRUE FALSE NEMA GA

	return to_return

# ((B,1),(B,2))
def check_triangles_for_d_link(dLink, all_links, board_size):
	to_return = []

	if dLink[0][0] != "A":
		char = chr(ord(dLink[0][0]) - 1)
		if ord(dLink[0][0]) - ord("A") < board_size:
			number = dLink[0][1]
			if (char, number) in all_links[dLink[0]] and (char, number) in all_links[dLink[1]]:
				to_return.append(["x", ord(char) - ord('A'), dLink[0][1] - 1, False])
		else:
			number = dLink[1][1]
			if (char, number) in all_links[dLink[0]] and (char, number) in all_links[dLink[1]]:
				to_return.append(["x", ord(char) - ord('A'), dLink[0][1], False])

	last_char = chr(ord("A") + board_size * 2 - 2)
	if dLink[0][0] != last_char:
		char = chr(ord(dLink[0][0]) + 1)
		if ord(dLink[0][0]) - ord("A") < board_size - 1:
			number = dLink[1][1]
			if (char, number) in all_links[dLink[0]] and (char, number) in all_links[dLink[1]]:
				to_return.append(["x", ord(char) - ord('A') - 1, dLink[0][1] - 1,
				                  True])
		else:
			number = dLink[0][1]
			if (char, number) in all_links[dLink[0]] and (char, number) in all_links[dLink[1]]:
				to_return.append(["x", ord(char) - ord('A') - 1, dLink[0][1] - 1,
				                  True])

	return to_return


def start_game():
	char_board_size = None
	# while True:
	# 	char_board_size = input("Unesite velicinu table (od 4 do 8):")
	# 	if (not char_board_size.isdigit()) or int(char_board_size) < 4 or int(char_board_size) > 8:
	# 		print("Dimenzija nije korektna!")
	# 	else:
	# 		break

	# while True:
	# 	user_input = input("Ko igra prvi (x ili o): ")
	# 	if user_input.upper() == "X" or user_input.upper() == "O":
	# 		# OVDE DOPUNITI
	# 		break
	# 	os.system('cls' if os.name == 'nt' else 'clear')
	#
	# os.system('cls' if os.name == 'nt' else 'clear')

	# board_size = int(char_board_size)
	board_size = int(4)

	tabla, moves, old_moves, occupied_triangles, links = initial_state(board_size)

	printBoard(tabla)

	# UKLJUCITE OVU LINIJU ZA PROIZVOLJNO STANJE
	# arbitrary_state(board_size)

	while True:
		# moves = copy.deepcopy(old_moves)
		# ovde je bilo jer niz nije bio prazan na pocetku... prebaceno dole

		user_input = give_coordinates_and_direction()

		parts = user_input.split()
		if len(parts) != 3:
			print("Nije dobar format!")
			continue

		move = [parts[0], parts[1], parts[2]]
		if validateMove(move, tabla, moves):
			to_draw = 3
			move[1] = int(move[1])
			move.append(to_draw)
			moves.append(move)

			lista = links_for_move(move[0].upper(), move[1], move[2].upper(), board_size)

			for link in lista:
				links[link[0]].append(link[1])
				links[link[1]].append(link[0])

			check_for_triangles(lista, links, move[2].upper(), occupied_triangles, board_size)

			# links.extend(links_for_move(move[0].upper(), move[1], move[2].upper(), board_size))

			old_moves = copy.deepcopy(moves)
			os.system('cls' if os.name == 'nt' else 'clear')
			printBoard(tabla, moves, occupied_triangles)

			moves = copy.deepcopy(old_moves)
			#for el in occupied_triangles:
			#	print(el)

			# OVO JE ZA TEST SAMO
			# print()
			# for el in links:
			#	print(el)
			# print()

			if end_check(occupied_triangles, board_size):
				print("Kraj igre!")
				end_game_screen(occupied_triangles)
				break


if __name__ == "__main__":
	while True:
		start_game()

		while True:
			user_input = input("Nova partija? [Yes/No]\n")
			if user_input.upper() == "YES":
				break
			if user_input.upper() == "NO":
				print("Hvala na igranju!")
				exit()
