class Developer:
    def __init__(
        self,
        nazwa: str,
        imie_wlasciciel: str,
        nazwisko_wlasciciel: str,
        adres: str,
    ) -> None:
        self._nazwa = nazwa
        self._imie_wlasciciel = imie_wlasciciel
        self._nazwisko_wlasciciel = nazwisko_wlasciciel
        self._adres = adres

    @property
    def nazwa(self) -> str:
        return self._nazwa

    @property
    def imie_wlasciciel(self) -> str:
        return self._imie_wlasciciel

    @property
    def nazwisko_wlasciciel(self) -> str:
        return self._nazwisko_wlasciciel

    @property
    def adres(self) -> str:
        return self._adres

    def __str__(self) -> str:
        return f"""Developer: {self._nazwa}\n\t
                imie: {self._imie_wlasciciel}\n\t
                nazwisko: {self._nazwisko_wlasciciel},\n\t
                adres: {self._adres}"""
