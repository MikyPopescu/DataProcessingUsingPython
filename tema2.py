

#1. Să se returneze într-un df componenta, anul de fabricatie și pretul manoperei pentru autoturismele Ford și Jeep. Pe setul din df, majorați cu 10% pretul manoperei pentru autoturismele fabricate inainte de 2010 și care au componenta BATTERY defectă. Salvați modificările într-un fișier .csv.
'''
import pandas as pd
import cx_Oracle
from pprint import pprint
import matplotlib.pyplot as plt
from click._compat import raw_input
connection = cx_Oracle.connect("BDSA_POPESCUM", "STUD", "193.226.34.57/oradb")
query="""SELECT componenta, cast(an_fabricatie as int) as an, pret_manopera  FROM t_clienti_daune where marca in ('FORD','JEEP')"""
df = pd.read_sql(query, con=connection)
df.loc[(df["AN"] < 2010) & (df["COMPONENTA"] == "BATTERY"), ["PRET_MANOPERA"]] = df["PRET_MANOPERA"] + df["PRET_MANOPERA"] * 0.1
#pprint(df)
df.to_csv("clienti.csv");
'''

#2. Încărcați într-un df marca, modelul, valoarea medie și numărul de daune pe fiecare model și marcă. Afișați numărul de autoturisme pentru care valoarea medie depășește 400 lei. Reprezentați grafic modelele care au înregistrat mai mult de 200 de daune.
'''
import cx_Oracle
import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt

connection = cx_Oracle.connect("BDSA_POPESCUM", "STUD", "193.226.34.57/oradb")
query="""SELECT marca, model, AVG(valoare_dauna) as VALOARE_MEDIE, COUNT(dauna) as NR_DAUNE FROM t_clienti_daune group by marca,model"""
df = pd.read_sql(query, con=connection)
print((df[df["VALOARE_MEDIE"] > 400]).count())
df = df[df["NR_DAUNE"] > 200]
df.plot(kind='bar', color='green', x='MODEL', y='NR_DAUNE')
'''

#3. Încărcați într-un df  numele, suma solicitată, suma din depozite și fidelitatea clienților cu vârsta > 30 de ani care au solicitat un credit mai mare de 10.000 lei. Verificați în df dacă suma din depozit este mai mare decât suma solicitată și pentru acești clienți modificați fidelitatea în 5 (doar în df).
'''
import cx_Oracle
import pandas as pd
from pprint import pprint
connection = cx_Oracle.connect("BDSA_POPESCUM", "STUD", "193.226.34.57/oradb")

query="""SELECT nume_client, suma_solicitata, suma_depozit, fidelitate FROM t_clienti_leasing where varsta > 30 and suma_solicitata > 10000"""
df = pd.read_sql(query, con=connection)
pprint(df)
df.loc[(df["SUMA_DEPOZIT"] > df["SUMA_SOLICITATA"]), ["FIDELITATE"]] = 5
pprint(df)
'''

#4. Încărcați într-un df  profesia, venitul anual, suma din depozite și suma solicitată pe fiecare profesie. În df adăugați o nouă coloană pentru a calcula gradul de îndatorare pe fiecare profesie (suma_solicitata/(venit_anual+suma_depozit)*100).
'''
import cx_Oracle
import pandas as pd
from pprint import pprint
connection = cx_Oracle.connect("BDSA_POPESCUM", "STUD", "193.226.34.57/oradb")
query = """SELECT profesia, venit_anual, sum(suma_solicitata) suma_solicitata, SUM(suma_depozit) suma_depozit FROM t_clienti_leasing GROUP_BY by profesia, venit_anual"""
df = pd.read_sql(query, con=connection)
#pprint(df)
df["GRAD_INDATORARE"] = round(df["SUMA_SOLICITATA"] / (df["VENIT_ANUAL_RON"]+df["SUMA_DEPOZIT"])*100,2)
pprint(df)
'''

#5. Încărcați într-un df starea civilă, profesia și suma totală solicitată grupată în funcție de aceste atribute.  Introduceți de la tastatură profesia și pentru aceasta reprezentați grafic suma solicitată în funcție de starea civilă.
import cx_Oracle
import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt
from click._compat import raw_input
connection = cx_Oracle.connect("BDSA_POPESCUM", "STUD", "193.226.34.57/oradb")
profesia = raw_input("Scrie profesia: ")
query="""SELECT stare_civila,profesia, SUM(suma_solicitata) FROM t_clienti_leasing WHERE profesia = :profesia GROUP BY stare_civila,profesia"""
df = pd.read_sql(query, con=connection, params={'profesia': profesia})
#pprint(df)
df.plot(kind='bar', color='green')
plt.show()