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
db_paratlan:int = 0
sum_3aloszthatok:int = 0
for n in szamok:
    osszeg += n
    if n % 2 == 1:
        db_paratlan += 1
    if n % 3 == 0:
        sum_3aloszthatok += n
print(f'összeg: {osszeg}')
print(f'átlag: {osszeg/len(szamok)}')
print(f'páratlanok száma: {db_paratlan} db')
print(f'3al oszthatók összege: {sum_3aloszthatok}')