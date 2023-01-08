import json

with open('projektit.json', 'r', encoding='utf-8') as projektit:
    projektilista = json.load(projektit)

# Sorttaus järjestyksen mukaan
projektilista = sorted(projektilista, key=lambda x: x['järjestys']) 
#print(format(projektilista))
nimi = 'bingo'
for i in range(0, len(projektilista)):
    if projektilista[i]['konenimi'] == nimi:
        nimi = projektilista[i]['nimi']    
        numero = i
print(numero, nimi)

#for dict in projektilista:
#    if dict['konenimi'] == nimi:
#        nimi = dict['nimi']
