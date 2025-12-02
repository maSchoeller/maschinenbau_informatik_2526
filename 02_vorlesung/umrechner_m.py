
print("Willkommen beim M umrechner!")
# Eingabe vom Kilometerstand
kilometer_value = float(input("Gib deinen Kilometerwert ein: "))
message = f"Deine Eingabe waren: {kilometer_value} km"
print(message)
meter_value = kilometer_value * 1000
print(f"Die konvertierte Meterzahl ist: {meter_value}")