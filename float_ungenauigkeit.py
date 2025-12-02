"""
Demonstration der Ungenauigkeit von Fließkommazahlen (Floats)
============================================================

Floats werden im Computer im binären System (IEEE 754 Standard) gespeichert.
Viele Dezimalzahlen können nicht exakt als Binärzahlen dargestellt werden,
ähnlich wie 1/3 im Dezimalsystem zu 0.333... wird.
"""

print("=" * 60)
print("Beispiel 1: Einfache Addition")
print("=" * 60)

# Was wir erwarten: 0.1 + 0.2 = 0.3
resultat = 0.1 + 0.2
print(f"0.1 + 0.2 = {resultat}")
print(f"Erwartet: 0.3")
print(f"Sind sie gleich? {resultat == 0.3}")  # False!
print(f"Genauer Wert: {resultat:.20f}")
print()

print("=" * 60)
print("Beispiel 2: Wiederholte Operationen")
print("=" * 60)

# Kleine Fehler akkumulieren sich
summe = 0.0
for i in range(10):
    summe += 0.1

print(f"0.1 addiert 10 mal: {summe}")
print(f"Erwartet: 1.0")
print(f"Sind sie gleich? {summe == 1.0}")  # False!
print(f"Genauer Wert: {summe:.20f}")
print(f"Differenz: {1.0 - summe}")
print()

print("=" * 60)
print("Beispiel 3: Subtraktion ähnlicher Zahlen")
print("=" * 60)

a = 1.0000000000000001
b = 1.0
differenz = a - b
print(f"{a} - {b} = {differenz}")
print(f"Genauer Wert: {differenz:.20f}")
print()

print("=" * 60)
print("Warum passiert das?")
print("=" * 60)
print("""
Floats werden binär gespeichert (Basis 2), aber wir denken dezimal (Basis 10).

Beispiel 0.1 in binär:
- Im Dezimalsystem: 0.1
- Im Binärsystem: 0.0001100110011001100... (unendlich periodisch!)
- Der Computer kann nur endlich viele Bits speichern
- Daher wird gerundet → kleiner Fehler entsteht
""")
print()

print("=" * 60)
print("Lösung 1: Vergleich mit Toleranz (epsilon)")
print("=" * 60)

a = 0.1 + 0.2
b = 0.3
epsilon = 1e-10  # Toleranzwert

if abs(a - b) < epsilon:
    print(f"{a} und {b} sind praktisch gleich (Differenz < {epsilon})")
else:
    print(f"{a} und {b} sind unterschiedlich")
print()

print("=" * 60)
print("Lösung 2: Decimal-Modul für exakte Dezimalzahlen")
print("=" * 60)

from decimal import Decimal

# Mit Decimal
d1 = Decimal('0.1')
d2 = Decimal('0.2')
d_resultat = d1 + d2
print(f"Mit Decimal: {d1} + {d2} = {d_resultat}")
print(f"Ist gleich 0.3? {d_resultat == Decimal('0.3')}")  # True!
print()

print("=" * 60)
print("Lösung 3: Arbeiten mit Ganzzahlen (Cents statt Euro)")
print("=" * 60)

# Statt 0.10€ + 0.20€ verwenden wir 10 Cent + 20 Cent
cents1 = 10
cents2 = 20
summe_cents = cents1 + cents2
euro = summe_cents / 100
print(f"{cents1} Cent + {cents2} Cent = {summe_cents} Cent = {euro}€")
print()

print("=" * 60)
print("Fazit")
print("=" * 60)
print("""
- Verwende NIEMALS == für Float-Vergleiche
- Nutze abs(a - b) < epsilon für Vergleiche
- Für Geld: decimal.Decimal oder Ganzzahlen (Cents)
- Für wissenschaftliche Berechnungen: numpy mit entsprechender Präzision
- Float-Fehler sind normal und in allen Programmiersprachen vorhanden!
""")
