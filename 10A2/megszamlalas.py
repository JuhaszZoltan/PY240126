# megszámlálás tétele
# adott kritériumnak megfelelő elemek száma a sorozatban

# input: sorozat
# output: egész szám
# 'condition': "kritérium" azaz az a logikai feltétel, aminek meg kell felelni a sorozat egyes elemeinek

sorozat:list[int] = [11, 26, 3, 71, 32]
darabszam:int = 0
# feltétel: páros szám

for elem in sorozat:
    if elem % 2 == 0:
        darabszam += 1
print(f'számok: {sorozat}')
print(f'páros elemek száma: {darabszam} db')

# -------------------
szavak:list[str] = ['csirke', 'gólya', 'tojás', 'folyó', 'rejtély']
# azon szavak száma, amiben van "ly"
darabszam:int = 0
for szo in szavak:
    if 'ly' in szo:
        darabszam += 1
print(f'szavak: {szavak}')
print(f'szavak száma, amiben van "ly": {darabszam} db')