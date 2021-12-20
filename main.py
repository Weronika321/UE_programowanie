from FirmaSpozywcza import FirmaSpozywcza
from FirmaTransportowa import FirmaTransportowa
from Pojazd import Pojazd
from Odcinek import Odcinek
from Kurs import Kurs


firma_tr = FirmaTransportowa(
    "Adam Nowak", 102.3, "Katowice", "Wyszyńskiego 6", "21-345"
)
firma_sp_1 = FirmaSpozywcza(
    "Bartek Jankowski", 121.5, "Chorzów", "ul. Kościuszki 64", "18-432"
)
firma_sp_2 = FirmaSpozywcza(
    "Anna Kwiatkowska", 76, "Katowice", "ul. Zielona 75", "31-212"
)

pojazd1 = Pojazd(4, "BMW", "dostawczy", "Adrian Korek", 3)

odcinek1 = Odcinek(firma_tr, firma_sp_1, 10.5, 0.5, "Jan Kowalski")
odcinek2 = Odcinek(firma_sp_1, firma_sp_2, 7.25, 1.5, "Jan Kowalski")
odcinek3 = Odcinek(firma_sp_2, firma_tr, 6.475, 0.5, "Jan Kowalski")

kurs1 = Kurs(
    [
        firma_tr.wlasciciel_firmy,
        firma_sp_1.wlasciciel_firmy,
        firma_sp_2.wlasciciel_firmy,
        firma_tr.wlasciciel_firmy,
    ],
    "Jan Kowalski",
    pojazd1,
    "2.5",
    [odcinek1.odleglosc_km, odcinek2.odleglosc_km, odcinek3.odleglosc_km],
)
# print(kurs1)
print(kurs1)
