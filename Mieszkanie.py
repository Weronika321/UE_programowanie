from Budynek import Budynek


class Mieszkanie(Budynek):
    def __init__(
        self, powierzchnia: float, cena: str, ulica: str, nr_pietra: int
    ) -> None:
        super().__init__(powierzchnia, cena, ulica)
        self._nr_pietra = nr_pietra

    @property
    def nr_pietra(self) -> float:
        return self._nr_pietra

    def __str__(self) -> str:
        return f"""Mieszkanie: \n\t
                powierzchnia: {self._powierzchnia},\n\t
                cena: {self._cena},\n\t
                ulica: {self._ulica},\n\t
                piętro: {self._nr_pietra}"""
