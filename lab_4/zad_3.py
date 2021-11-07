class Property:
    def __init__(self,
                 area: float,
                 rooms: int,
                 price: int,
                 adress: str) -> None:
        self._area = area
        self._rooms = rooms
        self._price = price
        self._adress = adress

    @property
    def area(self):
        return self._area

    @property
    def rooms(self):
        return self._rooms

    @property
    def price(self):
        return self._price

    @property
    def adress(self):
        return self._adress


class House(Property):
    def __init__(self,
                 area: float,
                 rooms: int,
                 price: int,
                 adress: str,
                 plot: int) -> None:
        self._area = area
        self._rooms = rooms
        self._price = price
        self._adress = adress
        self._plot = plot

    @property
    def area(self):
        return self._area

    @property
    def rooms(self):
        return self._rooms

    @property
    def price(self):
        return self._price

    @property
    def adress(self):
        return self._adress

    @property
    def plot(self):
        return self._plot

    def __str__(self) -> str:
        return f"""Dom:\n\t
                Powierzchnia domu: {self.area}m^2\n\t
                Liczba pokoi: {self.rooms}\n\t
                Cena: {self.price}zł\n\t
                Adres: {self.adress}\n\t
                Rozmiar działki: {self.plot}m^2"""


class Flat(Property):
    def __init__(self,
                 area: float,
                 rooms: int,
                 price: int,
                 adress: str,
                 floor: int) -> None:
        self._area = area
        self._rooms = rooms
        self._price = price
        self._adress = adress
        self._floor = floor

    @property
    def area(self):
        return self._area

    @property
    def rooms(self):
        return self._rooms

    @property
    def price(self):
        return self._price

    @property
    def adress(self):
        return self._adress

    @property
    def floor(self):
        return self._floor

    def __str__(self) -> str:
        return f"""Mieszkanie:\n\t
                Powierzchnia mieszkania: {self.area}m^2\n\t
                Liczba pokoi: {self.rooms}\n\t
                Cena: {self.price}zł\n\t
                Adres: {self.adress}\n\t
                Numer piętra: {self.floor}"""


house1 = House(200, 5, 1_000_000, "Zielona 34, 32-122 Katowice", 300)
flat1 = Flat(50, 2, 200_000, "Miejska 281/7, 90-432 Gliwice", 3)

print(house1)
print(flat1)
