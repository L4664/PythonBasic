# Benutzereingaben für die Reise
distanz = float(input("Wie viele Kilometer möchtest du fahren? "))
geschwindigkeit = float(input("Wie schnell fährt dein Auto im Durchschnitt (km/h)? "))
verbrauch = float(input("Wie hoch ist der Verbrauch des Autos in Litern pro 100 km? "))

# Berechnung der Fahrtzeit in Minuten
fahrzeit_stunden = distanz / geschwindigkeit
fahrzeit_minuten = round(fahrzeit_stunden * 60, 2)

# Berechnung des Benzinverbrauchs
gesamtverbrauch = round(distanz * verbrauch / 100, 2)

# Ausgabe mit Formatierung
print(f"Die Fahrzeit beträgt {fahrzeit_minuten} Minuten.")
print(f"Der gesamte Benzinverbrauch beträgt {gesamtverbrauch} Liter.")
