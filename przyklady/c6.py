# if warunek1:


#     kod
# elif warunek2:
#     kod
# elif warunek3:
#     kod
# else:
#     kod

import datetime as dt

x = dt.date.today()
x = None

if x:
    print(True)
else:
    print(False)

import re
m = re.match('\\d\\d', '2d')
if m:
    print('Jest dopasowanie', m)
else:
    print('Brak dopasowania', m)
    
# co z klasami
class A:
    # BARDZO ZŁY POMYSŁ!!!
    def __bool__(self):
        return False

a = A()
if a:
    print(True)
else:
    print(False)

print(True or False)
print(True and False)
print(not True)





