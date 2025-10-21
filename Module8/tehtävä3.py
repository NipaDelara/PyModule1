import mariadb
from geopy.distance import geodesic

def get_connection():
    return mariadb.connect(
        host="127.0.0.1",
        user="root",
        password="12345",
        database="flight_game",
        port=3307
    )

def get_airport_coordinates(cursor, icao):
    cursor.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = ?", (icao,))
    result = cursor.fetchone()
    if result:
        return result[0], result[1]
    else:
        return None

def main():
    global cursor, connection
    icao1 = input("Enter the ICAO code of the first airport: ").upper()
    icao2 = input("Enter the ICAO code of the second airport: ").upper()

    try:
        connection = get_connection()
        cursor = connection.cursor()

        coords1 = get_airport_coordinates(cursor, icao1)
        coords2 = get_airport_coordinates(cursor, icao2)

        if coords1 and coords2:
            distance = geodesic(coords1, coords2).kilometers
            print(f"The distance between {icao1} and {icao2} is {distance:.2f} km.")
        else:
            print("One or both ICAO codes were not found in the database.")

    except mariadb.Error as e:
        print(f"Database error: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

if __name__ == "__main__":
    main()
