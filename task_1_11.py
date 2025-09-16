# BMI Rechner mit Benutzereingabe
gewicht = float(input("Bitte Gewicht in kg eingeben: "))
groesse = float(input("Bitte Körpergrösse in m eingeben: "))

bmi = round(gewicht / (groesse ** 2), 2)
print(f"Dein BMI beträgt: {bmi}")
