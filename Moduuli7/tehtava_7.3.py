airports = {"EFHK": "Helsinki-Vantaa", "SHST":"Santiago de Chile", "LEST": "Santiago de Compostela", "LICR":"Reggio Calabria", "LICJ":"Falcone-Borsellino, Palermo"}
airports_info = input("Do you want to 'enter a new airport', 'fetch the information of an existing one' or press enter to quit? ")
if airports_info == "fetch the information of an existing one":
    airport_info = input("Enter existing airport ICAO code: ")
    if airport_info in airports:
        print(f"{airports[airport_info]}")

if airports_info == "enter a new airport":
    airport_info = input("Enter new airport ICAO code and name of the airport: ")


