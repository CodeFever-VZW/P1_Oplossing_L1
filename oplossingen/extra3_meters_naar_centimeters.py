# Schrijf een programma dat de gebruiker vraagt om een afstand in meters in te voeren om ze vervolgens om te zetten naar centimeters.
# Het programma moet de omgezette afstand in centimeters afdrukken.

afstand_in_meters = input("Voer een afstand in meters in: ")
omgezette_afstand = float(afstand_in_meters) * 100
print("Het equivalent in centimeters is:", omgezette_afstand)