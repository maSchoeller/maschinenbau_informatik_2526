def ist_primzahl(n: int) -> bool:
	if n < 2:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	teiler = 3
	while teiler * teiler <= n:
		if n % teiler == 0:
			return False
		teiler += 2
	return True





def erste_primzahlen(anzahl: int) -> list[int]:
	primzahlen: list[int] = []
	kandidat = 2
	while len(primzahlen) < anzahl:
		if ist_primzahl(kandidat):
			primzahlen.append(kandidat)
		kandidat += 1
	return primzahlen


def main() -> None:
	primzahlen = erste_primzahlen(100)
	for p in primzahlen:
		print(p)


if __name__ == "__main__":
	main()
