def time_to_decimal_hours(hours, minutes, seconds):
    decimal_hours = hours + minutes / 60 + seconds / 3600
    return decimal_hours

# Beispiel:
stunden = 3
minuten = 2
sekunden = 10

result = time_to_decimal_hours(stunden, minuten, sekunden)
print(f"{stunden} Stunden / {minuten} Minuten / {sekunden} Sekunden => {result} Stunden")
