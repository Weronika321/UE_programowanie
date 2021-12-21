from Dom import Dom
from Mieszkanie import Mieszkanie
from Zamowienie import Zamowienie
from Developer import Developer


dom = Dom(200, 1000000, "ul. Kwiatkowska 32", 300)
mieszkanie = Mieszkanie(50, 300000, "ul. Zielona 42", 3)
developer = Developer(
    "Pan domek", "Adrian", "Kowalski", "Katowice, ul. Bankowa 5"
)

zamowienie = Zamowienie(developer, 2, 8, [dom, mieszkanie])

print(zamowienie)
