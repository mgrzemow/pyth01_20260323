import json
from pprint import pprint

import requests

r = requests.get('https://api.nbp.pl/api/exchangerates/tables/a/?format=json')
j = r.json()
pprint(j)

with open('plik.json', 'wt', encoding='utf-8') as f:
    json.dump(j, f)

# jeżeli ma być human readable
with open('plik1.json', 'wt', encoding='utf-8') as f:
    json.dump(j, f, ensure_ascii=False, indent=2)

with open('plik1.json', 'rt', encoding='utf-8') as f:
    j = json.load(f)
    pprint(j)

kursy = {}
for n in j[0]['rates']:
    kursy[n['code']] = n['mid']

pprint(kursy)

x = [kod.lower() for kod in kursy]
with open('kody.json', 'wt', encoding='utf-8') as f:
    json.dump(x, f, ensure_ascii=False, indent=2)

# serializacja
# podstawowy format - pickle
import datetime as dt
import pickle
d1 = dt.date.today()

with open('data.pickle', 'wb') as f:
    pickle.dump(d1, f)

with open('data.pickle', 'rb') as f:
    d2 = pickle.load(f)

print(d1, d2)

# w przypadku modeli AI pickle niewydajny - użyjemy marshall

# uwaga na XML - wbudowane parsery są słabe
# lepszy parser - beatifulsoup
# zaawansowany parser - lxml
# altermatywnie - konwersja do json, np xmljson

# inne formaty - patrz pandas - np csv, excel
# zaawansowana biblioteka do excela - xlwings

