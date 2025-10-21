import mariadb

def get_connection():
    return mariadb.connect(
        host="127.0.0.1",
        user="root",
        password="12345",
        database="flight_game",
        port=3307
    )

def main():
    global connection, cursor
    country_code = input("Enter country code (e.g. FI, EE, US): ").strip().upper()

    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Query airports by country
        sql = "SELECT name, ident FROM airport WHERE iso_country = ?"
        cursor.execute(sql, (country_code,))
        results = cursor.fetchall()

        if results:
            print(f"\nAirports in {country_code}:")
            for row in results:
                # row[0] = name, row[1] = ident
                print(f"{row[1]} - {row[0]}")
        else:
            print("No airports found for that area code.")

    except mariadb.Error as e:
        print(f"Database error: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

if __name__ == "__main__":
    main()
