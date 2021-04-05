# Tema 1

# 1. Să se creeze o listă de numere întregi pozitive si negative de 10 elemente.
# Să se filtreze elementele listei astfel incat acestea sa fie pozitive și să se afișeze lista ordonata crescător.

'''
from pip._vendor.distlib.compat import raw_input

nrElementeLista = 10
lista = []
for element in range(nrElementeLista):
    element = int(raw_input("Adaugati un element in lista: "))
    lista.append(element)
    if element < 0:
        lista.remove(element)
lista.sort()

if len(lista) > 0:
    print(lista)
else:
    print("Nu au fost introduse valori pozitive! Lista este vida")
'''

# 2. Se da lista de orase de mai jos. Să se realizeze un dictionar care sa grupeze orasele dupa lungimea denumirii.
# Dictionarul va avea valorile si cheile ordonate in ordine crescatoare, respectiv alfabetica.
# lista_o = ['Vaslui','Cluj', 'Iasi', 'Alba', 'Oradea', 'Arad', 'Craiova', 'Mehedinti', 'Bucuresti', 'Orastie’]

'''
listaOrase = ["Vaslui", "Cluj", "Iasi", "Alba", "Oradea", "Arad", "Craiova", "Mehedinti", "Bucuresti", "Orastie"]
listaOrase.sort()
dictionarOrase = {}
for oras in listaOrase:
    dictionarOrase[oras] = len(oras)
print(sorted(dictionarOrase.items(), key = lambda x: x[1]))
'''

#3. Se da o listă de liste cu denumiri de electrocasnice si electronice (televizor, frigider, laptop_tip1,laptop_tip2), prețul și cantitatea acestora.
# Calculați valoarea fiecărui echipament, adăugați-o în lista fiecarui produs și sortați în funcție de pret, utilizand functia lambda.
# Pentru produsele care au pretul mai mare de 3000 si cantitatea mai mare de 5 produse, se va diminua pretul cu 10%.
#lista = [['tv', 3500,9], ['frigider', 2500, 4], ['laptop_tip1',5000,5],['laptop_tip2',10000,6]]

'''
listaDeListe = [['tv', 3500, 9], ['frigider', 2500, 4], ['laptop_tip1', 5000, 5], ['laptop_tip2', 10000, 6]]
# lista[0] = tv, frigider, laptop_tip1, laptop_tip2
# lista[1] = 3500, 2500, 5000, 10000
# lista[2] = 9, 4, 5, 6
for lista in listaDeListe:
    valoare = lista[1] * lista[2]  #valoareEchipament = pret*cantitate
    lista.append(valoare)

    if lista[1] > 3000 and lista[2] > 5:
         discount = lista[1] * 0.1
         lista[1] -= discount
         
listaDeListe.sort(key=lambda x: x[1])
print(listaDeListe)
'''

#4. Să dau două liste de liste: lista produse aflate pe stoc (lps cu denumire_produs si cantitate) și lista produse comandate (lpc cu denumire_produs si cantitate).
# Să se afiseze numele produselor care nu au fost comandate. Sa se calculeze diferenta dintre cantitatea aflata pe stoc si cantitatea comandata si sa se actualizeze cantitatea aflata pe stoc.
# Daca cantitatea comandata este mai mare decat cantitatea aflata pe stoc, aceasta va fi egala cu 0.
#lps=[['tableta',13], ['tv',50], ['smart_phone',4],['laptop_tip1',41], ['desktop',60], ['tastatura',16], ['monitor32inch',28], ['flipchart',6], ['carioca',200]]
#lpc=[['tv',52],['laptop_tip1',20], ['desktop',11], ['tastatura',3], ['monitor32inch',11], ['flipchart',1]]

'''
lps = [["tableta", 13], ["tv", 50], ["smart_phone", 4],["laptop_tip1", 41], ["desktop", 60], ['tastatura', 16], ["monitor32inch", 28], ["flipchart", 6], ["carioca", 200]]
lpc = [["tv", 52],["laptop_tip1", 20], ["desktop", 11], ["tastatura", 3], ["monitor32inch", 11], ["flipchart", 1]]
lista = []
for stoc in lps:
    lista.append(stoc[0])
for comanda in lpc:
    lista.append(comanda[0])
for element in lista:
    if lista.count(element) == 1:
        print('Produs care nu a fost comandat: ' + element)
for comanda in lpc:
    cant_comanda = comanda[1]
    for stoc in lps:
        cant_stoc = stoc[1]
        if comanda[0] == stoc[0]:
            diferenta= cant_stoc - cant_comanda
            if diferenta < 0:
                stoc[1] = 0
            else:
                stoc[1] = diferenta
print(lps)
'''

#5. Să se creeze o listă de dicționare cu următoarele chei: id, denumire, pret și cantitate pentru produsele: televizor, laptop, frigider.
#lista = [{"id":1, "denumire":"tv", "pret":3500, "cantitate":30},
# {"id":2, "denumire":"laptop", "pret":10000, "cantitate":65},
# {"id":3, "denumire":"frigider", "pret":2500, "cantitate":48}]
#Dacă produsele au pretul mai mare decât 5000 sau cantitatea este mai mare decat 20, să se reduca pretul cu 5%.
'''
lista = [{"id":1, "denumire":"tv", "pret":3500, "cantitate":30}, {"id":2, "denumire":"laptop", "pret":10000, "cantitate":65}, {"id":3, "denumire":"frigider", "pret":2500, "cantitate":48}]
for element in lista:
    pret = element.get("pret")
    cantitate = element.get("cantitate")
    if pret > 5000 and cantitate > 20:
        pret -= pret * 0.05
        element.update({"Pret modificat: ":pret})
print(lista)
'''

#6. Să se creeze o listă li1, formată din primele m numere naturale, apoi să se realizeze o funcție prin care să se creeze o listă li2 formată din numerele prime ale listei li1.
#se citeste de la tastatura dimensiunea
'''
from pip._vendor.distlib.compat import raw_input
li1 = []
m = int(raw_input("m= "))
for element in range(m):
    element = int(raw_input("Adaugati un element in lista: "))
    li1.append(element)
    if element < 0:
        li1.remove(element)
if len(li1)>0:
    print('Lista de numere naturale introduse: ')
    print(li1)
else:
    print("Nu au fost introduse valori pozitive! Lista este vida")
li2 = []
for element in li1:
    nrDivizori = 0
    d = 1
    while d <= element:
        if element % d == 0:
            nrDivizori += 1
        d += 1
    if nrDivizori == 2:
        li2.append(element)
if len(li2) > 0:
    print('Lista cu numere prime: ')
    print(li2)
else:
    print("Nu exista numere prime")
'''

#7. Sa se deschida fisierul csv clienti_leasing si sa se stocheze in 3 liste valorile din coloanele name_client, venit_per_year_ron si description.
# Sa se determine de cate ori apare produsul bancar 'CAMIN SUPER BCR - TL  dob. fixa 1 an - dob. referinta  var. ulterior IND EUR' in coloana descriere
'''
import pandas as pd
fisier = pd.read_csv('clienti_leasing.csv')
# print(fisier)
nume = list(fisier.loc[:,"NUME_CLIENT"])
#print(nume)
venit = list(fisier.loc[:,"VENIT_ANUAL_RON"])
#print(venit)
descriere = list(fisier.loc[:,"DESCRIERE"])
#print(descriere)
nr = descriere.count("CAMIN SUPER BCR - TL  dob. fixa 1 an - dob. referinta  var. ulterior IND EUR")
print("Aparitii CAMIN SUPER BCR - TL  dob. fixa 1 an - dob. referinta  var. ulterior IND EUR in descriere: ")
print(nr)
'''

# Tema 2

#1. Să se reprezinte grafic (de tip pie) valoarea medie a daunelor pentru al doilea semestru pentru marcile Audi si Ford pentru fiecare an de fabricatie
'''
import pandas as pd
from pprint import pprint
from matplotlib import pyplot as plt
fisier = pd.read_csv("clienti_daune.csv")
fisier['DATA_CERERE'] = pd.to_datetime(fisier['DATA_CERERE'])
# pprint(fisier['DATA_CERERE'])
fisier = fisier[(fisier.MARCA == 'AUDI') | (fisier.MARCA == 'FORD')]
fisier = fisier[((pd.DatetimeIndex(fisier['DATA_CERERE']).month) >= 4) & ((pd.DatetimeIndex(fisier['DATA_CERERE']).month) <= 6)]
fisier = fisier.groupby('AN_FABRICATIE')['VALOARE_DAUNA'].mean()
#pprint(fisier)
fisier.sort_values().plot(kind='pie')
plt.xlabel('An fabricatie')
plt.ylabel('Valoarea medie a daunei')
plt.title('Valoarea medie a daunei/an fabricatie FORD si AUDI (sem II)')
plt.legend()
plt.show()
'''

#2. Sa se grupeze dupa tara producatoare si sa afiseze valoarea medie a pretului manoperei
'''
import pandas as pd
from pprint import pprint
fisier = pd.read_csv('clienti_daune.csv')
#pprint(fisier)
pd.options.display.max_rows= 999
print(round(fisier.groupby('TARAPRODUCATOR')['PRET_MANOPERA'].mean(),2))
'''

#3. Sa se grupeze dupa tara producatoare si sa afiseze tara producatoare si toate tagurile fiecarei marci din tara producatoare respctiva. Sa se calculeze de cate ori apare tagul bad pentru fiecare tara producatoare.
'''
import pandas as pd
from pprint import pprint
fisierDaune = pd.read_csv('clienti_daune.csv')
fisierMasini = pd.read_csv('cars.csv')
fisierMasini = fisierMasini.rename(columns={'MARCA_CARS':'MARCA'})
rezultat = pd.merge(fisierDaune[['MARCA','TARAPRODUCATOR']], fisierMasini[['MARCA','TAGS']], on='MARCA')
print(rezultat.groupby(['TARAPRODUCATOR','MARCA','TAGS']).agg({'TAGS':'count'}))
rezultat=rezultat.loc[(rezultat['TAGS']=='bad')]
print('Tagul BAD pentru fiecare tara: ')
print(rezultat.groupby(['TARAPRODUCATOR']).agg({'TAGS':'count'}))
'''

#4. Să se creeze setul format din user_usage și supported_devices și să se reprezinte grafic (bare verticale) traficul însumat (coloana monthly_mb) pentru fiecare brand (coloana Retail Branding).
'''
import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt
user_usage = pd.read_csv('user_usage.csv')
user_device = pd.read_csv('user_device.csv')
supported_devices = pd.read_csv('supported_devices.csv')
rezultat = pd.merge(user_usage,user_device[['use_id', 'device']],on='use_id',how='left')
supported_devices.rename(columns={"Retail Branding": "manufacturer"}, inplace=True)
rezultat = pd.merge(rezultat,supported_devices[['manufacturer', 'Model']],left_on='device',right_on='Model',how='left')
print(rezultat.groupby("manufacturer").agg({"monthly_mb": "sum"}))
rezultat.groupby("manufacturer").agg({"monthly_mb": "sum"}).plot(kind='bar')
plt.ylabel('manufacter')
plt.xlabel('monthly_mb')
plt.show()
'''
#5. Să se afișeze, utilizând fișierul phone_data.csv, durata însumata pentru fiecare lună și durata însumată pentru un anumit tip de rețea (mobile) pentru fiecare lună.
'''
import pandas as pd
pd.set_option("display.max_columns", 10)
fisier = pd.read_csv('phone_data.csv')
print('\nDurata pe fiecare luna')
print(fisier.groupby('month')['duration'].sum())
print('\nDurata pe tip de retea mobila')
print(fisier[fisier['network_type'] == 'mobile'].groupby('month')['duration'].sum())
'''

#6. Sa se construiasca un pivot table utilizand datele: http://bit.ly/2cLzoxH
'''
import pandas as pd
date = pd.read_csv('https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv')
#print(date)
pivot = date.pivot(index='country', columns='year', values=['continent','pop', 'lifeExp', 'gdpPercap'])
print(pivot)
'''

#7. Sa se reprezinte grafic sub forma de bare 3 marci din Europa care au cele mai mici daune totale
'''
import pandas as pd
import matplotlib.pyplot as plt
fisier = pd.read_csv('clienti_daune.csv')
fisier = fisier[(fisier["REGIUNEPRODUCATOR"] == "Europe")].groupby('MARCA')['VALOARE_DAUNA'].sum().nsmallest(3)
fisier.plot(kind='bar', color=["blue", "green", "yellow"])
plt.show()
'''