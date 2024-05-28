import numpy as np
from uncertainties import ufloat

E=ufloat(47,2.8)
E_t=34.1

A=ufloat(42.4,1.4)
A_t=12.1

print((A-A_t)/A_t*100)