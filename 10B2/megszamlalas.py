# megszámlálás tétele

sorozat:list[int] = [11, 26, 3, 71, 32]
# 'condition': páros szám
db:int = 0
for elem in sorozat:
    if elem % 2 == 0:
        db += 1
print(f'számsorozat: {sorozat}')
print(f'páros számok száma: {db} db')

# ------------------------

szavak:list[str] = ['gólya', 'bableves', 'hajó', 'tojás', 'rejtély']
# kritérium: van benne "ly"
db:int = 0
for szo in szavak:
    if 'ly' in szo:
        db += 1
print(f'szavak listája: {szavak}')
print(f'"ly"-t tartalmazó szavak száma: {db} db')

szamok:list[float] = [12.4, -311.5, 0.67, -6, -49, 16.01]
# condition: pozitív
db:int = 0
for szam in szamok:
    if szam > 0:
        db += 1
print(f'számok: {szamok}')
print(f'pozitív számok száma: {db} db')