import requests

kaupunki = input("Anna paikkakunnan nimi: ")
api_avain = "526d53948512ca7578cfdbc740ed2443"

url = f"http://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={api_avain}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    saakuvaus = data["weather"][0]["description"]
    lampotila_celsius = data["main"]["temp"]

    print(f"Sää: {saakuvaus.capitalize()}")
    print(f"Lämpötila: {lampotila_celsius:.1f} °C")
else:
    print(f"Virhe ({data.get('cod')}): {data.get('message')}")
