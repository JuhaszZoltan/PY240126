# megszámlálás tétele
# INPUT: sorozat
# <elemekre vonatkoztatható logikai kritérium> (condition)
# OUTPUT: egész szám
# (a kritériumnak eleget tevő elemek száma a sorozatban)

sorozat:list[int] = [11, 26, 3, 71, 32]
darabszam:int = 0
for elem in sorozat:
    if elem % 2 == 0:            # feltétel: az elem páros
        darabszam += 1
print(f'INPUT: számsorozat: {sorozat}')
print(f'OUTPUT: páros elemek száma: {darabszam} db')

szavak:list[str] = ['gólya', 'hajó', 'tojás', 'lyuk', 'rejtély']
# hány szóban van 'ly'?
darabszam:int = 0
for szo in szavak:
    if 'ly' in szo:
        darabszam += 1
print(f'szavak: {szavak}')
print(f'"ly"-os szavak száma: {darabszam}')
