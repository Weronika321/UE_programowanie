class Developer:
    def __init__(
        self,
        nazwa: str,
        imie: str,
        nazwisko: str,
        adres: str,
    ) -> None:
        self._nazwa = nazwa
        self._imie = imie
        self._nazwisko = nazwisko
        self._adres = adres

    @property
    def nazwa(self) -> str:
        return self._nazwa

    @property
    def imie(self) -> str:
        return self._imie

    @property
    def nazwisko(self) -> str:
        return self._nazwisko

    @property
    def adres(self) -> str:
        return self._adres

    def __str__(self) -> str:
        return f"""{self._nazwa}\n\t
                imie: {self._imie}\n\t
                nazwisko: {self._nazwisko},\n\t
                adres: {self._adres}"""
