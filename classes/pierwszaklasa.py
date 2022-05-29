# najprostszy sposob definiowania obiektu
# self reprezentuje instancje klasy. Dzieki uzyciu self mozemu miec dostep do wlasciwosci i funkcji testklasy
# tworzenie obiektu realizujemy przez tzw. konstruktor - jest to specjalna funkcja, ktora jest wykonywana, kiedy tworzymy nasz obiekt.
# w Pythonie taka funkcje pelni metoda __init__
class Paletka:
    def __init__(self, kolor):
        self.kolor_obiektu = kolor
        print(f"Utworzylismy obiekt o kolorze {self.kolor_obiektu}m. - ID: {id(self)}")
    def info(self):
        print(f"Kolor obiektu to: {self.kolor_obiektu}")
    def info_ex(self, nazwa):
        print(f"Kolor obiektu {nazwa} to: {self.kolor_obiektu}")
# pass jest to miejsce dla funkcjonalnosci, ktora bedzie dodana pozniej
# pass moze tez byc uzyte w ciele funkcji, ktore nic nie robi
# przyklad:
# def odejmij(a, b):
#     pass

# tworzymy obiekt na podstawie klasy
# 1. podajemy nazwe obiektu (paletka_a)
# 2. wywolujemy konstruktor klasy (Paletka())
def testklasy():
    paletka_a = Paletka("czerwony")
    paletka_b = Paletka("niebieski")
    print("*****************************")
    print(f"Obiekt typu {type(paletka_a)} zawiera od razu pewne wlasciwosci i funkcje:")
# f-string
# val = "Python course"
# print(f"Rezultat zwracany przez nasz zmienn to {val}"")

# name = "Kasia"
# age = 32
# print(f"imie {name} i wiek {age}")
    print(dir(paletka_a))
    print("*****************************")
    print(f"Obiekt typu {type(paletka_a)} zawiera od razu pewne wlasciwosci i funkcje:")
# f-string
# val = "Python course"
# print(f"Rezultat zwracany przez nasz zmienn to {val}"")

# name = "Kasia"
# age = 32
# print(f"imie {name} i wiek {age}")
    print(dir(paletka_a))
    print("*****************************")
    print(f"Obiekt typu {type(paletka_a)} zawiera od razu pewne wlasciwosci i funkcje:")
# f-string
# val = "Python course"
# print(f"Rezultat zwracany przez nasz zmienn to {val}"")

# name = "Kasia"
# age = 32
# print(f"imie {name} i wiek {age}")
    print(dir(paletka_a))
    print("*****************************")
    print(f"Obiekt typu {type(paletka_b)} zawiera od razu pewne wlasciwosci i funkcje:")
    print(dir(paletka_b))
    print(f"Kolor dla paletka_a: {paletka_a.kolor_obiektu}")
    print(f"Kolor dla paletka_b: {paletka_b.kolor_obiektu}")
    paletka_a.info()
    paletka_b.info()
    paletka_a.info_ex("a")
    paletka_b.info_ex("b")
