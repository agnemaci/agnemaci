import sqlite3
# 1
conn = sqlite3.connect("saldainiu_baze.db") # rysys su duomenu baze
c = conn.cursor() # zymeklis

# 2
with conn:
    c.execute("CREATE TABLE IF NOT EXISTS Saldainiai (Pavadinimas text, Tipas text, Kaina_kg integer, Perkamas_kiekis integer, Kaina integer)")
saldainiai = [
    ("Aurora", "Kokosinis", 4, 10),
    ("Rūpintojė", "Karamelinis", 3, 15),
    ("Saulutė", "Bravorinis", 5, 8),
    ("Žiema", "Saldainių", 7, 12),
    ("Vėjopatis", "Likerinis", 8, 6),
    ("Gintarinė", "Agurkinis", 2, 20),
    ("Kukurūzai", "Želė", 6, 10),
    ("Šaltibarščiai", "Šokoladinis", 4, 18),
    ("Medus", "Bandelių", 5, 14),
    ("Lietuviškas Skonis", "Riešutų", 7, 7)
     ]
# c.executemany('INSERT OR REPLACE INTO Saldainiai (Pavadinimas, Tipas, Kaina_kg, Perkamas_kiekis) VALUES (?, ?, ?,?)', saldainiai)
print('==================================')

#  3.  Užpildykite stulpelį Kaina įtraukdami apskaičiuotas sumos vertes prie atitinkamo saldainio.

with conn:
    c.execute("SELECT * From Saldainiai")
    print(c.fetchall())

for saldainis in saldainiai:
    kaina = saldainis[2] * saldainis[3]
    print(kaina)
    c.execute(f'UPDATE saldainiai SET Kaina=Kaina_kg*Perkamas_kiekis')
print('==================================')

# 4. Atspausdintų tik tuos saldainius kurių tipas "Šokoladinis" ir kaina > 5 eur.

ivedimas = ''

while ivedimas != 'n':
    print("Iveskite, kokio tipo ir kainos saldaini norite rasti (tipas rasomas su didziaja raide): ")
    tipas = input("Tipas: ")
    kaina = int(input("Kaina: "))

    with conn:
        c.execute("SELECT * FROM Saldainiai WHERE Tipas = ? AND Kaina > ?", (tipas, kaina))
        rez = c.fetchall()

        if rez:
            print("Rasti saldainiai:")
            for eilute in rez:
                print(eilute)
        else:
            print('Tokio tipo ir kainos saldainio nera ')

    ivedimas = input("Jei norite nutraukti ivedima spauskite 'n', jei norite testi spauskite bet ka: ")

print('==================================')

# 5. Panaikintų input pagalba įvesto saldainio pavadinimimo duomenis - ištrintų visą eilutę lentelėje apie tą saldainį.

ivedimas = ''

while ivedimas != 'n':
    print("Iveskite, kuri saldaini norite istrinti: ")
    pavadinimas = input("Pavadinimas: ")

    with conn:
        c.execute("DELETE FROM Saldainiai WHERE Pavadinimas = ?", (pavadinimas,))
        if c.rowcount > 0:
            print(f"Saldainis {pavadinimas} buvo sekmingai istrintas.")
        else:
            print('Tokio saldainio nera ')

    ivedimas = input("Jei norite nutraukti ivedima spauskite 'n', jei norite testi spauskite bet ka: ")

# 6. Spausdinkite tarpinius rezultatus kiekvieną eilutę atskirai. Pvz.
# ("Miglė", "Šokoladinis", 6, 2,)
# ("Miglė", "Šokoladinis", 6, 2,)
# ("Miglė", "Šokoladinis", 6, 2,)

for sal in saldainiai:
    print(sal)

conn.commit()
conn.close()
print('==================================')

# 7. Naudodamiesi Seaborn arba Matplotlib Python bibliotekomis, atvaizduokite bent du grafikus (skirtingų tipų - linijinių, stulpelinių, taškinių ar kt. ) Kaina/Saldainis.
# Pakaitaliokite grafikų parametrus, pvz. spalvų paletė. Grafikai turi turėti ašių pavadinimus, vertes ant ašių, pavadinimą. Dar gali turėti legentdą ar kt. pasirinktą info.

kaina = [40,45,40,84,48,40,60,72,70,49]
pavadinimas = ['Aurora',
               'Rūpintojė',
               'Saulutė',
               'Žiema',
               'Vėjopatis',
               'Gintarinė',
               'Kukurūzai',
               'Šaltibarščiai',
               'Medus',
               'Lietuviškas Skonis'
               ]
from matplotlib import pyplot as plt

plot1 = plt.figure(1)
plt.plot(kaina, pavadinimas)
plt.legend(['Saldainiu kaina'])
plt.title('Saldainiu kainu palyginimas')
plt.xlabel('Kaina')
plt.ylabel('Saldainiu pavadinimas')

plot2 = plt.figure(2)
plt.plot(pavadinimas, kaina)
plt.legend(['Saldainiu kaina'])
plt.title('Saldainiu kainu palyginimas***')
plt.xlabel('Saldainiu pavadinimai')
plt.ylabel('Kaina')

plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()
ax.bar(pavadinimas, kaina, color='skyblue')
plt.legend(['Saldainių kaina'])
plt.title('Saldainių kainų palyginimas')
plt.xlabel('Saldainių pavadinimai')
plt.ylabel('Kaina')
plt.xticks(rotation=45, ha='right')

plt.show()


