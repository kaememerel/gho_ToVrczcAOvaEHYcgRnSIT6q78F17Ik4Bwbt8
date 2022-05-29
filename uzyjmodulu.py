# importujemy modul i nadajemy mu alias
from mytoolkit import matematyczny as mat
from mytoolkit import pomocniczy as pom
# wywolanie funkcji z mytoolkit/matematyczny (alias: 'mat')
print(mat.dodaj(4,14))
print(mat.odejmij(10, 5))
# wywolanie funkcji z mytoolkit/pomocniczy
pom.czesc()
