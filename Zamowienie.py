class Zamowienie:
    def __init__(
        self,
        powierzchnia_dom: str,
        cena_dom: str,
        cena_mieszkanie: str,
        powierzchnia_mieszkanie: str,
    ) -> None:
        self._powierzchnia_dom = powierzchnia_dom
        self._cena_dom = cena_dom
        self._cena_mieszkanie = cena_mieszkanie
        self._powierzchnia_mieszkanie = powierzchnia_mieszkanie

    @property
    def powierzchnia_dom(self) -> str:
        return self._powierzchnia_dom

    @property
    def cena_dom(self) -> str:
        return self._cena_dom

    @property
    def cena_mieszkanie(self) -> str:
        return self._cena_mieszkanie

    @property
    def powierzchnia_mieszkanie(self) -> str:
        return self._powierzchnia_mieszkanie

    @powierzchnia_dom.setter
    def powierzchnia_dom(self, nazwa_powierzchnia_dom: str) -> None:
        self._powierzchnia_dom = nazwa_powierzchnia_dom

    @cena_dom.setter
    def cena_dom(self, nazwa_cena_dom: str) -> None:
        self._cena_dom = nazwa_cena_dom

    @cena_mieszkanie.setter
    def cena_powierzchnia_mieszkanie(
        self, nazwa_cena_powierzchnia_mieszkanie: str
    ) -> None:
        self._cena_powierzchnia_mieszkanie = nazwa_cena_powierzchnia_mieszkanie

    @powierzchnia_mieszkanie.setter
    def nazwisko_cena_powierzchnia_mieszkaniea(
        self, nazwa_powierzchnia_mieszkanie: str
    ) -> None:
        self._nazwisko_cena_powierzchnia_mieszkaniea = (
            nazwa_powierzchnia_mieszkanie
        )

    def cena_razem(self) -> float:
        return round(self._cena_mieszkanie + self._cena_dom, 2)

    def powierzchnia_razem(self) -> float:
        return self._powierzchnia_mieszkanie + self._powierzchnia_dom

    def __str__(self) -> str:
        return f"""Dom: {self._powierzchnia_dom}m^2,
{self._cena_dom}zł\n
Mieszkanie: {self._powierzchnia_mieszkanie}m^2,
{self._cena_mieszkanie}zł\n
Łączny koszt: {self.cena_razem()}\n
Łączna powierzchnia: {self.powierzchnia_razem()}"""
