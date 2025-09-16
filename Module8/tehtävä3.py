import mysql.connector
from geopy.distance import geodesic

#Connect to MariaDB
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3307,
    database='flight_game',
    user='root',
    password='1234',
    autocommit=True
)

cursor = connection.cursor()

# ICAO code
def get_airport_coordinates(icao):
    cursor.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s", (icao,))
    result = cursor.fetchone()
    if result:
        return result[0],result[1]
    else:
        return None

icao1 = input("Enter the ICAO code of the first airport: ").upper()
icao2 = input("Enter the ICAO code of the second airport: ").upper()

coords1 = get_airport_coordinates(icao1)
coords2 = get_airport_coordinates(icao2)

if coords1 and coords2:
    distance = geodesic(coords1, coords2).kilometers
    print(f"The distance between {icao1} and {icao2} is {distance:.2f} km.")
else:
    print("One or both ICAO codes were not found in the database.")

# Clean
cursor.close()
connection.close()
