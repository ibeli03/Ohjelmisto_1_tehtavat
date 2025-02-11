import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "isabelal",
    password = "K4kkel!123",
    database = "flight_game"
)

icao_code = input("Enter the airport ICAO code: ")

cursor = connection.cursor()

query = """SELECT name, municipality FROM airport WHERE ident = %s;"""
cursor.execute(query, (icao_code,))
result = cursor.fetchone()

if result:
    airport_name, town = result
    print(f"The airport name is {airport_name}")
    print(f"The town is {town}")
else:
    print("No airport found.")
cursor.close()
connection.close()

