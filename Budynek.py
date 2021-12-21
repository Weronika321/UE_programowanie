class Budynek:
    def __init__(self, powierzchnia: float, cena: float, ulica: str) -> None:
        self._powierzchnia = powierzchnia
        self._cena = cena
        self._ulica = ulica

    @property
    def powierzchnia(self) -> float:
        return self._powierzchnia

    @property
    def cena(self) -> str:
        return self._cena

    @property
    def ulica(self) -> str:
        return self._ulica
