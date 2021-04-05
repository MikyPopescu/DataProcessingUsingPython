# 1. Pe baza colecției clienti_leasing din MongoDB, încărcați într-un df  numele, suma solicitată, suma din depozite și fidelitatea clienților cu vârsta > 35 de ani care au solicitat un credit mai mare de 15.000$. Verificați în df dacă suma din depozit este mai mare decât suma solicitată și pentru acești clienți modificați fidelitatea în 5. Salvați setul de date într-un fișier .csv (clienti_leasing.csv).
'''
import pymongo
import pandas as pd
from pprint import pprint
conn = pymongo.MongoClient("mongodb://master:stud1234@37.120.249.57:27017/?authSource=daune_leasing&authMechanism=SCRAM-SHA-256")
print(conn.list_database_names())
db = conn["daune_leasing"]
#pprint(db.list_collection_names())
collection = db["clienti_leasing"]
projection={"_id":0,
            "NUME_CLIENT":1,
            "SUMA_SOLICITATA":1,
            "SUMA_DEPOZIT":1,
            "FIDELITATE":1
   }
cursor = collection.find({"VARSTA": {'$gt': 35},"SUMA_SOLICITATA": {'$gt': 15000}}, projection = projection)
df = pd.DataFrame.from_dict(list(cursor))
df.loc[(df["SUMA_DEPOZIT"] > df["SUMA_SOLICITATA"]), ["FIDELITATE"]] = 5
#pprint(df)
df.to_csv('clienti.csv')
cursor.close()
'''
# 2. Pe baza colecției clienti_leasing din MongoDB, încărcați într-un df  profesia, venitul anual, suma din depozite și suma solicitată pe fiecare profesie. În df adăugați o nouă coloană pentru a calcula gradul de îndatorare pe fiecare profesie (suma_solicitata/(venit_anual+suma_depozit)*100). Reprezentați grafic gradul de îndatorare pe fiecare profesie.
'''
import pymongo
import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint
conn = pymongo.MongoClient("mongodb://master:stud1234@37.120.249.57:27017/?authSource=daune_leasing&authMechanism=SCRAM-SHA-256")
db = conn["daune_leasing"]
#print(conn.list_database_names())
collection = db["clienti_leasing"]
projection = {"_id": 0,
              "PROFESIA": 1,
              "SUMA_DEPOZIT": 1,
              "SUMA_SOLICITATA": 1,
              "VENIT_ANUAL_RON": 1,
              }
cursor = collection.find({}, projection = projection)
df = pd.DataFrame.from_dict(list(cursor))
#print(df)
#print(df.dtypes)
cursor.close()
df['SUMA_DEPOZIT'] = pd.to_numeric(df['SUMA_DEPOZIT'], errors='coerce')
df["GRAD_INDATORARE"] = round(df["SUMA_SOLICITATA"] / (df["VENIT_ANUAL_RON"] + df["SUMA_DEPOZIT"]) * 100, 2)
df.plot(kind='bar', color='green')
plt.show()
# pprint(df)
'''
# 3. Pe baza colecției clienti_daune din MongoDB, încărcați într-un df marca, modelul, valoarea totală și numărul de daune pe fiecare model și marcă fabricate între 2010 și 2012. Afișați numărul de autoturisme pentru care valoarea totală depășește 30.000$. Reprezentați grafic modelele care au înregistrat mai mult de 100 de daune.
'''
import pymongo
import pandas as pd
from pprint import pprint
conn = pymongo.MongoClient("mongodb://master:stud1234@37.120.249.57:27017/?authSource=daune_leasing&authMechanism=SCRAM-SHA-256")
db = conn["daune_leasing"]
#print(db.list_collection_names())
collection = db["clienti_daune"]
pipeline = [{'$group': {
    "_id": {"MARCA": "$MARCA",
            "MODEL": "$MODEL"
            },
    "VALOARE_DAUNA": {'$sum': "$VALOARE_DAUNA"},
    "TOTAL_DAUNE": {'$sum': 1},

}},
      { '$match': { 'AN_FABRICATIE': {'$in': ['2019','2011','2012']} } }
]
# cursor = collection.find({'AN_FABRICATIE': {'$gt': 2010}}, projection = pipeline)
#df = pd.DataFrame.from_dict(list(cursor))
#print(df)
#df.plot(kind='bar', color='green')
'''

# 4. Pe baza colecției clienti_daune din MongoDB, într-un df marca, modelul, anul de fabricație, componenta, prețul total și prețul manoperei pentru autoturismele din mărcile AUDI, BMW, FORD, FIAT. Calculați procentul manoperei din prețul total.
'''
import pymongo
import pandas as pd
from pprint import pprint

conn = pymongo.MongoClient("mongodb://master:stud1234@37.120.249.57:27017/?authSource=daune_leasing&authMechanism=SCRAM-SHA-256")
print(conn.list_database_names())
db = conn["daune_leasing"]
print(db.list_collection_names())
collection = db["clienti_daune"]
pipeline = [{'$project': {
    "_id": 0,
    "AN_FABRICATIE": 1,
    "MARCA": 1,
    "COMPONENTA": 1,
    "PRET_MANOPERA": 1,
    "PRET_TOTAL": 1,

}},
    {'$match': {'MARCA': {'$in': ['AUDI', 'BMW', 'FORD', 'FIAT']}}},
]

# cursor = collection.find({'AN_FABRICATIE': {'$gt': 2010}}, projection=pipeline)
cursor = collection.aggregate(pipeline)
df = pd.DataFrame.from_dict(list(cursor))
df['PROCENT_MANOPERA'] = (df['PRET_MANOPERA'] / df['PRET_TOTAL']) * 100
pprint(df)
'''
# 5. Modificați exemplele 5 și 15 astfel încât tabela T_CLIENTI_DAUNE din MySQL să fie înlocuite cu tabela similară din baza de date Oracle din schema student_ps.
'''
import pandas as pd
import flask
from flask import request, jsonify
import json
import cx_Oracle
import pymongo

app = flask.Flask(__name__)
app.config["DEBUG"] = False


# home page
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Regasirea clientilor cu daune</h1>
<p>API pentru afisarea clientilor cu daune.</p>'''

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

# pagina: http://127.0.0.1:5000/api/v1/resources/daune_clienti?suma_solicitata=7000&valoare_dauna=1000
@app.route('/api/v1/resources/daune_clienti', methods=['GET'])
def api_daune_clienti():
    # Verificarea parametrului introdus in URL.
    #if
    #else:
        
    connection = cx_Oracle.connect("BDSA_POPESCUM", "STUD", "193.226.34.57/oradb")
    connection.close()


app.run()
'''