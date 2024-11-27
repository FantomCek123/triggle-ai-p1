def izvrsi_potez(bord_size):
	while True:
		try:
			# Unos koordinata
			coordinates = input("Unesite koordinate: ").strip()
			if len(coordinates) < 2:
				print("Unos nije validan. Pokušajte ponovo.")
				continue

			y = coordinates[0].strip().upper()  # Prvo slovo
			y_cord = ord(y) - ord('A')

			x = coordinates[1:].strip()  # Ostatak kao broj

			x_cord = int(x) - 1  # Pretvaramo u broj nakon validacije

			# Unos poteza
			move = input("Unesite potez (D, DL, DD): ").strip().upper()

			# Provera validnosti poteza
			if move not in ["D", "DL", "DD"]:
				print("Nevalidan potez. Dozvoljeni potezi su: D, DL, DD.")
				continue

			# Ako su oba unosa validna, vraćamo rezultat
			if proveri_potez(x_cord, y_cord, move, bord_size):
				return (x_cord, y_cord), move

			print("Nevalidan potez, probaj ponovo!\n")
		except ValueError:
			print("Greška u unosu. Pokušajte ponovo.")


def proveri_potez(X_kordinata, Y_kordinata, move, bord_size):
	if not (0 <= X_kordinata <= bord_size * 2 - 2 and 0 <= Y_kordinata <= bord_size * 2 - 2):
		return False
	if move == "D":
		if not ((Y_kordinata < bord_size and X_kordinata <= bord_size - 4 + Y_kordinata) or (Y_kordinata >= bord_size and X_kordinata <= bord_size + 2 - Y_kordinata)):
			return False

	if move == "DD" and not (X_kordinata < bord_size and Y_kordinata < bord_size):
		return False

	if move == "DL" and not (Y_kordinata < bord_size and Y_kordinata <= X_kordinata < bord_size + Y_kordinata):
		return False

	return True


# Testiramo funkciju
while True:
	coordinates, move = izvrsi_potez(4)
	print(f"Uneli ste koordinate: {coordinates} i potez: {move}")
