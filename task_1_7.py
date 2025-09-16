# Zwei Zahlen vergleichen
zahl1 = float(input("Gib die erste Zahl ein: "))
zahl2 = float(input("Gib die zweite Zahl ein: "))

if zahl1 > zahl2:
    print(f"{zahl1} ist grösser als {zahl2}")
elif zahl1 == zahl2:
    print(f"{zahl1} und {zahl2} sind gleich")
else:
    print(f"{zahl2} ist grösser als {zahl1}")