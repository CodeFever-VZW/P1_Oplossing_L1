# Vraag de gebruiker om een temperatuur in Celsius in te voeren en bereken de equivalente temperatuur in Fahrenheit.
# Print de resultaten uit.  Fahrenheit = Celsius × 1.8 + 32

celsius = float(input("Voer de temperatuur in Celsius in: "))
fahrenheit = (celsius * 9/5) + 32
print("De temperatuur in Fahrenheit is: " + str(fahrenheit) + "°F")