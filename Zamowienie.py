class Zamowienie:
    def __init__(
        self,
        developer: str,
        nr_zamowienia: int,
        nr_developera: int,
        lista_budynkow: list,
    ) -> None:
        self._developer = developer
        self._nr_zamowienia = nr_zamowienia
        self._nr_developera = nr_developera
        self._lista_budynkow = lista_budynkow

    @property
    def developer(self) -> str:
        return self._developer

    @property
    def nr_zamowienia(self) -> int:
        return self._nr_zamowienia

    @property
    def nr_developera(self) -> int:
        return self._nr_developera

    @property
    def lista_budynkow(self) -> list:
        return self._lista_budynkow

    @developer.setter
    def developer(self, nazwa_developer: str) -> None:
        self._developer = nazwa_developer

    @nr_zamowienia.setter
    def nr_zamowienia(self, numer: int) -> None:
        self._nr_zamowienia = numer

    @nr_developera.setter
    def nr_developera(self, numer: int) -> None:
        self._nr_developera = numer

    @lista_budynkow.setter
    def lista_budynkow(self, lista: list) -> None:
        self._lista_budynkow = lista

    def cena_razem(self) -> float:
        suma = 0
        for budynek in self._lista_budynkow:
            suma += budynek._cena
        return round(suma, 2)

    def powierzchnia_razem(self) -> float:
        powierzchnia = 0
        for budynek in self._lista_budynkow:
            powierzchnia += budynek._powierzchnia
        return powierzchnia

    def __str__(self) -> str:
        return f"""Numer zamowienia: {self._nr_zamowienia}
Numer developera: {self._nr_developera}
Developer: {self._developer}
Łączny koszt: {self.cena_razem()}
Łączna powierzchnia: {self.powierzchnia_razem()}"""
