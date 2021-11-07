import requests
import argparse  # przekazywanie parametrów (argumentów) wiersza poleceń

response = requests.get("https://api.openbrewerydb.org/breweries")


class Brawery:
    def __init__(self, id: int, name: str, brewery_type: str,
                 street: str, address_2: str, address_3: str,
                 city: str, state: str, county_province: str,
                 postal_code: str, country: str, longitude: str,
                 latitude: str, phone: str,  website_url: str,
                 updated_at: str, created_at: str) -> None:
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state = state
        self.county_province = county_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.updated_at = updated_at
        self.created_at = created_at

    def __str__(self) -> str:
        return f"""Dane obiektu:\n\t
                id: {self.id}\n\t
                Nazwa: {self.name}\n\t
                Typ: {self.brewery_type}\n\t
                Ulica: {self.street}\n\t
                Drugi adres: {self.address_2}\n\t
                Trzeci adres: {self.address_3}\n\t
                Miasto: {self.city}\n\t
                Stan: {self.state}\n\t
                Prowincja kraju: {self.county_province}\n\t
                Kod pocztowy: {self.postal_code}\n\t
                Kraj: {self.country}\n\t
                Długość geograficzna: {self.longitude}\n\t
                Szerokość geograficzna: {self.latitude}\n\t
                Numer telefonu: {self.phone}\n\t
                Adres strony internetowej: {self.website_url}\n\t
                Ostatnia aktualizacja: {self.updated_at}\n\t
                Utworzony: {self.created_at}"""


"""
Inicjujemy parser
(to on odpowiada za poprawne “wychwycenie”
podawanych argumentów i odczytanie ich wartości)
"""
parser = argparse.ArgumentParser()

# ? Definiujemy możliwe do użycia argumenty.
# ? required = False <- ozn. argument opcjonalny
parser.add_argument('--city',
                    help="Miasto, z którego mają być pobrane dane",
                    required=False)

# ? Parsujemy argumenty, aby “wyłuskać” przekazane w nich wartości
args = parser.parse_args()

for i in range(0, len(response.json())):
    if args.city is None:
        lista = list(response.json()[i].values())
    else:
        if response.json()[i]["city"] == "Knox":
            lista = response.json()[i].values()

    id, name, brewery_type, street = lista[:4]
    address_2, address_3, city, state = lista[4:8]
    county_province, postal_code, country, longitude = lista[8:12]
    latitude, phone, website_url, updated_at, created_at = lista[12:]

    obiekt = Brawery(id, name, brewery_type, street,
                     address_2, address_3, city, state,
                     county_province, postal_code, country,
                     longitude, latitude, phone, website_url,
                     updated_at, created_at)

    print(f"{i+1}. {obiekt}\n")

    if len(lista) == 20:
        break
