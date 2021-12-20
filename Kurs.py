class Kurs:
    def __init__(
        self,
        lista_odcinkow: list,
        kierowca: str,
        auto: str,
        czas: str,
        odleglosc_km: list,
    ) -> None:
        self._lista_odcinkow = lista_odcinkow
        self._kierowca = kierowca
        self._auto = auto
        self._czas = czas
        self._odleglosc_km = odleglosc_km

    @property
    def lista_odcinkow(self) -> list:
        return self._lista_odcinkow

    @property
    def kierowca(self) -> str:
        return self._kierowca

    @property
    def auto(self) -> str:
        return self._auto

    @property
    def czas(self) -> str:
        return self._czas

    @property
    def odleglosc_km(self):
        return self._odleglosc_km

    @lista_odcinkow.setter
    def lista_odcinkow(self, lista: list) -> None:
        self._lista_odcinkow = lista

    @kierowca.setter
    def kierowca(self, nazwa_kierowcy: str) -> None:
        self._kierowca = nazwa_kierowcy

    @auto.setter
    def auto(self, nazwa_auta: str) -> None:
        self._auto = nazwa_auta

    @czas.setter
    def czas(self, nazwa_czas: str) -> None:
        self._czas = nazwa_czas

    def __str__(self) -> str:
        return f"""Lista właścicieli: {self._lista_odcinkow}.\n
                Kierowca: {self._kierowca}\n
                Auto: {self._auto}\n
                Lista odległości w km: {self._odleglosc_km}\n
                Czas: {self._czas}h
                """

    def suma_km(self) -> float:
        suma = 0
        for km in self._odleglosc_km:
            suma += km
        return round(suma, 2)

    def marka(self) -> str:
        return self._auto
