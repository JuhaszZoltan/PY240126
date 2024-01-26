from random import randint

# létrehozol egy listát egész számoknak
# hozzáadsz 30 db két számjegyű véletlenszámot
# meghatározod az elemek összegét
# az elemek átlagát
# 3-mal maradék nélkül osztható elemek számát

numbers:list[int] = []
for _ in range(30):
    numbers.append(randint(10, 99))
print(f'30 rnd num: {numbers}')

osszeg:int = 0
darab:int = 0
for n in numbers:
    osszeg += n
    if n % 3 == 0: darab += 1

print(f'összeg: {osszeg}')
print(f'átlag: {osszeg/len(numbers)}')
print(f'3am oszthatók száma: {darab}')