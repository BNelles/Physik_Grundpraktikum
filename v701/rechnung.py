import numpy as np
from uncertainties import ufloat


E1=ufloat(27.45,7.51)
E2=ufloat(44.16,4.83)

d1=0.022
d2=ufloat(0.018,0.003)

print(E2/E1)
print(d2/d1)