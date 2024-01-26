from random import randint

# létrehozol egy egész számokat tartalmazó listát
# hozzáadsz 30db kétszámjegyű véletlenszámot

# meghatározod a számok összegét
# a számok átlagát
# a 3-al osztható elemek számát
# a páratlan számok összegét

szamok:list[int] = []
for _ in range(30):
    szamok.append(randint(10, 99))
print(f'rnd számok: {szamok}')

osszeg:int = 0
paratlan_osszeg:int = 0
db_3aloszthato:int = 0

for e in szamok:
    osszeg += e
    if e % 3 == 0:
        db_3aloszthato += 1
    if e % 2 == 1:
        paratlan_osszeg += e
print(f'osszeg: {osszeg}')
print(f'atlag: {osszeg / len(szamok)}')
print(f'3al oszthatok száma: {db_3aloszthato}')
print(f'paratlanok osszege: {paratlan_osszeg}')