import mysql.connector

def airports_by_country():
    connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3307,
         database='flight_game',
         user='root',
         password='1234',
         autocommit=True
    )
    cursor = connection.cursor()

    # Ask for area code (e.g., FI)
    country_code = input("Enter country area code (e.g., FI): ").strip().upper()

    # Query: count airports by type for given country
    sql = """
        SELECT type, COUNT(*) 
        FROM airport 
        WHERE iso_country = %s
        GROUP BY type
        ORDER BY type;
    """
    cursor.execute(sql, (country_code,))
    results = cursor.fetchall()

    if results:
        print(f"\nAirports in {country_code}:")
        for row in results:
            print(f"{row[1]} {row[0]} airports")
    else:
        print("No airports found for that area code.")

    cursor.close()
    connection.close()

if __name__ == "__main__":
    airports_by_country()

