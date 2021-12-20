from Firma import Firma


class FirmaSpozywcza(Firma):
    def __init__(
        self,
        wlasciciel_firmy: str,
        powierzchnia_firmy: float,
        miejscowosc_firmy: str,
        ulica_firmy: str,
        kod_pocztowy_firmy: str,
    ) -> None:
        super().__init__(
            wlasciciel_firmy,
            powierzchnia_firmy,
            miejscowosc_firmy,
            ulica_firmy,
            kod_pocztowy_firmy,
        )

    def __str__(self) -> str:
        return f"""Firma transportowa:\n\t
                    właściciel firmy: {self._wlasciciel_firmy}\n\t
                    powierzchnia firmy: {self._powierzchnia_firmy}\n\t
                    Adres firmy: {self._ulica_firmy}
                    \t\t{self._kod_pocztowy_firmy} {self._miejscowosc_firmy}
                """
