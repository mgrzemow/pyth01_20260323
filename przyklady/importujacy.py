import math


print(math.pi)
from math import pi, e, sqrt
print(pi)
import datetime as dt
print(dt.datetime.now())
from math import e as liczba_e
print(liczba_e)

# uwaga - ryzyko powtórzenia się i nadpisania symboli
from urllib import *
from requests import *

import subdir1.subdir2.importowany
subdir1.subdir2.importowany.f1()

import subdir1.subdir2.importowany as importowany
importowany.f1()

