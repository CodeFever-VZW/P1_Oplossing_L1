# Schrijf een Python-programma dat aan de gebruiker twee vragen stelt:
# 1. Hoeveel mensen gaan er naar het concert?
# 2. Wat is de prijs per ticket?
#
# Bereken het totaalbedrag en print dat bedrag.
#
# Tip: Het aantal mensen is een geheel getal en de prijs is een kommagetal. Welke types zijn dat?
#
# Voorbeeldinvoer:
# Hoeveel mensen gaan er naar het concert?  3
# Wat is de prijs per ticket?  10.55
#
# Voorbeelduitvoer:
# De totale prijs bedraagt 31.65 euro.

aantal_mensen = int(input("Hoeveel mensen gaan er naar het concert?  "))
prijs_per_ticket = float(input("Wat is de prijs per ticket? "))

totaalbedrag = aantal_mensen * prijs_per_ticket

print("De totale prijs bedraagt", totaalbedrag, "euro.")