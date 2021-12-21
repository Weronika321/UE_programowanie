from Budynek import Budynek


class Dom(Budynek):
    def __init__(
        self,
        powierzchnia: float,
        cena: float,
        ulica: str,
        powierzchnia_działki: float,
    ) -> None:
        super().__init__(powierzchnia, cena, ulica)
        self._powierzchnia_działki = powierzchnia_działki

    @property
    def powierzchnia_działki(self) -> float:
        return self._powierzchnia_działki

    def __str__(self) -> str:
        return f"""Dom: \n\t
                powierzchnia: {self._powierzchnia},\n\t
                cena: {self._cena},\n\t
                ulica: {self._ulica},\n\t
                powierzchnia działki: {self._powierzchnia_działki}"""
