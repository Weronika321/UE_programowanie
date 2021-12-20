class Odcinek:
    def __init__(
        self,
        start: str,
        meta: str,
        odleglosc_km: float,
        czas_h: float,
        kierowca: str,
    ) -> None:
        self._start = start
        self._meta = meta
        self._odleglosc_km = odleglosc_km
        self._czas_h = czas_h
        self._kierowca = kierowca

    @property
    def start(self) -> str:
        return self._start

    @property
    def meta(self) -> str:
        return self._meta

    @property
    def odleglosc_km(self) -> float:
        return self._odleglosc_km

    @property
    def czas_h(self) -> float:
        return self._czas_h

    @property
    def kierowca(self) -> str:
        return self._kierowca

    def __str__(self) -> str:
        return f"""Odcinek od {self._start} do {self._meta}. \n
                Odległość {self._odleglosc_km}km przebyta w czasie
                {self._czas_h}h przez {self._kierowca}"""
