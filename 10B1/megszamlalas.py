# megszámlálás tétele

sorozat:list[int] = [11, 26, 3, 71, 32]
# 'kritérium': páros szám
db:int = 0
for elem in sorozat:
    if elem % 2 == 0:
        db += 1
print(f'sorozat elemei: {sorozat}')
print(f'páros számok darabszáma: {db}')

# ------------------------------

szavak:list[str] = ['gólya', 'hajó', 'cica', 'rejtély', 'lyuk']
# condition: van a szóban "ly"
db:int = 0
for szo in szavak:
    if 'ly' in szo:
        db += 1
print(f'szavak listája: {szavak}')
print(f'"ly"-t tartalmazó szavak száma: {db}')