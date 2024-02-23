# Turite duomenis apie UAB „Autoparkas“ priklausančius automobilius.
# Duomenų faile (txt ar csv) pateikta ši informacija: valstybinis numeris, gamintojas, modelis, pagaminimo metai.
#
# Reikalavimai: Naudoti sąrašus,failų skaitymą ir rašymą, funkcijas.
#
from csv import reader, writer, DictReader, DictWriter
import datetime

with open('autoparkas.csv', encoding='utf8') as failas:
    skaitytojas = reader(failas, delimiter=',')
    next(skaitytojas)
    skaitytojas = list(skaitytojas)

#1. Raskite, kurių gamintojų automobilių yra daugiau nei vienas, ekrane atspausdinkite gamintojų pavadinimus.
# (Atspausdinkite ir kiekį - NEBŪTINA)

orginalus = []

for eilute in skaitytojas:
    orginalus.append(eilute[1])
print(orginalus)
print('==================')

unikalus = set(orginalus)
print(unikalus)

print('==================')
for marke in unikalus:
    if orginalus.count(marke) > 1:
        print(f'Gamintojai, kurie turi daugiau nei viena automobili: {marke}')
print('===================')
# 2. Sudarykite visų pasirinkto gamintojo (pvz.: „Volvo“) automobilių sąrašą,
# # ekrane atspausdinkite automobilio valstybinį numerį, modelį, bei pagaminimo metus.
# # Jei tokio automobilio sąraše nėra atspausdinkite pranešimą - "Tokio gamintojo automobilių sąraše nėra".
#
automobilis = input('Iveskite, koki automobili norite rasti (zodi rasykite didziaja raide): ')
auto = 0

for eilute in skaitytojas:
    if eilute[1] == automobilis:
        print(automobilis, 'numeris:', eilute[0], 'modelis:', eilute[2], 'pagaminimo metai:', eilute[3])
        auto += 1
if not auto:
    print('Tokio automobilio sarase nera')

print('==================')
# # 3 Sudarykite sąrašą, senesnių nei 10 metų, į failą „Senienos.csv“ surašykite visus jų duomenis.
# # # Jei senienų programa neranda atspausdinkite pranešimą į failą - "Senesnių nei 10 metų automobilių sąraše nėra".

dabar = datetime.datetime.now().year

with open('autoparkas.csv', encoding='utf8') as failas:
    skaitytojas = list(DictReader(failas))

for eilute in skaitytojas:
    eilute['Amzius'] = dabar - int(eilute['Metai'])
    print(eilute)
print('====================')

zodynas = skaitytojas[0]
raktai = zodynas.keys()

senesni_10m = []
for eilute in skaitytojas:
    if eilute['Amzius'] > 10:
        senesni_10m.append(eilute)
        print('Senesnes nei 10 metu masinos', eilute)

if len(senesni_10m) != 0:
    with open('Senienos.csv', 'w', encoding='utf8', newline='') as failas:
        stulpeliu_pavadinimai = raktai
        rasytojas = DictWriter(failas, fieldnames=stulpeliu_pavadinimai)
        rasytojas.writeheader()

        for eilute in senesni_10m:
            rasytojas.writerow(eilute)
else:
    print('Senesniu masinu nei 10 m. parke nera')