zahl1 = 30  # feste erste Zahl

zahl2 = input("Gib die zweite Zahl ein: ")

# hier wird zahl1 durch zahl2 geteilt
try:
    zahl2_f = float(zahl2)
except ValueError:
    print("Fehler: Die eingegebene zweite Zahl ist keine gültige Zahl.")
    raise SystemExit(1)

if zahl2_f == 0:
    print("Fehler: Division durch Null ist nicht erlaubt.")
else:
    resultat = float(zahl1) / zahl2_f  # eigentliche Division
    print("Das Ergebnis der Division von", zahl1, "durch", zahl2_f, "ist:", resultat)
