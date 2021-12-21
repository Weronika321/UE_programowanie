from Dom import Dom
from Mieszkanie import Mieszkanie
from Zamowienie import Zamowienie


dom = Dom(200, 1000000, "ul. Kwiatkowska 32", 300)
mieszkanie = Mieszkanie(50, 300000, "ul. Zielona 42", 3)

zamowienie = Zamowienie(
    dom.powierzchnia, dom.cena, mieszkanie.cena, mieszkanie.powierzchnia
)

print(zamowienie)
