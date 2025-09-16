# Passwort-Programm: Ist das Passwort lang genug?
pw = input("Bitte Passwort eingeben: ")
if len(pw) > 8:
    print(f"Das Passwort ist lang genug ({len(pw)} Zeichen).")
else:
    print(f"Das Passwort ist zu kurz ({len(pw)} Zeichen).")