# sorozatszámítás tétele

# összegzés
sorozat:list[int] = [11, 26, 3, 71, 32]
osszeg:int = 0
for elem in sorozat:
    osszeg += elem
print(f'számsorozat: {sorozat}')
print(f'sorozat elemeinek összege: {osszeg}')

# ----------------------

# konkatenáció
szavak:list[str] = ['bab', 'szem', 'jankó']
szoosszetetel:str = ''
for szo in szavak:
    szoosszetetel += szo
print(f'szavak egyenként: {szavak}')
print(f'összetett szó: {szoosszetetel}')

# ----------------------

# szorzatszámítás:
szamok:list[int] = [1, 2, 3, 4, 5]
szorzat:int = 1
for szam in szamok:
    szorzat *= szam
print(f'5!: {szorzat}')