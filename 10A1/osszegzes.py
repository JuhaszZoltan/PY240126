# összegzés tétele

# input: bármilyen sorozat (pl. egy lista).
# fotos, hogy a listának az elemein értelmezhető legyen a "+" operátor (tehát pl. int, float, str)

# output: a lista elemeinek összege
#         (str esetében konkateációja)

# pl.:
sorozat:list[int] = [11, 26, 3, 71, 32]
print(f'INPUT: számsorozat: {sorozat}')

osszeg:int = 0
for elem in sorozat:
    osszeg += elem

print(f'OUTPUT: elemek összege a sorozatban: {osszeg}')

# milyen "j" vel írják azt a szót, hogy "tojás"? 50p

szavak:list[str] = ['bab', 'szem', 'jankó']
print(f'szavak: {szavak}')
szoosszetetel:str = ''
for szo in szavak:
    szoosszetetel += szo
print(f'összetett szó: {szoosszetetel}')

# szorzatszámítás:
szamok:list[int] = [1, 2, 3, 4, 5]
szorzat:int = 1
for szam in szamok:
    szorzat *= szam
print(f'{szamok} szorzata (5!): {szorzat}')