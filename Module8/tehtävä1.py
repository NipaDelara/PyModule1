import mysql.connector

def main():

    connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3307,
         database='flight_game',
         user='root',
         password='1234',
         autocommit=True
         )
    cursor = connection.cursor()

    icao = input("Enter ICAO code: ").strip().upper()

    #db query
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    if result:
        print(f"Airport: {result[0]}, located in {result[1]}")
    else:
        print("No airport found with that ICAO code.")

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()