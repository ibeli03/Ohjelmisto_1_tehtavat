import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
    host="localhost",
    user="isabel",
    password="k4kkeli123",
    database="flight_game"
)

cursor = connection.cursor()

def get_coordinates(icao_code):
    query = "SELECT latitude, longitude FROM airports WHERE ICAO = %s"
    cursor.execute(query, (icao_code,))
    result = cursor.fetchone()
    return result if result else None

icao1= input("Enter the ICAO code for the first airport: ")
icao2= input("Enter the ICAO code for the second airport: ")

coords1= get_coordinates(icao1)
coords2= get_coordinates(icao2)

if coords1 and coords1:
    distance = geodesic(coords1, coords2).kilometers
    print(f"The distance between {icao1} and {icao2} is {distance:2f} kilometers.")
else:
    print("One or both ICAO codes invalid.")

cursor.close()
connection.close()

