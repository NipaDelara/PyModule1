import mariadb

def main():
    global cursor, connection

    def get_connection():
        return mariadb.connect(
            host="127.0.0.1",
            user="root",
            password="12345",
            database="flight_game",
            port=3307
        )

    icao = input("Enter ICAO code: ").strip().upper()

    try:
        connection = get_connection()
        cursor = connection.cursor()

        sql = "SELECT name, municipality FROM airport WHERE ident = ?"
        cursor.execute(sql, (icao,))
        result = cursor.fetchone()

        if result:
            print(f"Airport: {result[0]}, located in {result[1]}")
        else:
            print("No airport found with that ICAO code.")

    except mariadb.Error as e:
        print(f"Database error: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

if __name__ == "__main__":
    main()
