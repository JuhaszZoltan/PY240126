from random import randint
# létrehozol egy egész számokat tartalmazó listát
# hozzáadsz 30db kétszámjegyű véletlenszámot

# meghatározod:
    # a számok átlagát
    # a 3-al osztható elemek számát
    # a páratlan számok összegét

szamok:list[int] = []
print(f'rnd számok:')
for i in range(30):
    szamok.append(randint(10, 99))
    print(szamok[i], end=' ')
    if (i+1) % 5 == 0: print(end='\n')

full_sum:int = 0
div3_count:int = 0
odd_sum:int = 0

for n in szamok:
    full_sum += n
    if n % 3 == 0: div3_count += 1
    if n % 2 == 1: odd_sum += n

print(f'átlag: {full_sum/len(szamok)}')
print(f'3al oszthatok szama: {div3_count} db')
print(f'paratlanok osszege: {odd_sum}')