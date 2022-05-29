# najprostszy sposob definiowania obiektu
class Paletka:
    pass
# pass jest to miejsce dla funkcjonalnosci, ktora bedzie dodana pozniej
# pass moze tez byc uzyte w ciele funkcji, ktore nic nie robi
# przyklad:
# def odejmij(a, b):
#     pass

# tworzymy obiekt na podstawie klasy
# 1. podajemy nazwe obiektu (paletka_a)
# 2. wywolujemy konstruktor klasy (Paletka())
def testklasy():
    paletka_a = Paletka()
    print(f"Obiekt typu {type(paletka_a)} zawiera od razu pewne wlasciwosci i funkcje:")
# f-string
# val = "Python course"
# print(f"Rezultat zwracany przez nasz zmienn to {val}"")

# name = "Kasia"
# age = 32
# print(f"imie {name} i wiek {age}")
    print(dir(paletka_a))
