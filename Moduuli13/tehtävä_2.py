import mariadb
from flask import Flask, jsonify

app = Flask(__name__)

#MariaDB connection
def create_connection():
    return mariadb.connect(
        host="127.0.0.1",
        user="root",
        password="12345",
        database="flight_game",
        port=3307
    )

# airport by ICAO code
@app.get("/kentta/<icao>")
def kentta(icao):
    try:
        conn = create_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("""
            SELECT ident, name, municipality, iso_country, latitude_deg, longitude_deg, type
            FROM airport
            WHERE ident = %s
        """, (icao,))
        row = cur.fetchone()
        conn.close()

        if row:
            return jsonify(row)
        else:
            return jsonify({"error": f"Lentokenttää koodilla {icao} ei löytynyt"}), 404

    except mariadb.Error as e:
        return jsonify({"error": str(e)}), 500


#all airports in a specific country
@app.get("/maa/<country>")
def maa(country):
    try:
        conn = create_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("""
            SELECT ident, name, municipality, iso_country, latitude_deg, longitude_deg, type
            FROM airport
            WHERE iso_country = %s
        """, (country.upper(),))
        rows = cur.fetchall()
        conn.close()

        if rows:
            return jsonify(rows)
        else:
            return jsonify({"error": f"Ei lentokenttiä löytynyt maasta {country}"}), 404

    except mariadb.Error as e:
        return jsonify({"error": str(e)}), 500

#Run flask app
app.run(host="127.0.0.1", port=3000, debug=True)