class Pojazd:
    def __init__(
        self,
        liczba_kol: int,
        marka: str,
        rodzaj: str,
        wlasciciel: str,
        liczba_miejsc: int,
    ) -> None:
        self._liczba_kol = liczba_kol
        self._marka = marka
        self._rodzaj = rodzaj
        self._wlasciciel = wlasciciel
        self._liczba_miejsc = liczba_miejsc

    @property
    def liczba_kol(self) -> int:
        return self._liczba_kol

    @property
    def marka(self) -> str:
        return self._marka

    @property
    def rodzaj(self) -> str:
        return self._rodzaj

    @property
    def wlasciciel(self) -> str:
        return self._wlasciciel

    @property
    def liczba_miejsc(self) -> int:
        return self._liczba_miejsc

    def __str__(self) -> str:
        return f"""Auto:\n\t
                Liczba kół: {self._liczba_kol}\n\t
                Marka: {self._marka}\n\t
                Rodzaj: {self._rodzaj}\n\t
                Właściciel: {self._wlasciciel}\n\t
                Liczba miejsc siedziących: {self._liczba_miejsc}
                """
