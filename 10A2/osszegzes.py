sorozat:list[int] = [11, 26, 3, 71, 32]
print(f'INPUT: számsorozat: {sorozat}')
osszeg:int = 0
for elem in sorozat:
    osszeg += elem
print(f'OUTPUT: számok összege: {osszeg}')

# --------------
szavak:list[str] = ['bab', 'szem', 'jankó']
osszetett_szo:str = ''
for szo in szavak:
    osszetett_szo += szo

print(f'szaval listája: {szavak}')
print(f'összetett szó: {osszetett_szo}')

# --------------
# szorzatszámítás
szamok:list[int] = [1, 2, 3, 4, 5]
szorzat:int = 1
for szam in szamok:
    szorzat *= szam
print(f'5! értéke: {szorzat}')