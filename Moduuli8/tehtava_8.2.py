import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="isabel",
    password="k4kkeli123",
    database="flight_game"
)

cursor = connection.cursor()

area_code = input("Enter area code (e.g F1): ")

query = """
SELECT airport_type, COUNT(*) as count FROM airports WHERE area_code = %s GROUP BY airport_type ORDER BY airport_type;"""

cursor.execute(query, (area_code,))
results = cursor.fetchall()

if results:
    print(f"Airports in area {area_code}: ")
    for row in results:
        print(f"{row[1]} {row[0]}(s)")
else:
    print("No airports found with that code.")
cursor.close()
connection.close()


