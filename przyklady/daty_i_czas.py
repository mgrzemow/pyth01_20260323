import datetime as dt
import time
d = '1995.12.23 12:33:23'
d1 = dt.datetime.strptime(d, '%Y.%m.%d %H:%M:%S')
print(d1)
t = d1.isoformat()
print(t)
d2 = dt.datetime.fromisoformat(t)
print(d2)

print(d1 > d2)

# timedelta - wygodna klasa do przeliczania czasów
d1 = dt.datetime.now()
time.sleep(2)
d2 = dt.datetime.now()
print(d2-d1, type(d2-d1))

# data 14 dni do przodu
d1 = dt.date.today()
td1 = dt.timedelta(days=1)
d2 = d1 + 14 * td1
print(d2)

import calendar, dateutil


