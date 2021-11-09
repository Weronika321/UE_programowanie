class Kurs():
    def __init__(self, lista_odcinkow: list, kierowca: str, auto: str, czas: str, odleglosc_km: list) -> None:
        self._lista_odcinkow = lista_odcinkow
        self._kierowca = kierowca
        self._auto = auto
        self._czas = czas
        self._odleglosc_km = odleglosc_km
        
    @property
    def lista_odcinkow(self):
        return self._lista_odcinkow
    
    @property
    def kierowca(self):
        return self._kierowca
    
    @property
    def auto(self):
        return self._auto
    
    @property
    def czas(self):
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
        return f"""Lista odcinków: {self._lista_odcinkow}.\n
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


class Pojazd():
    def __init__(self, liczba_kol: int, marka: str, rodzaj: str, wlasciciel: str, liczba_miejsc: int) -> None:
        self._liczba_kol = liczba_kol
        self._marka = marka
        self._rodzaj = rodzaj
        self._wlasciciel = wlasciciel
        self._liczba_miejsc = liczba_miejsc
        
    @property
    def liczba_kol(self):
        return self._liczba_kol
    
    @property
    def marka(self):
        return self._marka

    @property
    def rodzaj(self):
        return self._rodzaj
    
    @property
    def wlasciciel(self):
        return self._wlasciciel
    
    @property
    def liczba_miejsc(self):
        return self._liczba_miejsc
    
    
    def __str__(self) -> str:
        return f"""Auto:\n\t
                Liczba kół: {self._liczba_kol}\n\t
                Marka: {self._marka}\n\t
                Rodzaj: {self._rodzaj}\n\t
                Właściciel: {self._wlasciciel}\n\t
                Liczba miejsc siedziących: {self._liczba_miejsc}
                """

class FirmaTransportowa():
    def __init__(self, wlasciciel_firmy: str, powierzchnia_firmy: float, miejscowosc_firmy: str, ulica_firmy: str, kod_pocztowy_firmy: str) -> None:
        self._wlasciciel_firmy = wlasciciel_firmy
        self._powierzchnia_firmy = powierzchnia_firmy
        self._miejscowosc_firmy = miejscowosc_firmy
        self._ulica_firmy = ulica_firmy
        self._kod_pocztowy_firmy = kod_pocztowy_firmy
            
    @property
    def wlasciciel_firmy(self):
        return self._wlasciciel_firmy
    
    @property
    def powierzchnia_firmy(self):
        return self._powierzchnia_firmy
    
    @property
    def miejscowosc_firmy(self):
        return self._miejscowosc_firmy
    
    @property
    def ulica_firmy(self):
        return self._ulica_firmy
    
    @property
    def kod_pocztowy_firmy(self):
        return self._kod_pocztowy_firmy
    
    def __str__(self) -> str:
        return f"""Firma transportowa:\n\t
                    właściciel firmy: {self._wlasciciel_firmy}\n\t
                    powierzchnia firmy: {self._powierzchnia_firmy}\n\t
                    Adres firmy: ul. {self._ulica_firmy}, {self._kod_pocztowy_firmy} {self._miejscowosc_firmy}   
                """
    

class Odcinek():
    def __init__(self, start: str, meta: str, odleglosc_km: float, czas_h: float, kierowca: str) -> None:
        self._start = start
        self._meta = meta
        self._odleglosc_km = odleglosc_km
        self._czas_h = czas_h
        self._kierowca = kierowca
        
    @property
    def start(self):
        return self._start
    
    @property
    def meta(self):
        return self._meta
    
    @property
    def odleglosc_km(self):
        return self._odleglosc_km
    
    @property
    def czas_h(self):
        return self._czas_h
    
    @property
    def kierowca(self):
        return self._kierowca
    
    def __str__(self) -> str:
        return f"""Odcinek od {self._start} do {self._meta}. \n
                Odległość {self._odleglosc_km}km przebyta w czasie {self._czas_h}h przez {self._kierowca}"""
        

class FirmaSpozywcza():
    def __init__(self, nazwa_firmy: str, wlasciciel_firmy: str, 
                 powierzchnia_firmy: float, liczba_pracownikow: int, adres_firmy: str) -> None:
        self._nazwa_firmy = nazwa_firmy
        self._wlasciciel_firmy = wlasciciel_firmy
        self._powierzchnia_firmy = powierzchnia_firmy
        self._liczba_pracownikow = liczba_pracownikow
        self._adres_firmy = adres_firmy
        
    @property
    def nazwa_firmy(self):
        return self._nazwa_firmy
    
    @property
    def wlasciciel_firmy(self):
        return self._wlasciciel_firmy
    
    @property
    def powierzchnia_firmy(self):
        return self._powierzchnia_firmy
    
    @property
    def liczba_pracownikow(self):
        return self._liczba_pracownik
    
    @property
    def adres_firmy(self):
        return self._adres_firmy
    
    def __str__(self) -> str:
        return f"""Firma spożywcza:\n\t
                    nazwa firmy: {self.nazwa_firmy}\n\t
                    właściciel firmy: {self._wlasciciel_firmy}\n\t
                    powierzchnia firmy: {self._powierzchnia_firmy}\n\t
                    liczba pracownikow: {self._liczba_pracownikow}\n\t
                    adres firmy: {self._adres_firmy}"""
                    
firma_tr = FirmaTransportowa("Adam Nowak", 102.3, "Katowice", "Wyszyńskiego 6", "21-345")
firma_sp_1 = FirmaSpozywcza("ABC", "Kamil Baran", 121.5, 6, "Chorzów, ul. Kościuszki 64")
firma_sp_2 = FirmaSpozywcza("Sklepik osiedlowy", "Ewa Nowakowska", 76, 3, "Katowice, ul. Zielona 75")

pojazd1 = Pojazd(4, "BMW", "dostawczy", "Adrian Korek", 3)

odcinek1 = Odcinek(firma_tr, firma_sp_1, 10.5, 0.5, "Jan Kowalski")
odcinek2 = Odcinek(firma_sp_1, firma_sp_2, 7.25, 1.5, "Jan Kowalski")
odcinek3 = Odcinek(firma_sp_2, firma_tr, 6.475, 0.5, "Jan Kowalski")
                 
kurs1 = Kurs([firma_tr, firma_sp_1, firma_sp_2, firma_tr], "Jan Kowalski", 
             pojazd1, "2.5", [odcinek1.odleglosc_km, odcinek2.odleglosc_km, odcinek3.odleglosc_km])
print(kurs1)
