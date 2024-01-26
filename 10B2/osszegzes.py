# sorozatszámítás tétele
# összegzés:

sorozat:list[int] = [11, 26, 3, 71, 32]
osszeg:int = 0
for elem in sorozat:
    osszeg += elem
print(f'input sorozat: {sorozat}')
print(f'output számok összege: {osszeg}')

# ------------------------

szavak:list[str] = ['bab', 'szem', 'jankó']
szoosszetetel:str = ''
for szo in szavak:
    szoosszetetel += szo
print(f'szavak listája: {szavak}')
print(f'összetett szó: {szoosszetetel}')

# ------------------------

szamok:list[int] = [1, 2, 3, 4, 5]
szorzat:int = 1
for szam in szamok:
    szorzat *= szam
print(f'5! (öt faktoriális): {szorzat}')