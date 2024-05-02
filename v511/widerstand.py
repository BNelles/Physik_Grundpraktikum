import numpy as np
from uncertainties import ufloat


k=ufloat(0.104,0.001)
s=ufloat(0.263,0.001)

A_k=np.pi*(k/2)**2
A_s=np.pi*(s/2)**2

R_k=2.7050
R_s=0.6086

l_k=1.37
l_s=1.73

p_k=(A_k*R_k)/l_k
p_s=(A_k*R_s)/l_s

print(p_k,p_s)
