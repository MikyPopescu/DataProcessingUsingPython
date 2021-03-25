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

if len(lista)>0:
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
listaProduseAflatePeStoc = [["tableta", 13], ["tv", 50], ["smart_phone", 4],["laptop_tip1", 41], ["desktop", 60], ['tastatura', 16], ["monitor32inch", 28], ["flipchart", 6], ["carioca", 200]]
listaProduseComandate = [["tv", 52],["laptop_tip1", 20], ["desktop", 11], ["tastatura", 3], ["monitor32inch", 11], ["flipchart", 1]]
list=[]
#adaugarea tuturor subliste intr-o singura lista si verificarea apoi a produselor care apar o singura data si afisarea lor
for stoc in listaProduseAflatePeStoc:
    list.append(stoc[0])
for comanda in listaProduseComandate:
    list.append(comanda[0])
for item in list:
    if list.count(item) == 1:
        print('Produs necomandat: ' + item)
for comanda in listaProduseComandate:
    #cantitate comanda
    cant_comanda = comanda[1]
    for stoc in listaProduseAflatePeStoc:
        #cantitate stoc
        cant_stoc = stoc[1]
        #daca au aceeasi denumire
        if comanda[0] == stoc[0]:
            diferenta= cant_stoc - cant_comanda
            if diferenta < 0:
                stoc[1] = 0
            else:
                stoc[1] = diferenta
print(listaProduseAflatePeStoc)
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
    if pret >5000 and cantitate>20:
        pret = pret - pret*0.05
        element.update({"pret":pret})
print(lista)
'''

#6. Să se creeze o listă li1, formată din primele m numere naturale, apoi să se realizeze o funcție prin care să se creeze o listă li2 formată din numerele prime ale listei li1.

#se citeste de la tastatura dimensiunea
'''
from pip._vendor.distlib.compat import raw_input

m = int(raw_input("Introduceti m= "))
li1=[]
for item in range(m):
    li1.append(item)

print('Lista primelor numerelor naturale')
print(li1)

li2=[]
for nr in li1:
    divizori = 0
    d=1
    while d <= nr:
        if nr % d == 0:
            divizori += 1
        d += 1
    if divizori == 2:
        li2.append(nr)
print('Numerele prime sunt: ')
print(li2)
'''
#7. Sa se deschida fisierul csv clienti_leasing si sa se stocheze in 3 liste valorile din coloanele name_client, venit_per_year_ron si description.
# Sa se determine de cate ori apare produsul bancar 'CAMIN SUPER BCR - TL  dob. fixa 1 an - dob. referinta  var. ulterior IND EUR' in coloana descriere
import pandas

df =pandas.read_csv('clienti_leasing.csv')
print(df)