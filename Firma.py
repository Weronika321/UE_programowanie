class Firma:
    def __init__(
        self,
        wlasciciel_firmy: str,
        powierzchnia_firmy: float,
        miejscowosc_firmy: str,
        ulica_firmy: str,
        kod_pocztowy_firmy: str,
    ) -> None:
        self._wlasciciel_firmy = wlasciciel_firmy
        self._powierzchnia_firmy = powierzchnia_firmy
        self._miejscowosc_firmy = miejscowosc_firmy
        self._ulica_firmy = ulica_firmy
        self._kod_pocztowy_firmy = kod_pocztowy_firmy

    @property
    def wlasciciel_firmy(self) -> str:
        return self._wlasciciel_firmy

    @property
    def powierzchnia_firmy(self) -> float:
        return self._powierzchnia_firmy

    @property
    def miejscowosc_firmy(self) -> str:
        return self._miejscowosc_firmy

    @property
    def ulica_firmy(self) -> str:
        return self._ulica_firmy

    @property
    def kod_pocztowy_firmy(self) -> str:
        return self._kod_pocztowy_firmy
